from django.urls import path
from blackout.views import index

urlpatterns = [
    path('', index, name='index'),
]
