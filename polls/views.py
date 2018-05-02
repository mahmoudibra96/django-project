# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
import datetime
from django.shortcuts import render

def current_datetime(request):
    now = datetime.datetime.now()
    html = "<html><body>It is now %s.</body></html>" % now
    return HttpResponse(html)


def home (request):
    now= datetime.datetime.now()
    context = {'date_time':now}
    return render(request,'home.html',context)