import csv
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

# from django.contrib.auth.models import User, Permission
# from django.contrib.contenttypes.models import ContentType
# from .models import Supplier

# content_type = ContentType.objects.get_for_model(Supplier)
# post_permission = Permission.objects.filter(content_type=content_type)
# print([perm.codename for perm in post_permission])

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

    @admin.action(permissions=['export'], description='Mark selected stories as published',)
    def export_as_xls(self, request, queryset):
        """
        Generic xls export admin action.
        """
        limit = -1
        if request.user.has_perm("Supplier.export_excel_as_admin"):
            limit = settings.EXPORT_RECORDS_ADMIN_LIMIT
        elif request.user.has_perm("Supplier.export_excel_as_staff"):
            limit = settings.EXPORT_RECORDS_LIMIT
        else:
            messages.error(request, "This action is only for staff of brandc" )
            return HttpResponseRedirect(request.path_info)

        if queryset.count()>limit:
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
            print('col_idx')
            print(col_idx)
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
        """Does the user have the publish permission?"""
        #opts = self.opts
        #codename = get_permission_codename('export', opts)
        has_perm = request.user.has_perm('Supplier.export_excel_as_staff') | request.user.has_perm('Supplier.export_excel_as_admin')
        return has_perm