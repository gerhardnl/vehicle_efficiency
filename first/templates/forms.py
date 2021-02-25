from django.forms import ModelForm
from first.models import Vehicle
from django import forms

class New_vehicle(ModelForm):
    class Meta:
        model = Vehicle
        fields = "__all__"

class FileFieldForm(forms.Form):
    file_field = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True}))