from django.shortcuts import render
from allauth.account.views import SignupView

from .forms import UserSignupForm, ShopSignupForm


def index(request):
    "Create your views here."
    return render(request, "user/base.html")


class UserSignupView(SignupView):
    "Signup View extended"
    template_name = "user/user_signup.html"

    form_class = UserSignupForm

    def get_context_data(self, **kwargs):
        context = super(UserSignupView, self).get_context_data(**kwargs)
        context.update(self.kwargs)
        userSignUpForm = UserSignupForm(self.request.POST or None)
        context['form'] = userSignUpForm
        return context


class ShopSignupView(SignupView):
    "Signup View extended"
    template_name = "user/shop_signup.html"

    form_class = ShopSignupForm

    def get_context_data(self, **kwargs):
        context = super(ShopSignupView, self).get_context_data(**kwargs)
        shopSignUpForm = ShopSignupForm(self.request.POST or None)
        context['form'] = shopSignUpForm
        return context

    
        


user_signup_view = UserSignupView.as_view()

shop_signup_view = ShopSignupView.as_view()
