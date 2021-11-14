from django.urls import path
from . import views

app_name = 'lecture'

urlpatterns = [
     path('', views.index,  name="index"),
     path('<int:lecture_id>/', views.detail, name="detail"),
     path('new/', views.new, name="new"),
     path('create/', views.create, name="create"),
     path('<int:lecture_id>/edit/', views.edit, name="edit"),
     path('<int:lecture_id>/update/', views.update, name="update"),
     path('<int:lecture_id>/delete/', views.delete, name="delete"),
     path('<int:lecture_id>/like/', views.like, name="like"),
]