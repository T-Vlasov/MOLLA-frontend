from django.urls import path
from myapp.views import index, CHAIRS, profile

urlpatterns = [
    path('index/', index, name='index'),
    path('chairs/', CHAIRS, name='chairs'),
    path('profile/', profile, name='profile')
]
