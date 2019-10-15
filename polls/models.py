import datetime
from django.db import models
from django.utils import timezone
from django.db import connection
from django.db import models
from django.conf import settings
from django import forms

POST_STATUS = (
   ('Pub', 'Public'),
   ('Pri', 'Private'),
   ('pro', 'Protected'),
)

COLOR_CHOICES = (
    ('green','GREEN'),
    ('blue', 'BLUE'),
    ('red','RED'),
    ('orange','ORANGE'),
    ('black','BLACK'),
)

class Post(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    category = models.BooleanField(default=True)
    comment_count = models.IntegerField()
    email = models.EmailField(max_length=100)
    post_status = models.CharField(choices=POST_STATUS, max_length=128)
    color_choices = models.CharField(choices=COLOR_CHOICES, max_length=150)
    created_date = models.DateField()

    def __str__(self):
        return self.title

