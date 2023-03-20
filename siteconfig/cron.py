from Supplier.utility_sync import SyncUtility

def sync_follower():
    sync_thread = SyncUtility()
    sync_thread.sync_follower()