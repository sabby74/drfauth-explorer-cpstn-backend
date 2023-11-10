from rest_framework import generics
from .models import Shops, Review
from .serializers import ShopsSerializer, ReviewSerializer
from rest_framework import permissions
from shops.permissions import IsOwnerOrReadOnly

# Create your views here.

class ShopList(generics.ListCreateAPIView):
    queryset = Shops.objects.all()
    serializer_class = ShopsSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
       serializer.save(owner=self.request.user)

class ShopDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Shops.objects.all()
    serializer_class = ShopsSerializer
    permission_classes = [IsOwnerOrReadOnly]

class ReviewList(generics.ListCreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
       serializer.save(owner=self.request.user)

class ReviewDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [IsOwnerOrReadOnly]