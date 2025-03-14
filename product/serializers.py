from rest_framework import serializers
from decimal import Decimal
from product.models import Category,Product,Review,ProductImage
from django.contrib.auth import get_user_model


class CategorySerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Category
        fields = ['id','name','description','product_count']

    product_count = serializers.IntegerField(read_only = True)

    def get_product_count(self, obj):
        return Product.objects.filter(category=obj).count()

class ProductImageSerializer(serializers.ModelSerializer):
    image = serializers.ImageField()
    class Meta:
        model = ProductImage
        fields = ['id','image']

class ProductSerializer(serializers.ModelSerializer):
    images = ProductImageSerializer(many=True,read_only = True)
    class Meta:
        model = Product
        fields = ['id','name','description','price','stock','category','images']

    category = serializers.PrimaryKeyRelatedField(
        queryset = Category.objects.all()
    )

    def validate_price(self,price):
        if price < 0:
            raise serializers.ValidationError('Price could not be Negative')
        return price
    
class SimpleUserSerializer(serializers.ModelSerializer):
    name = serializers.SerializerMethodField(method_name='get_current_user_name')
    class Meta:
        model = get_user_model()
        fields = ['id','name']

    def get_current_user_name(self,obj):
        return obj.get_full_name()

class ReviewSerializer(serializers.ModelSerializer):
    user = SimpleUserSerializer(read_only=True)
    class Meta:
        model = Review
        fields = ['id','user','product','ratings','comment']
        read_only_fields = ['user','product']
    
    def create(self, validated_data):
        product_id = self.context['product_id']
        return Review.objects.create(product_id=product_id,**validated_data)

