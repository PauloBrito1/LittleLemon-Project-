from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('api/menu/', views.MenuItemsView.as_view(), name='menu-items'),
    path('api/menu/<int:pk>/', views.SingleMenuItemView.as_view(), name='single-menu-item'),
]
