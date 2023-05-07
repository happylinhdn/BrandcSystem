from django.core.management.base import BaseCommand, CommandError
from Supplier.models import SupplierModel
from siteconfig.models import BackgroundLog
from datetime import timedelta
from django.utils import timezone

class Command(BaseCommand):
    help = 'Check old logs item'
        
    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS('call Check old logs'))
        #today = datetime.date.today()
        aPastWeek = timezone.now() - timedelta(days=2)
        
        oldDB = BackgroundLog.objects.filter(time__lte=aPastWeek)
        count = oldDB.count()
        self.stdout.write(self.style.SUCCESS('"%s" old logs will be deleted' % count))
        oldDB.delete()