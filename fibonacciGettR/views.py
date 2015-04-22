import models
# import forms
from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.core.context_processors import csrf
from django.core import serializers
from django.template import Context, Template
from django.contrib.auth.models import User
from django.utils.html import escape
from django.db.models.loading import get_model
from django.http import QueryDict


def test(request):
	return HttpResponse("Hello W0rld 2")