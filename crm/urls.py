from django.urls import path

from . import views

app_name = 'crm'

urlpatterns = [
    path('', views.client_list, name='client_list'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('clients/new/', views.client_create, name='client_create'),
    path('clients/<int:pk>/edit/', views.client_update, name='client_update'),
    path('clients/<int:pk>/delete/', views.client_delete, name='client_delete'),
]
