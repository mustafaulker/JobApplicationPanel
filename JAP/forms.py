from django import forms

from .models import PositionModel


class PositionForm(forms.ModelForm):
    class Meta:
        model = PositionModel
        fields = "__all__"
