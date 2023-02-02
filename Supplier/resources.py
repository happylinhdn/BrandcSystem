from import_export import resources
from .models import Supplier

class SupplierResource(resources.ModelResource):
    class Meta:
        model = Supplier
        exclude = ('follower_2', )