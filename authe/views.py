from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.views.generic.base import TemplateView
from .forms import MyUserCreationForm
from django.urls import reverse_lazy
from django.contrib.auth import views
from django.contrib.auth.models import User
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from .tokens import account_activation_token
from django.core.mail import send_mail
from django.contrib.sites.shortcuts import get_current_site
# Create your views here.

class NotFound(TemplateView):
    template_name = "authe/404_not_found.html"
    pass



def activate(request,uidb64,token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user,token):
        user.is_active = True
        user.save()
        return render(request, 'registration/signup_confirm_success.html')
    else:
        return render(request, 'registration/signup_confirm_failure.html')

    
def signup_confirm(request):
    return render(request, 'registration/signup_confirm.html')


class UserCreate(CreateView):
    success_url= reverse_lazy('authe:signup_confirm')
    form_class = MyUserCreationForm
    template_name = 'registration/signup.html'
    def send_email(self,receiver,request):        
        mail_subject = 'Activate your blog account.'
        current_site = get_current_site(request)
        context_object = {'user':receiver,
                          'domain': current_site.domain,
                          'protocol': request.is_secure() and "https" or "http",
                          'uid':urlsafe_base64_encode(force_bytes(receiver.pk)).decode(),
                          'token':account_activation_token.make_token(receiver),
        }
        plainmessage = render_to_string('registration/signup_confirmation_email_plain.txt',context_object)
        htmlmessage = render_to_string('registration/signup_confirmation_email.html',context_object)
        to_email = receiver.email
        print("plainmessage:", plainmessage)
        print("htmlmessage:", htmlmessage)
        send_mail(mail_subject, message=plainmessage,from_email="hugoblognoreply@gmail.com",recipient_list=[to_email], fail_silently=False, html_message=htmlmessage)
        return
    
    def post(self, request, *args, **kwargs):
        self.object = None
        form = self.get_form()
        if form.is_valid():
            response = self.form_valid(form)
            user = form.save(commit=False)
            user.is_active = False
            user.save()
            self.send_email(user, request)
            return response
        else:
            return self.form_invalid(form)
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
