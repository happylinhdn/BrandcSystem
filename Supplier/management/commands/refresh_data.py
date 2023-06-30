from django.core.management.base import BaseCommand, CommandError
from Supplier.models import SupplierModel

class Command(BaseCommand):
    help = 'Refresh data'
        
    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS('call Refresh data'))
        count = SupplierModel.objects.count()
        self.stdout.write(self.style.SUCCESS('All Supplier is "%s"' % count))
        all_suppliers = SupplierModel.objects.all().order_by('id')
        for supplier in all_suppliers:
            supplier.save()