from django.urls import path
from . import views


#note the syntax for 3.0.6
urlpatterns = [
  path('welcome/',views.welcome, name='welcome'),
  path('today/',views.news_of_day, name='newsToday'),
  path('archives/<past_date>',views.past_days_news, name = 'pastNews')
]