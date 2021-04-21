from django import forms
from .models import Stock

class StockCreateForm(forms.ModelForm):
    export_to_CSV = forms.BooleanField(required=False)
    class Meta:
        model = Stock
        fields = ['category', 'item_name','quantity','measurement_unit','reorder_level']

class IssueForm(forms.ModelForm):
    class Meta:
        model = Stock
        fields = ['issue_quantity', 'issue_to']


class ReceiveForm(forms.ModelForm):
    class Meta:
        model = Stock
        fields = ['receive_quantity', 'receive_by']

class ReorderLevelForm(forms.ModelForm):
    class Meta:
        model = Stock
        fields = ['reorder_level']


from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm

#
# class UserAdminCreationForm(UserCreationForm):
#     """
#     A Custom form for creating new users.
#     """
#
#     class Meta:
#         model = get_user_model()
#         fields = ['phone']