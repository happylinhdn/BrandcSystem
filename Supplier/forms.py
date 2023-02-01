from django.forms import ModelForm, MultipleChoiceField
from .models import Supplier
from .supportmodels import Fields

class SupplierForm(ModelForm):
    class Meta:
        model = Supplier
        fields = '__all__'
        localized_fields = ['original_cost_picture', 'original_cost_video', 'original_cost_event', 'original_cost_tvc']