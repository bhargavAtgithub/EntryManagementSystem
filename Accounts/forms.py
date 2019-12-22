from django import forms
from Accounts.models import VisitorProfileInfo, RegisteredVisitorEntry

class VisitorProfileInfoForm(forms.ModelForm):
    password = forms.CharField(widget = forms.PasswordInput())
    class Meta():
        model = VisitorProfileInfo
        fields = ('name', 'email', 'phone', 'address', 'username', 'password')

class RegisteredVisitorEntryForm(forms.ModelForm):
    
    class Meta():
        model = RegisteredVisitorEntry
        fields = ('username','host','check_in_time','check_out_time')

        widgets = {
            'username' : forms.TextInput(attrs = { 'readonly':'True' })
        }
        
class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget = forms.PasswordInput())
