from django.forms import ModelForm

from first.models import Vehicle


class New_vehicle(ModelForm):
    class Meta:
        model = Vehicle
        fields = "__all__"
