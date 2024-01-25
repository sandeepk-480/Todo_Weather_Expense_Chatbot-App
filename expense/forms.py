from django import forms 
from expense.models import Expense

class ExpenseForm(forms.ModelForm):
    # amount = forms.DecimalField(required=True)
    # description = forms.CharField(required=True)
    
    class Meta:
        model = Expense
        fields = ['amount', 'category', 'description']

        # Applying Bootstrap classes
        widgets = {
            'amount': forms.NumberInput(attrs={'class': 'form-control', 'id': 'amountid'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'id': 'descriptionid', 'rows': 4, 'cols':20}),
            'category': forms.Select(attrs={'class': 'form-control', 'id': 'categoryid'}),
        }