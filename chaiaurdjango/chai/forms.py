from django import forms
from .models import ListChai

class ListChaiForm(forms.Form):
    chai_variety=forms.ModelChoiceField(queryset=ListChai.objects.all(),label="Select Chai Variety")