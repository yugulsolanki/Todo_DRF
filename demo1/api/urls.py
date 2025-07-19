from django.contrib import admin
from django.urls import path
from .views import *
from . import views

urlpatterns = [
    #REST API Endpoints
    path('todos/', TodoListCreateAPIView.as_view(), name='todo-list-create-api'),
    path('todos/<int:pk>/', TodoDetailAPIView.as_view(), name='todo-detail-api'),
    path('todos/update/<int:pk>/', TodoUpdateAPIView.as_view(), name='todo-update-api'),
    path('todos/delete/<int:pk>/', TodoDeleteAPIView.as_view(), name='todo-delete-api'),

    # from from data
    # HTML Views with Forms
    path('', TodoListView.as_view(), name='todo-list-html'),
    path('create/', TodoCreateView.as_view(), name='todo-create-html'),
    path('<int:pk>/', TodoDetailView.as_view(), name='todo-detail-html'),
    path('<int:pk>/edit/', TodoUpdateView.as_view(), name='todo-update-html'),
    path('<int:pk>/delete/', TodoDeleteView.as_view(), name='todo-delete-html'),

]