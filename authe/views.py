from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.views.generic.base import TemplateView
from .forms import MyUserCreationForm
from django.urls import reverse_lazy
from django.contrib.auth import views

# Create your views here.

class NotFound(TemplateView):
    template_name = "authe/404_not_found.html"
    pass

class UserCreate(CreateView):
    success_url= reverse_lazy('authe:login')
    form_class = MyUserCreationForm
    template_name = 'registration/signup.html'
    pass


class UserChangePassword(views.PasswordChangeView):
    template_name = 'registration/password_change.html'
    success_url = reverse_lazy('authe:chpwddone')
    pass


class UserResetPassword(views.PasswordResetView):
    template_name = 'registration/password_reset.html'
    success_url = reverse_lazy('authe:pwdresetdone')
    email_template_name = 'registration/password_send_email.html'
    html_email_template_name = 'registration/password_send_email.html'
    pass


class UserResetConfirm(views.PasswordResetConfirmView):
    template_name = 'registration/password_reset_confirm.html'
    success_url = reverse_lazy('authe:pwdresetcomp')
    pass
