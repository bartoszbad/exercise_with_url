"""URL URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path, re_path

from shortening_urls.views import LandingPageView, ShorterUrlView, YourShorterUrlView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', LandingPageView.as_view(), name="landing_page"),
    re_path(r'shorter_url/([0-9a-z]{5}$)', ShorterUrlView.as_view(), name="your_shorter_url"),
    re_path(r'([0-9a-z]{5}$)', YourShorterUrlView.as_view(), name="your_shorter_url"),
]
