from django.core.management.base import BaseCommand, CommandError
from Supplier.models import Supplier
from Supplier.supportmodels import isFbChannel
from Supplier.utility import *
from Supplier.utility_numbers import *
from siteconfig.models import BackgroundLog, BackgroundLogDevOnly
from Supplier.utility_sync import SyncUtility
import re

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
        parser.add_argument('--logs')
        parser.add_argument('--channel')
        parser.add_argument('--check_hl')



    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS('call update_follower command success, checking arg'))
        sync_thread = SyncUtility(True)
        if options['channel']:
            self.sync_by_channel(options['channel'])
        elif options['check_hl']:
            self.check_hl()
        elif options['logs']:
            self.show_logs_fail()
        elif options['all']:
            sync_thread.sync_follower()
        elif options['ids']:
            shouldSetupFb = False
            shouldSetupInstagram = False
            suppliers = []
            for supplier_id in options['ids']:
                try:
                    supplier = Supplier.objects.get(pk=supplier_id)
                    shouldSetupFb = shouldSetupFb or isFbChannel(supplier.channel)
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
                    shouldSetupFb = shouldSetupFb or isFbChannel(supplier.channel)
                    shouldSetupInstagram = shouldSetupInstagram or supplier.channel == SupplierChannel.INSTAGRAM
                    suppliers.append(supplier)
                except Supplier.DoesNotExist:
                    raise CommandError('Supplier "%s" does not exist' % supplier_id)
            sync_thread.sync_suppliers(suppliers, shouldSetupFb, shouldSetupInstagram)


        self.stdout.write(self.style.SUCCESS('Sync End'))
    def show_logs_fail(self):
        self.stdout.write(self.style.SUCCESS('Do sync log fails'))

        failLogs = BackgroundLogDevOnly.objects.filter(isSuccess=False)
        #count = failLogs.count()
        #self.stdout.write(self.style.SUCCESS('Log fails = %s') % count)
        ids = []
        for logObj in failLogs:
            ids += self.detectFailNumber(logObj.log)
        shouldSetupFb = False
        shouldSetupInstagram = False
        suppliers = []
        self.stdout.write(self.style.SUCCESS('fails = %s') % len(ids))
        for id in ids:
            try:
                supplier_id = id.removeprefix('(').removesuffix(')')
                supplier = Supplier.objects.get(pk=supplier_id)
                shouldSetupFb = shouldSetupFb or isFbChannel(supplier.channel)
                shouldSetupInstagram = shouldSetupInstagram or supplier.channel == SupplierChannel.INSTAGRAM
                suppliers.append(supplier)
            except Supplier.DoesNotExist:
                print('Supplier "%s" does not exist' % id)
        
        sync_thread = SyncUtility(True)
        sync_thread.sync_suppliers(suppliers, shouldSetupFb, shouldSetupInstagram)
        
    def detectFailNumber(self, text):
        outputs = []
        regex = r"\([+-]?\d+?\)"
        matches = re.finditer(regex, text, re.MULTILINE)

        for matchNum, match in enumerate(matches, start=1):
            raw = match.group()
            #print ("Match {matchNum} was found at {start}-{end}: {match}".format(matchNum = matchNum, start = match.start(), end = match.end(), match = raw))
            outputs.append(raw)
        myunique = set(outputs)
        return myunique  

    def sync_by_channel(self, channel):
        print('sync_by_channel', channel)
        sync_thread = SyncUtility(True)
        sync_thread.sync_channel(channel)
        
    def check_hl(self):
        suppliers = Supplier.objects.filter(link__contains='hl=')
        count = suppliers.count()
        print('check_hl', count)
        for sup in suppliers:
            print(sup.id, sup.name, sup.link)
        
        for channel in SupplierChannel.choices:
            print('channel', channel[0])