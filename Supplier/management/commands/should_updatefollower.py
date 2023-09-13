from django.core.management.base import BaseCommand, CommandError
from Supplier.models import SupplierModel
from Supplier.supportmodels import isFbChannel
from Supplier.utility import *
from Supplier.utility_numbers import *
from siteconfig.models import BackgroundLogDevOnly
from Supplier.utility_sync import SyncUtility
import re

class Command(BaseCommand):
    help = 'Should Update follower'

    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS('call command success, checking arg'))
        self.check_sync_today()

        self.stdout.write(self.style.SUCCESS('Sync End'))

    def check_sync_today(self):
        print('check_sync_today')
        sync_thread = SyncUtility(True)
        should_sync = sync_thread.should_sync()
        print("Check should_sync result = ", should_sync)
        handle_channel = sync_thread.store_last_sync() 
        print("handle_channel = ", handle_channel)       