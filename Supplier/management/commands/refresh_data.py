from django.core.management.base import BaseCommand, CommandError
from Supplier.models import SupplierModel
from Supplier.supportmodels import YearCategory

class Command(BaseCommand):
    help = 'Refresh data for year category'
        
    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS('call Refresh data'))
        count = SupplierModel.objects.count()
        self.stdout.write(self.style.SUCCESS('All Supplier is "%s"' % count))
        all_suppliers = SupplierModel.objects.all().order_by('id')
        for supplier in all_suppliers:
            if supplier.year_of_birth != None:
                year = supplier.year_of_birth
                if year >= 1965 and year <= 1980:
                    supplier.year_category = YearCategory.GenX
                elif year >= 1981 and year <= 1996:
                    supplier.year_category = YearCategory.GenY
                elif year >= 1997 and year <= 2012:
                    supplier.year_category = YearCategory.GenY
                else:
                    supplier.year_category = YearCategory.General
            else:
                supplier.year_category = YearCategory.General
            supplier.save()