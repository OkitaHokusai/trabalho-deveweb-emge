from django.urls import path
from .views import index, contato, sobre

urlpatterns = [
    path('', index, name='index'),
    path('contato/', contato, name='contato'),
    path('sobre/', sobre, name='sobre'),
]
