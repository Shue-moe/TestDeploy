from django.conf import settings
from django.conf.urls.static import static

from django.contrib import admin
from django.urls import path
from mainApp.views import mainPage


urlpatterns = [
	path('', mainPage, name="mainPage"),
    path('admin/', admin.site.urls),
]