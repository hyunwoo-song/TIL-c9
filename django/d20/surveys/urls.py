from django.urls import path
from . import views

app_name = 'surveys'

urlpatterns = [
    path('', views.index, name='list'),
    path('new/', views.new, name='new'),
    path('create/', views.create, name='create'),
    path('<int:question_id>/', views.detail, name='detail'),
    path('<int:question_id>/delete/', views.delete, name='delete'),
    path('<int:question_id>/edit/', views.edit, name='edit'),
    path('<int:question_id>/update/', views.update, name='update'),
    path('<int:question_id>/choices/create/', views.choice_create, name='choice_create'),
    path('<int:question_id>/choices/<int:choice_id>/delete/', views.choice_delete, name='choice_delete'),

]