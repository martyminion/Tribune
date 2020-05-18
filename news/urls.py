from django.urls import path
from . import views


#note the syntax for 3.0.6
urlpatterns = [
  path('welcome/',views.welcome, name='welcome'),
]