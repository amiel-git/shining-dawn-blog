from django.shortcuts import render
from accounts.forms import UserRegistrationForm,StaffRegistrationForm
from accounts.models import UserProfile, StaffProfile

from django.urls import reverse
from django.http import HttpResponseRedirect,HttpResponse

"""
uid encoder = urlsafe_base64_encode(force_bytes(user.pk))
django.contrib.auth.token import passwordresettokengenerator = Used for generating token for password reset
passwordresettokengenerator._make_hash_value(self,user,timestamp)
"""


def Index(request):
    return render(request,'core/index.html')


def UserRegistration(request):

    if request.user.is_staff:
        registration_form = StaffRegistrationForm()
        if request.method == 'POST':
            registration_form = StaffRegistrationForm(request.POST)

            if registration_form.is_valid():
                user = registration_form.save()
                user.set_password(user.password)
                user.save()
            
            else:
                return HttpResponse(registration_form.errors)

            return HttpResponseRedirect(reverse('index'))
    
    else:
        registration_form = UserRegistrationForm()

        if request.method == 'POST':
            registration_form = UserRegistrationForm(request.POST)

            if registration_form.is_valid():
                user = registration_form.save()
                user.set_password(user.password)
                user.save()

            else:
                return HttpResponse(registration_form.errors)

            return HttpResponseRedirect(reverse('index'))

    return render(request,'accounts/register.html',context={'form':registration_form})
