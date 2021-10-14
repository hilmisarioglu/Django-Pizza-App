from django.urls import path
from .views import pizza_create,home
urlpatterns = [
    path('order/', pizza_create, name='order'),
    path('home/', home, name='home'),

]
