"""
URL configuration for inmobiliaria project.

The urlpatterns list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
#from django.contrib.auth.views import LoginView, LogoutView
#from django.contrib.auth import views as auth_views
from users.views import first_view
from django.contrib.auth.forms import UserCreationForm
from users import views
from accounts import views
from users.views import scraping_view


urlpatterns = [

   # path('registro.html/', views.sign_up, name='registro.html'),
    #path('', views.index, name='home'),
    path('scraping/', scraping_view, name='scraping'),
    path('', include('properties.urls')),
    path('admin/', admin.site.urls),
    path('', first_view, name="inicio"),
    path("properties/", include("properties.urls")),
   # path('registro/', views.registrar_usuario, name='registrar_usuario'),
    #path('', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)