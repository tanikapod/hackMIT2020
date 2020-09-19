from django.shortcuts import render
from django.http import HttpResponse
from django.utils.html import escape
from .models import Document
import requests

def home(request):
    return render(request, 'templates/home.html')

def annotate(request):
    document = Document(text=request.GET.get('paragraph_text'))
    return render(request, 'templates/document.html', context={"doc_text":document.text})
