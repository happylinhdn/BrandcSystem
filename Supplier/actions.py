# -*- coding: utf-8 -*-
import csv
import imp
from importlib.metadata import requires
from django.http import HttpResponse

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

from .models import Supplier

# content_type = ContentType.objects.get_for_model(Supplier)
# post_permission = Permission.objects.filter(content_type=content_type)
#print([perm.codename for perm in post_permission])
# for perm in post_permission:
#     print(perm, perm.codename)
#     if perm.codename in ('export_excel_50', 'export_excel_100', 'export_excel_1000', 'export_excel_as_admin', 'export_excel_as_staff'):
#         print ('do remove ', perm.codename)
#         perm.delete()


class ExportCsvMixin:
    def export_as_csv(self, request, queryset):
        meta = self.model._meta
        field_names = [field.name for field in meta.fields]

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
        if request.user.has_perm("Supplier.export_excel_1000_admin"):
            limit = 1000#settings.EXPORT_RECORDS_ADMIN_LIMIT
        elif request.user.has_perm("Supplier.export_excel_100_buyer"):
            limit = 100
        elif request.user.has_perm("Supplier.export_excel_50_seller"):
            limit = 50
        else:
            messages.error(request, "This action is only for staff of brandc" )
            return HttpResponseRedirect(request.path_info)

        if limit > 0 and queryset.count() > limit:
            messages.error(request, "Can't export more then %s Records in one go." % str(limit))
            return HttpResponseRedirect(request.path_info)
        
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
        #result = read_followers('https://www.facebook.com/lebaobinh.fan', SupplierChannel.FB_PERSONAL) - success
        #result = read_followers('https://www.facebook.com/hoquanghieutv', SupplierChannel.FB_PERSONAL)# - fail
        #result = read_followers('https://www.facebook.com/IQFact', SupplierChannel.FB_FANPAGE) - success
        #result = read_followers('https://www.facebook.com/fanpageNGLG/', SupplierChannel.FB_FANPAGE) - success
        #result = read_followers('https://www.facebook.com/groups/groupyanpets/', SupplierChannel.FB_GROUP) - sucecss
        #result = read_followers('https://www.facebook.com/groups/saigonconfession/', SupplierChannel.FB_GROUP) - success
        #result = read_followers('https://www.tiktok.com/@tyle1994?lang=vi-VN', SupplierChannel.TIKTOK_PERSONAL) - success
        #result = read_followers('https://www.tiktok.com/@quynhitraan?lang=vi-VN', SupplierChannel.TIKTOK_PERSONAL) - success
        # result = read_followers('https://www.tiktok.com/@theanh28entertainment?lang=vi-VN', SupplierChannel.TIKTOK_COMMUNITY) - success
        # result = read_followers('https://www.tiktok.com/@60giay.com', SupplierChannel.TIKTOK_COMMUNITY) - success
        # result = read_followers('https://www.youtube.com/user/otosaigon', SupplierChannel.YOUTUBE_COMMUNITY) - success
        #result = read_followers('https://www.youtube.com/c/ThanhCongTC', SupplierChannel.YOUTUBE_COMMUNITY)
        limit = 4
        if limit > 0 and queryset.count() > limit:
            messages.error(request, "Can't sync more than %s Records in one go." % str(limit))
            return HttpResponseRedirect(request.path_info)
        driver = prepare_driver()
        for obj in queryset:
            result = read_followers(driver, obj.link, obj.channel)
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
        
        
        return HttpResponseRedirect(request.path_info)

    def has_syncfollower_permission(self, request):
        """Does the user have the sync follower permission?"""
        has_perm = request.user.has_perm('Supplier.sync_follower')
        return has_perm