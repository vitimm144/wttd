#coding: utf-8
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader, Context


def home(request):

    t = loader.get_template('index.html')
    c = Context()

    content = t.render(c)
    return HttpResponse(content)