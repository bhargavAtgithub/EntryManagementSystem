from django import forms
from app.models import Host, VisitorEntry

class HostForm(forms.ModelForm):
    
    class Meta():
        model = Host
        fields = ('name','email','phone','address')


class VisitorEntryForm(forms.ModelForm):

    class Meta():
        model = VisitorEntry
        fields = ('name','email','phone','check_in_time','check_out_time','host')
