from django import forms
from .models import Registration

class ApplicantForm(forms.ModelForm):
    class Meta:
        model = Registration
        fields = ['name','email','phone']