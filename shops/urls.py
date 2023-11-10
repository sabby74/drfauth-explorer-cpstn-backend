# URLS

from django.urls import path
from .views import ShopList, ShopDetail, ReviewList, ReviewDetail

urlpatterns = [
    path('shops/', ShopList.as_view(), name='shop-list'),
    path('shops/<int:pk>/', ShopDetail.as_view(), name='shop-detail'),
    path('reviews/', ReviewList.as_view(), name='review-list'),
    path('reviews/<int:pk>/', ReviewDetail.as_view(), name='review-detail'),
]