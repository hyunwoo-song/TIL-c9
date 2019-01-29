from django.urls import path
from . import views

urlpatterns = [
    path('new/', views.new),
    path('create/', views.create),
    path('', views.index),
    path('<int:student_id>/', views.detail),
    path('<int:student_id>/delete/', views.delete),
    path('<int:student_id>/edit/', views.edit),
    path('<int:student_id>/update/', views.update),
]