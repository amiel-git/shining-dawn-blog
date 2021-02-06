from django import forms
from accounts.models import UserProfile, StaffProfile

class UserRegistrationForm(forms.ModelForm):

    class Meta():
        model = UserProfile
        fields = [
            'username',
            'first_name',
            'last_name',
            'email',
            'password'
        ]

        widgets = {
            'password': forms.widgets.TextInput(attrs={'type':'password','class':'form-control'}),
            'username': forms.widgets.TextInput(attrs={'class':'form-control'}),
            'first_name': forms.widgets.TextInput(attrs={'class':'form-control'}),
            'last_name': forms.widgets.TextInput(attrs={'class':'form-control'}),
            'email': forms.widgets.EmailInput(attrs={'class':'form-control'}),
        }

class StaffRegistrationForm(forms.ModelForm):

    class Meta():
        model = StaffProfile
        fields = [
            'username',
            'first_name',
            'last_name',
            'email',
            'password'
        ]

        widgets = {
            'password': forms.widgets.TextInput(attrs={'type':'password','class':'form-control'}),
            'username': forms.widgets.TextInput(attrs={'class':'form-control'}),
            'first_name': forms.widgets.TextInput(attrs={'class':'form-control'}),
            'last_name': forms.widgets.TextInput(attrs={'class':'form-control'}),
            'email': forms.widgets.EmailInput(attrs={'class':'form-control'}),
        }