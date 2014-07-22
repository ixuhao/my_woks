# coding: utf-8
# Last modified: 2014 Jul 22 03:16:39 PM
# xh

# csrf http://blog.csdn.net/tr1ue/article/details/20654943

from django.core.context_processors import csrf
from django.core.mail import send_mail
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response

def contact(request):
    c = {}
    c.update(csrf(request))
    c['errors'] = []
    if request.method == 'POST':
        if not request.POST.get('subject', ''):
            c['errors'].append('Enter a subject.')
        if not request.POST.get('message', ''):
            c['errors'].append('Enter a message.')
        if request.POST.get('email') and '@' not in request.POST['email']:
            c['errors'].append('Enter a valid email address.')
        if not c['errors']:
            #send_mail(
            #        request.POST['subject'],
            #        request.POST['message'],
            #        request.POST.get('email', 'noreply@example.com'),
            #        ['siteowner@example.com'],
            #        )
            return HttpResponseRedirect('/contact/thanks/')

    c['subject'] = request.POST.get('subject', '')
    c['message'] = request.POST.get('message', '')
    c['email'] = request.POST.get('email', '')
    return render_to_response('contact_form.html', c)

def thanks(request):
    return render_to_response('thanks.html')
