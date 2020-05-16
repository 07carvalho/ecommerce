from django.utils.translation import ugettext_lazy as _
from rest_framework import generics, serializers, status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Cart, CartItem
from .serializers import CartSerializer, CartItemSerializer
from .permissions import IsOwner, IsOwnerCart


class CartDetail(APIView):
    """Get a cart."""
    description = 'This route is used to get a single cart.'
    serializer_class = CartSerializer
    permission_classes = (IsOwner,)

    def get_object(self, owner):
        try:
            return Cart.objects.get(owner=owner)
        except Cart.DoesNotExist as e:
            raise serializers.ValidationError({'not_found': _('You has no cart.')})

    def get(self, request):
        cart = self.get_object(request.user)
        serializer = CartSerializer(cart)
        return Response(serializer.data)


class CartItemCreate(generics.CreateAPIView, generics.DestroyAPIView):

    description = 'This route is used to insert a product from user`s cart or clear the cart.'
    serializer_class = CartItemSerializer
    permission_classes = (IsOwnerCart,)
    queryset = CartItem.objects.all()

    def get_object(self):
        try:
            obj = Cart.objects.get(owner=self.request.user)
            self.check_object_permissions(self.request, obj)
            return obj
        except Cart.DoesNotExist as e:
            raise serializers.ValidationError({'not_found': _('This product does not exist.')})

    def get_serializer_context(self):
        return {'request': self.request}

    def post(self, request, format=None):
        self.get_object()
        serializer = CartItemSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, *args, **kwargs):
        cart = self.get_object()
        cart.cartitem_set.all().delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class CartItemDetail(generics.DestroyAPIView):

    description = 'This route is used to remove a single product from user`s cart.'
    serializer_class = CartItemSerializer
    permission_classes = (IsOwnerCart,)
    queryset = CartItem.objects.all()

    def get_object(self):
        try:
            obj = Cart.objects.get(owner=self.request.user, )
            self.check_object_permissions(self.request, obj)
            return obj
        except Cart.DoesNotExist as e:
            raise serializers.ValidationError({'not_found': _('This product does not exist.')})

    def delete(self, request, pk=None, format=None):
        cart = self.get_object()
        try:
            cart.cartitem_set.get(pk=pk).delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except CartItem.DoesNotExist:
            raise serializers.ValidationError({'not_found': _('This item does not exist.')})
