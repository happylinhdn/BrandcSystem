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

        # KhanhHoaCount1 = Supplier.objects.filter(location='Khánh Hoà').count()
        # KhanhHoaCount2 = Supplier.objects.filter(location='Khánh Hòa').count()
        # self.stdout.write(self.style.SUCCESS('Successfully Read All KhanhHoaCount1 Supplier "%s"' % KhanhHoaCount1))
        # self.stdout.write(self.style.SUCCESS('Successfully Read All KhanhHoaCount2 Supplier "%s"' % KhanhHoaCount2))
        # Supplier.objects.filter(location='Khánh Hoà').update(location='Khánh Hòa')
        # KhanhHoaCount1 = Supplier.objects.filter(location='Khánh Hoà').count()
        # KhanhHoaCount2 = Supplier.objects.filter(location='Khánh Hòa').count()
        # self.stdout.write(self.style.SUCCESS('Update after KhanhHoaCount1 Supplier "%s"' % KhanhHoaCount1))
        # self.stdout.write(self.style.SUCCESS('Update after KhanhHoaCount2 Supplier "%s"' % KhanhHoaCount2))