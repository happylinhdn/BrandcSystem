from django.core.management.base import BaseCommand, CommandError
from Supplier.models import SupplierModel
from io import BytesIO as IO
import pandas as pd
import datetime

class Command(BaseCommand):
    help = 'Export suppliers'

    def add_arguments(self, parser):
        # parser.add_argument('--ids', nargs='+', type=int)
        # parser.add_argument('--ssid', nargs='+', type=str)
        parser.add_argument(
            '--all',
            action='store_true',
            dest='all',
            help='Select all instead of id',
        )

    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS('Call exportdata command success, checking arg'))
        count = SupplierModel.objects.count()
        if count > 0:
            self.do_export_all_2excel()
    
        # if options['ssid']:
        #     count = SupplierModel.objects.count()
        #     self.stdout.write(self.style.SUCCESS('Successfully exportdata Supplier "%s"' % count))
        #     return
        # if options['all']:
        #     count = SupplierModel.objects.count()
        #     self.stdout.write(self.style.SUCCESS('Successfully exportdata Supplier "%s"' % count))
        #     self.do_export_all_2excel()
        #     return
        
        # if options['ids']:
        #     for supplier_id in options['ids']:
        #         try:
        #             supplier = SupplierModel.objects.get(pk=supplier_id)
        #         except SupplierModel.DoesNotExist:
        #             raise CommandError('Supplier "%s" does not exist' % supplier_id)
        #         supplier.save()

        #         self.stdout.write(self.style.SUCCESS('Successfully exportdata "%s"' % supplier_id))
    
    

    def do_export_all_2excel(self):
        self.stdout.write(self.style.SUCCESS('do_export_all_2excel Start'))
        today = datetime.datetime.today()
        ddmmyy = today.strftime("%Y%m%d_%H%M%S")
        output = f'./tmp/data_{ddmmyy}.xlsx'
        self.stdout.write(self.style.SUCCESS(f'do_export_all_2excel output={output}'))

        data = []
        for obj in SupplierModel.objects.all().order_by('id'):
            data.append(obj.parse_to_json())
        

        #excel_file = IO()
        xlwriter = pd.ExcelWriter(output, engine='xlsxwriter')
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
        


        # xlwriter.save()
        xlwriter.close()

        self.stdout.write(self.style.SUCCESS('do_export_all_2excel End'))

        #excel_file.seek(0)