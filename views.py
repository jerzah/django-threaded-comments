from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.template import loader
from django.shortcuts import render, get_object_or_404
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from .models import Articles, Comments

# Create your views here.
def index(request):
    return render(request, 'commentApp/index.html')
