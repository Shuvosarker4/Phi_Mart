from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.views import APIView
from django.db.models import Count
from rest_framework.decorators import api_view
from rest_framework.response import Response
from product.models import Product,Category
from product.serializers import ProductSerializer,CategorySerializer
# Create your views here.


# @api_view(['GET', 'POST'])
# def view_products(request):
#     if request.method == 'GET':
#         products = Product.objects.select_related('category').all()
#         serializer = ProductSerializer(
#         products, many=True,context={'request': request})
#         return Response(serializer.data)
#     if request.method == 'POST':
#         serializer = ProductSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data,status=status.HTTP_201_CREATED)

class ViewProduct(APIView):
    def get(self,request):
        products = Product.objects.select_related('category').all()
        serializer = ProductSerializer(
        products, many=True,context={'request': request})
        return Response(serializer.data)
    
    def post(self,request):
        serializer = ProductSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data,status=status.HTTP_201_CREATED)


# @api_view(['GET','PUT','DELETE'])
# def view_specific_product(request,pk):
#     if request.method == 'GET':
#         products = get_object_or_404(Product,pk=pk)
#         serializer = ProductSerializer(products,context={'request': request})
#         return Response(serializer.data)
#     if request.method == 'PUT':
#         products = get_object_or_404(Product,pk=pk)
#         serializer = ProductSerializer(products,data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data)
#     if request.method == 'DELETE':
#         products = get_object_or_404(Product,pk=pk)
#         copy_of_product = products
#         products.delete()
#         serializer = ProductSerializer(copy_of_product)
#         return Response(serializer.data,status=status.HTTP_204_NO_CONTENT)

class ViewSpecificProduct(APIView):
    def get(self,request,pk):
        products = get_object_or_404(Product,pk=pk)
        serializer = ProductSerializer(products,context={'request': request})
        return Response(serializer.data)

    def put(self,request,pk):
        products = get_object_or_404(Product,pk=pk)
        serializer = ProductSerializer(products,data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    def delete(self,request,pk):
        products = get_object_or_404(Product,pk=pk)
        copy_of_product = products
        products.delete()
        serializer = ProductSerializer(copy_of_product)
        return Response(serializer.data,status=status.HTTP_204_NO_CONTENT)

# @api_view()
# def view_category(request):
#     categories = Category.objects.annotate(product_count = Count('products')).all()
#     serializer = CategorySerializer(categories,many=True)
#     return Response(serializer.data)

class ViewCategory(APIView):
    def get(self,request):
        categories = Category.objects.annotate(product_count = Count('products')).all()
        serializer = CategorySerializer(categories,many=True)
        return Response(serializer.data)


# @api_view()
# def view_specific_category(request,pk):
#     category = get_object_or_404(Category,pk=pk)
#     serializer = CategorySerializer(category)
#     return Response(serializer.data)

class ViewSpecificCategory(APIView):
    def get(self,request,pk):
        category = get_object_or_404(Category,pk=pk)
        serializer = CategorySerializer(category)
        return Response(serializer.data)