from django import forms
from .models import Application
from django import forms

class ApplicationForm(forms.ModelForm):
    class Meta:
        model = Application
        fields = [
            'surname', 'other_names',  'date_of_birth', 'disability', 'passport',
            'last_class', 'state_of_origin', 'lga', 'current_address', 'parent_name', 'parent_phone',
            'parent_address', 'parent_relationship', 'parent_email', 'special_needs', 'class_applying',
             'department', 'declaration'
        ]
        widgets = {
            'date_of_birth': forms.SelectDateWidget(years=range(1990, 2024)),
        }

from django import forms
from .models import Application

class ClassUpgradeForm(forms.ModelForm):
    class Meta:
        model = Application
        fields = ['class_applying']
        widgets = {
            'class_applying': forms.Select(choices=Application.CLASS_CHOICES)
        }



class PaystackPaymentForm(forms.Form):
    email = forms.EmailField()
    amount = forms.IntegerField()  # In kobo (multiply Naira by 100)

