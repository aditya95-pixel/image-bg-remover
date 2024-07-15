from django.urls import path
from .views import home, remback

urlpatterns = [
    path('', home, name='home'),
    path('remback/', remback, name='remback'),
]
