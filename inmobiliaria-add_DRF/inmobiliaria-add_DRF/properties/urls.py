

from django.urls import path, include
from .views import PropertyView
from django.contrib.auth.forms import UserCreationForm
from users import views
from accounts import views
from . import views

urlpatterns = [
    #path('base/', views.base, name='home'),
    path('form/', PropertyView, name="form-property"),
    path('login/', views.user_login, name='login'),
    path('signup/', views.user_signup, name='signup'),
    path('logout/', views.user_logout, name='logout'),
    #path('propiedades/', views.base, name='base'),
]