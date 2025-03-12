from django.db.models import Count
from product.models import Product,Category,Review
from product.serializers import ProductSerializer,CategorySerializer,ReviewSerializer
from rest_framework.viewsets import ModelViewSet
from django_filters.rest_framework import DjangoFilterBackend
from product.filters import ProductFilter
from rest_framework.filters import SearchFilter,OrderingFilter
from product.paginations import DefaultPagination
from api.permissions import IsAdminOrReadOnly
from product.permissions import IsReviewAuthorOrReadOnly

# Create your views here.

# using ModelViewSets

class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = [DjangoFilterBackend,SearchFilter,OrderingFilter]
    filterset_class = ProductFilter
    search_fields = ['name','description']
    ordering_fields = ['id','price','updated_at']
    pagination_class = DefaultPagination
    permission_classes = [IsAdminOrReadOnly]


class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.annotate(product_count = Count('products')).all()
    serializer_class = CategorySerializer
    permission_classes = [IsAdminOrReadOnly]

class ReviewViewSet(ModelViewSet):
    serializer_class = ReviewSerializer
    permission_classes = [IsReviewAuthorOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def perform_update(self, serializer):
        serializer.save(user=self.request.user)

    def get_queryset(self):
        return Review.objects.filter(product_id=self.kwargs['product_pk'])
    
    def get_serializer_context(self):
        return {'product_id':self.kwargs['product_pk']}
    




"""
For learning purpose
"""


# using function based view

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

# using class based view


# class ViewSpecificProduct(APIView):
#     def get(self,request,pk):
#         products = get_object_or_404(Product,pk=pk)
#         serializer = ProductSerializer(products,context={'request': request})
#         return Response(serializer.data)

#     def put(self,request,pk):
#         products = get_object_or_404(Product,pk=pk)
#         serializer = ProductSerializer(products,data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data)
#     def delete(self,request,pk):
#         products = get_object_or_404(Product,pk=pk)
#         copy_of_product = products
#         products.delete()
#         serializer = ProductSerializer(copy_of_product)
#         return Response(serializer.data,status=status.HTTP_204_NO_CONTENT)

# class ViewProduct(APIView):
#     def get(self,request):
#         products = Product.objects.select_related('category').all()
#         serializer = ProductSerializer(
#         products, many=True,context={'request': request})
#         return Response(serializer.data)
    
#     def post(self,request):
#         serializer = ProductSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data,status=status.HTTP_201_CREATED)


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


# @api_view()
# def view_category(request):
#     categories = Category.objects.annotate(product_count = Count('products')).all()
#     serializer = CategorySerializer(categories,many=True)
#     return Response(serializer.data)

# class ViewCategory(APIView):
#     def get(self,request):
#         categories = Category.objects.annotate(product_count = Count('products')).all()
#         serializer = CategorySerializer(categories,many=True)
#         return Response(serializer.data)
    
#     def post(self,request):
#         serializer = CategorySerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data,status=status.HTTP_201_CREATED)
    

# class ProductList(ListCreateAPIView):
#     # using attributes
#     queryset = Product.objects.select_related('category').all()
#     serializer_class = ProductSerializer

#     # use method for logical things
#     def get_queryset(self):
#         return Product.objects.select_related('category').all()
    
#     def get_serializer_class(self):
#         return ProductSerializer

# @api_view()
# def view_specific_category(request,pk):
#     category = get_object_or_404(Category,pk=pk)
#     serializer = CategorySerializer(category)
#     return Response(serializer.data)


# class ViewSpecificCategory(APIView):
#     def get(self,request,pk):
#         category = get_object_or_404(Category.objects.annotate(product_count = Count('products')).all(),pk=pk)
#         serializer = CategorySerializer(category)
#         return Response(serializer.data)
    
#     def put(self,request,pk):
#         category = get_object_or_404(Category.objects.annotate(product_count = Count('products')).all(),pk=pk)
#         serializer = CategorySerializer(category,data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data)
    
    
#     def delete(self,request,pk):
#         categories = get_object_or_404(Category,pk=pk)
#         categories.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)


# using Generic api view
# class ProductList(ListCreateAPIView):
#     queryset = Product.objects.select_related('category').all()
#     serializer_class = ProductSerializer


# class ProductDetails(RetrieveUpdateDestroyAPIView):
#     queryset = Product.objects.all()
#     serializer_class = ProductSerializer


# class CategoryList(ListCreateAPIView):
#     queryset = Category.objects.annotate(product_count = Count('products')).all()
#     serializer_class = CategorySerializer


# class CategoryDetails(RetrieveUpdateDestroyAPIView):
#     queryset = Category.objects.annotate(product_count = Count('products')).all()
#     serializer_class = CategorySerializer