# -*- coding: utf-8 -*-
import csv
from importlib.metadata import requires
from django.http import HttpResponse
from django.conf import settings
from django.core.exceptions import PermissionDenied
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
import pandas as pd
from django.utils.html import strip_tags
from django.contrib import messages
from io import BytesIO as IO
from django.conf import settings
from django.contrib import admin
from django.contrib.auth import get_permission_codename
from django.contrib.auth.models import User, Permission
from django.contrib.contenttypes.models import ContentType
from .utility import *
from datetime import datetime

from siteconfig.models import UserProfile, UserEventLog

from .supportmodels import SupplierChannel, support_sync

class ExportCsvMixin:
    def export_as_csv(self, request, queryset):
        print("XIn CHAO export_as_csv")

        meta = self.model._meta
        field_names = [field.name for field in meta.industries]

        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename={}.csv'.format(meta)
        writer = csv.writer(response)

        writer.writerow(field_names)
        for obj in queryset:
            data = [getattr(obj, field) for field in field_names]
            print('Data')
            print(data)
            row = writer.writerow(data)
            print('Row')
            print(row)

        return response

    export_as_csv.short_description = "Export Selected"

    @admin.action(permissions=['export'], description='Export selected rows to excel',)
    def export_as_xls(self, request, queryset):
        """
        Generic xls export admin action.
        """
        limit = -1
        in_capability = False
        if request.user.has_perm("Supplier.export_excel_1000_admin"):
            limit = settings.EXPORT_RECORDS_ADMIN_LIMIT
        elif request.user.has_perm("Supplier.export_excel_100_buyer"):
            limit = 100
        elif request.user.has_perm("Supplier.export_excel_50_seller"):
            limit = 50
        else:
            messages.error(request, "This action is only for staff of brandc" )
            return HttpResponseRedirect(request.path_info)
        
        user_profile, created = UserProfile.objects.get_or_create(user=request.user)
        if user_profile.download_capability <= 0:
            in_capability = False
        else:
            in_capability = True
            user_profile.download_capability = user_profile.download_capability - 1
            user_profile.save()

        if limit > 0 and queryset.count() > limit:
            messages.error(request, "Can't export more then %s Records in one go." % str(limit))
            log = UserEventLog(user=request.user, log="Cố gắng xuất file nhưng chọn quá nhiều items so với qui định", time = datetime.now())
            log.save()
            return HttpResponseRedirect(request.path_info)
        
        if in_capability == False:
            messages.error(request, "Please contact Admin of Brandc to grant the download capability!")
            log = UserEventLog(user=request.user, log="Cố gắng xuất file nhưng đã hết quota!", time = datetime.now())
            log.save()
            return HttpResponseRedirect(request.path_info)
        log = UserEventLog(user=request.user, log="Xuất file thành công", time = datetime.now())
        log.save()

        data = []
        for obj in queryset:
            data.append(obj.parse_to_json())
        

        excel_file = IO()
        xlwriter = pd.ExcelWriter(excel_file, engine='xlsxwriter')
        df = pd.DataFrame(data)
        df.to_excel(xlwriter, "Summary", index=False)

        # Get the xlsxwriter workbook and worksheet objects.
        workbook  = xlwriter.book
        worksheet = xlwriter.sheets['Summary']

        # Set a currency number format for a column.
        num_format = workbook.add_format({'num_format': '#,###'})
        for column in df:
            column_length = max(df[column].astype(str).map(len).max(), len(column))
            col_idx = df.columns.get_loc(column)
            #print('col_idx')
            #print(col_idx)
            worksheet.set_column(col_idx, col_idx, column_length)

        worksheet.set_column('H:H', 15, num_format)
        worksheet.set_column('J:J', 15)
        worksheet.set_column('M:M', 15, num_format)
        worksheet.set_column('N:N', 15, num_format)
        worksheet.set_column('O:O', 15, num_format)
        worksheet.set_column('P:P', 15, num_format)
        


        xlwriter.save()
        xlwriter.close()

        excel_file.seek(0)
        response = HttpResponse(excel_file.read(),
                                content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')

        response['Content-Disposition'] = 'attachment; filename="excel_file.xlsx"'
        return response

    export_as_xls.short_description = "Export selected to EXCEL"

    def has_export_permission(self, request):
        """Does the user have the export excel permission?"""
        #opts = self.opts
        #codename = get_permission_codename('export', opts)
        has_perm = request.user.has_perm('Supplier.export_excel_50_seller') | request.user.has_perm('Supplier.export_excel_100_buyer') | request.user.has_perm('Supplier.export_excel_1000_admin')
        return has_perm
    
    @admin.action(permissions=['syncfollower'], description='Sync follower number',)
    def sync_follower(self, request, queryset):
        limit = 4
        if limit > 0 and queryset.count() > limit:
            messages.error(request, "Can't sync more than %s Records in one go." % str(limit))
            return HttpResponseRedirect(request.path_info)
        
        shouldSetupFb = queryset.filter(channel=SupplierChannel.FB_PERSONAL).count() > 0 \
            or queryset.filter(channel=SupplierChannel.FB_FANPAGE).count() > 0 \
                or queryset.filter(channel=SupplierChannel.FB_GROUP).count() > 0
        shouldSetupInstagram = queryset.filter(channel=SupplierChannel.INSTAGRAM).count() > 0
        
        driver = prepare_driver(shouldSetupFb, shouldSetupInstagram)
        for obj in queryset:
            result = -1
            if support_sync(obj.channel):
                result = read_followers(driver, obj)
                if result > 0:
                    old_follower = obj.follower
                    obj.follower = convert_to_string_number(result)
                    try:
                        obj.save()
                        messages.info(request, obj.name + " was update follower number from " + old_follower + " to " +  str(obj.follower))
                    except Exception as e:
                        messages.warning(request, obj.name + " can not update follower number, let try manual for this record, the error is " + str(e))
                else:
                    messages.warning(request, obj.name + " can not update follower number, let try manual for this record")
            else:
                messages.warning(request, obj.name + " is not supported this feature")
        if driver:
            try:
                close_driver(driver)
                driver = None
            except:
                pass
        
        return HttpResponseRedirect(request.path_info)

    def has_syncfollower_permission(self, request):
        """Does the user have the sync follower permission?"""
        has_perm = request.user.has_perm('Supplier.sync_follower')
        return has_perm