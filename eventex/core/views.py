#coding: utf-8
from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.template import loader, Context
from django.conf import settings


def home(request):
    context = {'STATIC_URL' : settings.STATIC_URL}
    return render_to_response('index.html', context)