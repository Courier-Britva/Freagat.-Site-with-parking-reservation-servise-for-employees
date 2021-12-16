from .models import ParkingList
from django.forms import ModelForm, TextInput


class ParkingListForm(ModelForm):
    class Meta:
        model = ParkingList
        fields = ['TimeStart', 'TimeEnd']
        widgets = {
            "TimeStart": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Write Here your Booking Start time!'
            }),
            "TimeEnd": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Write Here your Booking End time!'
            }),
        }

