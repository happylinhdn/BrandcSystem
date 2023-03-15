from django.core.management.base import BaseCommand, CommandError
from Supplier.models import Supplier

class Command(BaseCommand):
    help = 'Correct location'

    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS('call update_follower command success, checking arg'))
        count = Supplier.objects.count()
        self.stdout.write(self.style.SUCCESS('Successfully Read All Supplier "%s"' % count))
        GeneralCount = Supplier.objects.filter(location='General').count()
        self.stdout.write(self.style.SUCCESS('Successfully Read All GeneralLocation Supplier "%s"' % GeneralCount))
        Supplier.objects.filter(location='General').update(location='Toàn Quốc')
        emptyLocation = Supplier.objects.filter(location=None).count()
        self.stdout.write(self.style.SUCCESS('Successfully Read All EmptyLocation Supplier "%s"' % emptyLocation))