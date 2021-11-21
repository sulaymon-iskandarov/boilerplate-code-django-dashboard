from django import forms

from apps.home.models import Data


class TransactionForm(forms.ModelForm):
    type = forms.CharField(disabled=True)

    name = forms.CharField(label="Name", widget=forms.TextInput(attrs={'class': 'form-control transaction'}))

    ts = forms.DateField(label="Timestamp", widget=forms.DateInput(
        attrs={'class': 'form-control datepicker_input transaction', 'placeholder': 'yyyy-mm-dd'}))

    value = forms.DecimalField(label="Total", max_digits=10, decimal_places=2,
                               widget=forms.TextInput(
                                   attrs={'class': 'form-control transaction', 'placeholder': '...'}))

    class Meta:
        model = Data
        fields = ['type', 'name', 'ts', 'value']
