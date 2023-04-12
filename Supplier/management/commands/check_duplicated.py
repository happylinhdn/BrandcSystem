from django.core.management.base import BaseCommand, CommandError
from Supplier.models import Supplier

class Command(BaseCommand):
    help = 'Check duplicated item'
        
    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS('call Check duplicated item'))
        count = Supplier.objects.count()
        self.stdout.write(self.style.SUCCESS('All Supplier is "%s"' % count))
        mylinks = [ supplier.link for supplier in  Supplier.objects.all()]
        dup = {x for x in mylinks if mylinks.count(x) > 1}
        self.stdout.write(self.style.SUCCESS('Duplicated Supplier is "%s"' % len(dup)))
        print(dup)