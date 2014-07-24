# coding: utf-8
# Last modified: 2014 Jul 24 05:11:29 PM
# xh

# csrf http://blog.csdn.net/tr1ue/article/details/20654943

from django.core.context_processors import csrf
from django.core.mail import send_mail
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext
from contact.myforms import ContactForm

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            #send_mail(
            #        cd['subject'],
            #        cd['message'],
            #        cd.get('email', 'noreply@example.com'),
            #        ['siteowner@example.com'],
            #        )
            return HttpResponseRedirect('/contact/thanks/') 
    else:
        form = ContactForm(initial={'subject': 'I love your site!'})
    return render_to_response('contact_form.html', {'form':form}, RequestContext(request))

def thanks(request):
    return render_to_response('thanks.html')
