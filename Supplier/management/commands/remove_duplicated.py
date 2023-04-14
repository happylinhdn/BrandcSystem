from django.core.management.base import BaseCommand, CommandError
from Supplier.models import Supplier

class Command(BaseCommand):
    help = 'Remove duplicated item'
        
    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS('call Remote duplicated item'))
        count = Supplier.objects.count()
        self.stdout.write(self.style.SUCCESS('All Supplier is "%s"' % count))
        mylinks = [ supplier.link for supplier in  Supplier.objects.all()]
        dup = [x for x in mylinks if mylinks.count(x) > 1]
        self.stdout.write(self.style.SUCCESS('Duplicated Supplier is "%s"' % len(dup)))
        #print(dup)
        for item in dup:
            #print(item)
            duplicated_ids = [x.id for x in Supplier.objects.filter(link=item)]
            max_id = max(duplicated_ids)
            Supplier.objects.get(pk=max_id).delete()

