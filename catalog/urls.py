from django.urls import path

from catalog.apps import CatalogConfig
from catalog.views import hello, contacts

app_name = CatalogConfig.name

urlpatterns = [
    path('', hello, name='index'),
    path('contacts/', contacts, name='contacts')
]