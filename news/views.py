from django.shortcuts import render
from django.http import HttpResponse
from datetime as dt
# Create your views here.

def welcome(request):

  return HttpResponse('Welcome to the Moringa Tribune')

def 