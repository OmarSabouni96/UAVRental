# forms.py
from django import forms
from .models import UAV, UAVRental
from django.core.exceptions import ValidationError

class UAVForm(forms.ModelForm):
    class Meta:
        model = UAV
        # fields = '__all__'
        exclude = ['user']


    def __init__(self, *args, **kwargs):
        super(UAVForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'input'})



class RentalForm(forms.ModelForm):
    class Meta:
        model = UAVRental
        fields = ['rental_start_date', 'rental_end_date']
        widgets = {
            'rental_start_date': forms.DateInput(attrs={'type': 'date'}),
            'rental_end_date': forms.DateInput(attrs={'type': 'date'}),
        }


    def __init__(self, *args, **kwargs):
        super(RentalForm, self).__init__(*args, **kwargs)






