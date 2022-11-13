from django.urls import path
from . import views
# localhost:8000/
### NOT DOING THIS: localhost:8000/cats

urlpatterns = [
  # localhost:8000/
  path('', views.home, name='home'),
  path('about/', views.about ,name='about')
]
