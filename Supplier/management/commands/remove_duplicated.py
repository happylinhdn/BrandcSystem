from django.core.management.base import BaseCommand, CommandError
from Supplier.models import SupplierModel

class Command(BaseCommand):
    help = 'Remove duplicated item'
        
    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS('call Remote duplicated item'))
        count = SupplierModel.objects.count()
        self.stdout.write(self.style.SUCCESS('All Supplier is "%s"' % count))
        mylinks = [ supplier.link for supplier in  SupplierModel.objects.all()]
        dup = [x for x in mylinks if mylinks.count(x) > 1]
        self.stdout.write(self.style.SUCCESS('Duplicated Supplier is "%s"' % len(dup)))
        #print(dup)
        for item in dup:
            #print(item)
            duplicated_ids = [x.id for x in SupplierModel.objects.filter(link=item)]
            max_id = max(duplicated_ids)
            SupplierModel.objects.get(pk=max_id).delete()

