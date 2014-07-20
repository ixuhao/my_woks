from django.http import HttpResponse, Http404
from django.shortcuts import render_to_response
import datetime

def hello(request):
    return HttpResponse('Hello world!')


def current_datetime(request):
    now = datetime.datetime.now()
    #return render_to_response('dateapp/current_datetime.html', {'current_date': now}) 
    return render_to_response('current_datetime.html', {'current_date': now}) 

def hours_ahead(request, offset):
    try:
        offset = int(offset)
    except ValueError:
        raise Http404

    dt = datetime.datetime.now() + datetime.timedelta(hours=offset)
    #assert False
    #html = "<html><body>In %s hour(s), it will be now %s.</body></html>" % (offset, dt)
    #return HttpResponse(html)
    return render_to_response('hours_ahead.html', {'hour_offset': offset, 'next_time': dt})

def display_meta(request):
    values = request.META.items()
    values.sort()
    p = request.path
    return render_to_response('display_meta.html', {'mvalues': values,
        'rpath': p})
