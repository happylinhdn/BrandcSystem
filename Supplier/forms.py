from django.forms import ModelForm, MultipleChoiceField
from .models import SupplierModel
from .supportmodels import Fields

class SupplierForm(ModelForm):
    class Meta:
        model = SupplierModel
        fields = '__all__'
        localized_fields = ['original_cost_picture', 'original_cost_video', 'original_cost_event', 'original_cost_tvc']