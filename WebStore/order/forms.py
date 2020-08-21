from django.forms import ModelForm
from .models import Order

class ShippingDataForm(ModelForm):
    class Meta:
        model = Order
        fields = ['user_name', 'user_gender', 'user_contact_phone_no', 'shipping_postal_code', 'shipping_address']
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.label_suffix = ''