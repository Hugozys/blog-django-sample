from django.urls import reverse
from django.http import HttpResponseRedirect


def redir(request):
    return HttpResponseRedirect(reverse('home:home'))
