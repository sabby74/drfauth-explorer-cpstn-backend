from rest_framework import generics
from rest_framework import permissions
from shops.permissions import IsOwnerOrReadOnly
from .models import Shops, Review
from .serializers import ShopsSerializer, ReviewSerializer

class ShopList(generics.ListCreateAPIView):
    queryset = Shops.objects.all()
    serializer_class = ShopsSerializer
    permission_classes = [permissions.AllowAny]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    def get_queryset(self):
        queryset = Shops.objects.all()
        return queryset.prefetch_related('reviews')  # Use prefetch_related to get related reviews efficiently

class ShopDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Shops.objects.all()
    serializer_class = ShopsSerializer
    permission_classes = [permissions.AllowAny]

    def get_queryset(self):
        queryset = Shops.objects.all()
        return queryset.prefetch_related('reviews')  # Use prefetch_related to get related reviews efficiently

class ReviewList(generics.ListCreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [permissions.AllowAny]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class ReviewDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [permissions.AllowAny]
