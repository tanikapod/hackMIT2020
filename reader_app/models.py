from django.db import models
from django.db.models import Model

class Document(Model):
    text_box = models.TextField()
