from secrets import choice
from .models import CustomUser

from allauth.account.forms import SignupForm
from django import forms

USER_TYPES = [
        ('S','shop'),
        ('C','customer')
    ]
    


class CustomSignupForm(SignupForm):
    first_name = forms.CharField(max_length=25, label='First Name')
    last_name = forms.CharField(max_length=25, label='Last Name')
    date_of_birth = forms.DateField(label="Date of Birth")
    address = forms.CharField(max_length=100,label="Address")
    user_type = forms.CharField(
    max_length=3,
    widget=forms.Select(choices=USER_TYPES ),
    ) 
    
    
    
    def save(self, request):
        user = super(CustomSignupForm, self).save(request)
        
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.date_of_birth = self.cleaned_data['date_of_birth']
        user.address = self.cleaned_data['address']
        user.user_type = self.cleaned_data['user_type']
        user.set_password(self.cleaned_data["password1"])
        user.save()
        return user
