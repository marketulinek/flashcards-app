from django import views
from django.urls import path
from . import views


urlpatterns = [
    path('', views.CardListView.as_view(), name='card_list'),
    path('card/new/', views.CardCreateView.as_view(), name='card_create'),
    path('card/<int:pk>/edit/', views.CardUpdateView.as_view(), name='card_update'),
]