from django.urls import path
from myapp.views import index, chairs, OortChairs, GgameChairs, OofficeChairs

urlpatterns = [
    path('index/', index, name='index'),
    path('chairs/', chairs, name='chairs'),
    path('officeChairs/', OofficeChairs, name='OfficeChairs'),
    path('gameChairs/', GgameChairs, name='GameChairs'),
    path('ortChairs/', OortChairs, name='OrtChairs'),
]
