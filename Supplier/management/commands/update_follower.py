from django.core.management.base import BaseCommand, CommandError
from Supplier.models import Supplier
from Supplier.utility import *
from Supplier.utility_numbers import *
from Supplier.utility_sync import SyncUtility

class Command(BaseCommand):
    help = 'Update follower'

    def add_arguments(self, parser):
        parser.add_argument('--ids', nargs='+', type=int)
        parser.add_argument(
            '--all',
            action='store_true',
            dest='all',
            help='Select all instead of id',
        )
        parser.add_argument('--range', nargs='+', type=int)

    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS('call update_follower command success, checking arg'))
        sync_thread = SyncUtility()
        if options['all']:
            sync_thread.sync_follower()
        elif options['ids']:
            shouldSetupFb = False
            shouldSetupInstagram = False
            suppliers = []
            for supplier_id in options['ids']:
                try:
                    supplier = Supplier.objects.get(pk=supplier_id)
                    shouldSetupFb = shouldSetupFb or supplier.channel == SupplierChannel.FB_PERSONAL
                    shouldSetupInstagram = shouldSetupInstagram or supplier.channel == SupplierChannel.INSTAGRAM
                    suppliers.append(supplier)
                except Supplier.DoesNotExist:
                    raise CommandError('Supplier "%s" does not exist' % supplier_id)
            sync_thread.sync_suppliers(suppliers, shouldSetupFb, shouldSetupInstagram)
        elif options['range']:
            shouldSetupFb = False
            shouldSetupInstagram = False
            suppliers = []
            if len(options['range']) < 2:
                raise CommandError('Provide range with from to')

            _from = options['range'][0]
            _to = options['range'][1]
            for supplier_id in range(_from, _to, 1):
                try:
                    supplier = Supplier.objects.get(pk=supplier_id)
                    shouldSetupFb = shouldSetupFb or supplier.channel == SupplierChannel.FB_PERSONAL
                    shouldSetupInstagram = shouldSetupInstagram or supplier.channel == SupplierChannel.INSTAGRAM
                    suppliers.append(supplier)
                except Supplier.DoesNotExist:
                    raise CommandError('Supplier "%s" does not exist' % supplier_id)
            sync_thread.sync_suppliers(suppliers, shouldSetupFb, shouldSetupInstagram)


        self.stdout.write(self.style.SUCCESS('Sync End'))