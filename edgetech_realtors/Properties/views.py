from django.shortcuts import render
from django.http import HttpResponse
from .models import Property
# Create your views here.
def home(request):
    properties = Property.objects.all()
    return render(request,'home.html', {'properties': properties})
