from properties.models import Property
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from .forms import RegisterForm
from django.contrib.auth.forms import UserCreationForm

def first_view(request):
    if request.user.is_authenticated:
        properties = Property.objects.exclude(owner=request.user)
    else:
        properties = Property.objects.all()
    context = {
        "properties": properties
    }
    return render(request, "base.html", context=context)

from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from .forms import LoginForm, RegisterForm

def sign_up(request):
    if request.method == 'GET':
        form = RegisterForm()
        return render(request, 'registro.html', { 'form': form})
    

    
#SCRAPING
from django.shortcuts import render
from lxml import html
import requests

def scraping_view(request):
    # Realizar la solicitud a la página web
    page = requests.get('https://webscraper.io/test-sites/e-commerce/allinone')
    
    # Parsear el contenido de la página
    tree = html.fromstring(page.content)
    
    # Obtener elementos utilizando XPath
    buyers = tree.xpath('//div[@class="col-sm-4 col-lg-4 col-md-4"]/div/div[1]/h4[1]/text()')
    
    # Imprimir los datos obtenidos
    print(buyers)
    
    # Renderizar la respuesta
    return render(request, 'scraped_data.html', {'buyers': buyers})

