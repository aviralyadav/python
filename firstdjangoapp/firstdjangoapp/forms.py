from django import forms

class UsersForm(forms.Form):
    name = forms.CharField(label='Name', required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.CharField(label='Email', widget=forms.TextInput(attrs={'class': 'form-control'}))
    subject = forms.CharField(label='Subject', widget=forms.TextInput(attrs={'class': 'form-control'}))
    message = forms.CharField(label='Message', widget=forms.Textarea(attrs={'class': 'form-control'}))