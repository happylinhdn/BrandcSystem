from import_export import resources
from .models import SupplierModel

class SupplierResource(resources.ModelResource):
    class Meta:
        model = SupplierModel
        exclude = ('follower_2', )