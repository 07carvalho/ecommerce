from django.utils.translation import ugettext_lazy as _
from rest_framework import generics, filters, serializers, status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Product
from .serializers import ProductSerializer
# from authapi.filters import IsAdminOrListOnlyVisibleFilterBackend
from authapi.permissions import IsAdminOrReadOnly


class ProductList(generics.ListCreateAPIView):

    description = 'This route is used to list or create a new product.'
    queryset = Product.objects.filter(visible=True)
    serializer_class = ProductSerializer
    permission_classes = (IsAdminOrReadOnly,)
    # filter_backends = [IsAdminOrListOnlyVisibleFilterBackend]
    # search_fields = ['title',]
    # ordering_fields = ['created_at', 'title', 'price',]
    ordering = ['-created_at']

    # def get_queryset(self):
    #     if 
    #     queryset = Product.objects.all()

    #     # filter_field = self.request.query_params.get('filter', None)
    #     # queryset = Product().filter_queryset(queryset, filter_field)

    #     order_field = self.request.query_params.get('order', None)
    #     queryset = Product().order_queryset(queryset, order_field)

    #     return queryset


    def list(self, request):
        queryset = self.get_queryset()
        serializer = ProductSerializer(queryset, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ProductDetail(APIView):
    """Get a product."""
    description = 'This route is used to get a single product.'
    permission_classes = (IsAdminOrReadOnly,)
    serializer_class = ProductSerializer

    def get_object(self, pk):
        try:
            return Product.objects.get(pk=pk)
        except Product.DoesNotExist as e:
            raise serializers.ValidationError({'not_found': _('This product does not exist.')})

    def get(self, request, pk=None):
        product = self.get_object(pk)
        serailizer = ProductSerializer(product)
        return Response(serailizer.data)

    def put(self, request, pk=None):
        product = self.get_object(pk)
        serializer = ProductSerializer(product, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=200)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk=None):
        product = self.get_object(pk)
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
