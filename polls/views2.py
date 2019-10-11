
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import auth
# from polls.models import Csv_upload
from polls import views
from django import forms
import csv, io
import pandas as pd
import pprint
from django.core.mail import BadHeaderError, send_mail
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.tokens import default_token_generator
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template import loader
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
from django.core.mail import send_mail
from django.contrib import messages
from django.contrib.auth.models import User
from django.db.models.query_utils import Q


