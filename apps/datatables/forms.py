from django import forms

from apps.home.models import Data


class TransactionForm(forms.ModelForm):

    name = forms.CharField(label="Name", widget=forms.TextInput(attrs={'class': 'form-control transaction'}))

    value = forms.DecimalField(label="Total", max_digits=10, decimal_places=2,
                               widget=forms.TextInput(
                                   attrs={'class': 'form-control transaction', 'placeholder': '...'}))

    class Meta:
        model = Data
        fields = ['name', 'value']
