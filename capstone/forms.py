from django import forms
from .models import Computer

class ComputerForm(forms.ModelForm):
    class Meta:
        model = Computer
        exclude = ["department", "created_at", "responsible","id"]

form = ComputerForm()