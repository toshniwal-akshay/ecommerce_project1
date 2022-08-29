"Custom Import"
from django import forms
from allauth.account.forms import SignupForm
MALE = 1
FEMALE = 2
OTHER = 3

GENDER_CHOICE = (
    (MALE, 'Male'),
    (FEMALE, 'Female'),
    (OTHER, 'Other'),

)


class UserSignupForm(SignupForm):
    "User Signup Form Extended from allauth SignUp form"
    name = forms.CharField(max_length=25, label='Full Name')
    date_of_birth = forms.DateField(label="Date of Birth")
    address = forms.CharField(max_length=100, label="Address")
    gender = forms.ChoiceField(choices=GENDER_CHOICE)

    def save(self, request):
        user = super(UserSignupForm, self).save(request)

        user.name = self.cleaned_data['name']
        user.dob = self.cleaned_data['date_of_birth']
        user.address = self.cleaned_data['address']
        user.gender = self.cleaned_data['gender']
        user.set_password(self.cleaned_data['password1'])
        
        user.save()
        
        return user


class ShopSignupForm(SignupForm):
    "Shop Signup Form Extended from allauth SignUp form"
    name = forms.CharField(max_length=25, label='Full Name')
    date_of_birth = forms.DateField(label="Date of Birth")
    address = forms.CharField(max_length=100, label="Address")
    gender = forms.ChoiceField(choices=GENDER_CHOICE)
    shop_name = forms.CharField(max_length=100, label="Shop Name")

    def save(self, request):
        user = super(ShopSignupForm, self).save(request)
        
        user.name = self.cleaned_data['name']
        user.dob = self.cleaned_data['date_of_birth']
        user.address = self.cleaned_data['address']
        user.gender = self.cleaned_data['gender']
        user.shop_name = self.cleaned_data['shop_name']
        user.shop = True
        user.set_password(self.cleaned_data['password1'])
        
        user.save()

        return user
