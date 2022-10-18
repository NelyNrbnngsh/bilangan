"""untirta URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path
from asli.views import BilanganAsli
from bulat.views import BilanganBulat
from cacah.views import BilanganCacah
from irrasional.views import BilanganIrrasional
from prima.views import BilanganPrima
from profil.views import Profil
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('asli/', BilanganAsli, name="asli"),
    path('bulat/', BilanganBulat, name="bulat"),
    path('cacah/', BilanganCacah, name="cacah"),
    path('irrasional/', BilanganIrrasional, name="irrasional"),
    path('prima/', BilanganPrima, name="prima"),
    path('profil/', Profil, name="profil"),
    path('', views.index),
]
