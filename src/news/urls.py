from django.urls import path
from .views import ReviewsAPI, UpdatesAPI, ContactsAPI, CategoryAPI, CartAPI, ColorAPI, CartGetBorderAPI

urlpatterns = [
    path('reviews/', ReviewsAPI.as_view()),
    path('updates/', UpdatesAPI.as_view()),
    path('contacts/', ContactsAPI.as_view()),
    path('categories/', CategoryAPI.as_view()),
    path('cart/border/<int:pk>/', CartGetBorderAPI.as_view()),
    path('cart/', CartAPI.as_view()),
    path('color/<int:pk>/', ColorAPI.as_view()),
]
