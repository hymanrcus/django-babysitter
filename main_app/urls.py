from django.urls import path
from . import views



urlpatterns = [
  # localhost:8000/
  path('', views.home, name='home'),
  path('about/', views.about ,name='about'),
  path('babies/', views.babies_index, name='babies_index'),
  path('babies/<int:baby_id>/', views.babies_detail, name='babies_detail'),
  path('babies/create/', views.BabyCreate.as_view(), name='babies_create'),
  path('babies/<int:pk>/update/', views.BabyUpdate.as_view(), name='babies_update'),
  path('babies/<int:pk>/delete/', views.BabyDelete.as_view(), name='babies_delete'),
  path('babies/<int:baby_id>/add_feeding/', views.add_feeding, name='add_feeding'),
  path('toys/create/', views.ToyCreate.as_view(), name='toys_create'),
  path('toys/<int:pk>/update/', views.ToyUpdate.as_view(), name='toys_update'),
  path('toys/<int:pk>/delete/', views.ToyDelete.as_view(), name='toys_delete'),
  path('babies/<int:baby_id>/assoc_toy/<int:toy_id>/', views.assoc_toy, name="assoc_toy")
]
