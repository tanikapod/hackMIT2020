from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse("Paste the text you're reading below.")
