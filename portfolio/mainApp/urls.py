from django.conf.urls.static import static
from django.urls import path, include
from .views import Home, About

urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('about/', About.as_view(), name='about'),
]
