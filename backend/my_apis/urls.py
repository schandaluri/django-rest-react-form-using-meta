"""my_apis URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path, include, re_path
from django.conf import settings
from common.views import handler_404, home

handler500 = "rest_framework.exceptions.server_error"

handler400 = "rest_framework.exceptions.bad_request"

urlpatterns = [
    path("", home),
    path("admin/", admin.site.urls),
    path("api/", include("common.urls")),
]

if not settings.DEBUG:
    urlpatterns.append(re_path(r".*", handler_404))
