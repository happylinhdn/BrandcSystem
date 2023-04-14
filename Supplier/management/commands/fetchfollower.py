from django.core.management.base import BaseCommand, CommandError
from Supplier.models import SupplierModel

class Command(BaseCommand):
    help = 'Fetch all suppliers'

    def add_arguments(self, parser):
        parser.add_argument('--ids', nargs='+', type=int)
        parser.add_argument(
            '--all',
            action='store_true',
            dest='all',
            help='Select all instead of id',
        )

    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS('call fetchFollower command success, checking arg'))
        if options['all']:
            count = SupplierModel.objects.count()
            self.stdout.write(self.style.SUCCESS('Successfully Read All Supplier "%s"' % count))
            return
        if options['ids']:
            for supplier_id in options['ids']:
                try:
                    supplier = SupplierModel.objects.get(pk=supplier_id)
                except SupplierModel.DoesNotExist:
                    raise CommandError('Supplier "%s" does not exist' % supplier_id)

                # poll.opened = False
                # poll.save()
                # supplier.booking_contact_phone = 'Linh test \n' + (supplier.booking_contact_phone or '')
                supplier.save()

                self.stdout.write(self.style.SUCCESS('Successfully Read Supplier "%s"' % supplier_id))