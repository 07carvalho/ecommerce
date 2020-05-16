from rest_framework import serializers
from .models import Product


class ProductSerializer(serializers.ModelSerializer):

    created_at = serializers.DateTimeField(format="%d/%m/%Y %H:%M:%S", read_only=True)
    updated_at = serializers.DateTimeField(format="%d/%m/%Y %H:%M:%S", read_only=True)
    slug = serializers.SlugField(read_only=True)

    class Meta:
        model = Product
        fields = '__all__'
