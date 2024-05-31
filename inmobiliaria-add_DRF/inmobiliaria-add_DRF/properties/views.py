from django.shortcuts import render
from .forms import PropertyForm
from .models import Property
from properties.models import Property
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout 
from .forms import SignupForm, LoginForm

# Create your views here.


def PropertyView(request):
    if request.method == "POST":
        form = PropertyForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        properties = Property.objects.all()
        context = {
            "properties": properties,
            "form": form
        }
        return render(request,"properties/property_list.html", context=context)
    else:
        form = PropertyForm()
        context = {
            "form": form
        }
        return render(request, "properties/property_form.html",context=context)
    
    
# Create your views here.
# Home page
def base(request):
    return render(request, 'base.html')

# signup page
def user_signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = SignupForm()
    return render(request, 'signup.html', {'form': form})

# login page
def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)    
                return redirect('home')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})

# logout page
def user_logout(request):
    logout(request)
    return redirect('login')

    