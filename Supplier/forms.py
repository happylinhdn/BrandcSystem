
from django import forms
from .models import Supplier

class SupplierForm(forms.ModelForm):
    class Meta:
        model = Supplier
        fields = '__all__'
        localized_fields = ['original_cost_picture', 'original_cost_video', 'original_cost_event', 'original_cost_tvc']