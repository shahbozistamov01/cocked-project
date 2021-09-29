from django import forms
from .models import bootstrap_user



class UserModelForm(forms.ModelForm):
    class Meta:
        model = bootstrap_user
        fields = '__all__'


