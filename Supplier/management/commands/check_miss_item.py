from django.core.management.base import BaseCommand, CommandError
from Supplier.models import Supplier

class Command(BaseCommand):
    help = 'Check miss item'
    def add_arguments(self, parser):
        parser.add_argument('--max_id', nargs='+', type=int)
        
    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS('call Check miss item'))
        count = Supplier.objects.count()
        self.stdout.write(self.style.SUCCESS('All Supplier is "%s"' % count))
        max_id = count
        if options['max_id']:
            max_id = options['max_id'][0]
                
        countMiss = 0
        log = ''
        for id in range(1, max_id, 1):
            try:
                supplier = Supplier.objects.get(pk=id)
            except Supplier.DoesNotExist:
                countMiss = countMiss + 1
                log += "%d, " % id
        if countMiss > 0:
            print("%d Missing item, ids is: %s" % (countMiss, log))
        else:
            print("All items is correct, no missing")
