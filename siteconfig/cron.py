from Supplier.utility_sync import SyncUtility
from Supplier.models import Supplier
from Supplier.supportmodels import SupplierChannel

def sync_follower():
    sync_thread = SyncUtility(False)
    sync_thread.sync_channels()

def sync_follower_ids():
    ids = [13, 1760, 1815]
    sync_thread = SyncUtility(True)
    shouldSetupFb = False
    shouldSetupInstagram = False
    suppliers = []
    for supplier_id in ids:
        try:
            supplier = Supplier.objects.get(pk=supplier_id)
            shouldSetupFb = shouldSetupFb or isFbChannel(supplier.channel)
            shouldSetupInstagram = shouldSetupInstagram or supplier.channel == SupplierChannel.INSTAGRAM
            suppliers.append(supplier)
        except:
            pass
    sync_thread.sync_suppliers(suppliers, shouldSetupFb, shouldSetupInstagram)

def isFbChannel(channel):
    supports = [
        SupplierChannel.FB_GROUP,
        SupplierChannel.FB_FANPAGE,
        SupplierChannel.FB_PERSONAL
    ]
    if channel in supports:
        return True

    return False