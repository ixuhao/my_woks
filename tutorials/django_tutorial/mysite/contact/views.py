# coding: utf-8
# Last modified: 2014 Jul 22 02:10:42 PM
# xh

from django.core.mail import send_mail
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response

def contact(request):
    errors = []
    if request.method == 'POST':
        if not request.POST.get('subject', ''):
            errors.append('Enter a subject.')
        if not request.POST.get('message', ''):
            errors.append('Enter a message.')
        if request.POST.get('email') and '@' not in request.POST['email']:
            errors.append('Enter a valid email address.')
        if not errors:
            send_mail(
                    request.POST['suject'],
                    request.POST['message'],
                    request.POST.get(['email'], 'noreply@example.com'),
                    ['siteowner@example.com',],
                    )
            return HttpResponseRedirect('/contact/thanks/')

    return render_to_response('contact_form.html', {'errors': errors})

