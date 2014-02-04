#coding: utf-8
from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.template import loader, Context


def home(request):

    return render_to_response('index.html')