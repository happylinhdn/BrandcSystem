from django.core.management.base import BaseCommand, CommandError
from Supplier.models import Supplier

class Command(BaseCommand):
    help = 'Correct location'

    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS('call correct location'))
        count = Supplier.objects.count()
        self.stdout.write(self.style.SUCCESS('Successfully Read All Supplier "%s"' % count))
        KhanhHoaCount1 = Supplier.objects.filter(location='Khánh Hoà').count()
        KhanhHoaCount2 = Supplier.objects.filter(location='Khánh Hòa').count()
        self.stdout.write(self.style.SUCCESS('Successfully Read All KhanhHoaCount1 Supplier "%s"' % KhanhHoaCount1))
        self.stdout.write(self.style.SUCCESS('Successfully Read All KhanhHoaCount2 Supplier "%s"' % KhanhHoaCount2))
        Supplier.objects.filter(location='Khánh Hoà').update(location='Khánh Hòa')
        KhanhHoaCount1 = Supplier.objects.filter(location='Khánh Hoà').count()
        KhanhHoaCount2 = Supplier.objects.filter(location='Khánh Hòa').count()
        self.stdout.write(self.style.SUCCESS('Update after KhanhHoaCount1 Supplier "%s"' % KhanhHoaCount1))
        self.stdout.write(self.style.SUCCESS('Update after KhanhHoaCount2 Supplier "%s"' % KhanhHoaCount2))