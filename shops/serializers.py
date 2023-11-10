from rest_framework import serializers
from .models import Shops, Review



class ShopsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shops
        fields = ('id','name', 'description', 'location', 'sells', 'rating', 'is_OpenSundays', 'created_at', 'updated_at', 'owner', 'reviews')
        read_only_fields = ('created_at', 'updated_at', 'owner')
        owner = serializers.ReadOnlyField(source='owner.username')

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ('id','title', 'shop', 'body', 'owner')
        owner = serializers.ReadOnlyField(source='owner.username')
        shop = serializers.ReadOnlyField(source='shop.name')