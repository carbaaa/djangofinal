"""django_base URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django import views
from django.contrib import admin
from django.urls import path, include
from django_base.views import index,login_view,logout_view,register_view,modal, change_password
from django.conf import settings
from django.conf.urls.static import static
#from django.conf.urls import url
from django.urls import include, re_path



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name = 'index'),
    path('paginas/', include('paginas.urls')),
    path('perfiles/', include('perfiles.urls')),
    path('login/',login_view,name = 'login'),
    path('modal/',modal,name = 'modal'),
    path('logout/',logout_view,name = 'logout_view'),
    path('register/',register_view,name = 'register'),
    path('login/change_password/', change_password, name='change_password'),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)