import datetime
from django.db import models
from django.utils import timezone
from django.db import connection
from django.db import models
from django.conf import settings
from django import forms

POST_STATUS = (
   ('Pub', 'Public'),
   ('Pri', 'Private')
)

class Post(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    category = models.BooleanField(default=True)
    comment_count = models.IntegerField()
    email = models.EmailField(max_length=100)
    post_status = models.CharField(choices=POST_STATUS, max_length=128)
    created_date = models.DateField()

    

