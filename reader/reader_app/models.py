from django.db import models
from django.db.models import Model

class Document(Model):
    def __init__(self, text):
        self.text = text
        self.words = text.split()

        # (start, end) tuples indicating word index ranges
        # that constitute a highlighted annotation
        self.annotations = set()
