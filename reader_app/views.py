from django.shortcuts import render
from django.http import HttpResponse
from .models import Document

def home(request):
    # return HttpResponse("Paste the text you're reading below.")
    render(request, '.reader/templates/home.html')
