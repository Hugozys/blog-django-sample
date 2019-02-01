from django.contrib.auth.models import User
from django import forms
from django.forms import EmailField
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.forms import UserCreationForm
from django.contrib.sites.shortcuts import get_current_site

class MyUserCreationForm(UserCreationForm):
    email = EmailField(label=_("Email address"), required=True, 
        help_text=_("Required."))
    
    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")
        pass
    
    def __init__(self, *args, **kwargs):
        super(UserCreationForm, self).__init__(*args, **kwargs)
        for field in iter(self.fields):
            if (field == "password1"):
                self.fields[field].widget.attrs.update({
                    'class': 'form-control',
                    'placeholder': 'password',
                })
            elif (field == "password2"):
                self.fields[field].widget.attrs.update({
                    'class': 'form-control',
                    'placeholder': 'confirm password',
                })
            else:
                self.fields[field].widget.attrs.update({
                'class': 'form-control',
                'placeholder': field,
                })
            pass
        pass
    
    def clean(self):
        cleaned_data = super().clean()
        new_email = cleaned_data.get("email")
        new_user = cleaned_data.get("username")
        if (User.objects.filter(email=new_email).exclude(username=new_user).exists()):
            raise forms.ValidationError(u'Email addresses must be unique')
            pass
        return cleaned_data
    
    def save(self, commit=True):
        user = super(UserCreationForm, self).save(commit=False)
        new_email = self.cleaned_data["email"]
        user.email = new_email
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user
