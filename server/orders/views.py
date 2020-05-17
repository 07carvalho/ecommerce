from django.utils.translation import ugettext_lazy as _
from rest_framework import generics, serializers, status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Order
from .serializers import OrderSerializer
# from .permissions import IsOwner, IsOwnerCart


class OrderList(generics.ListCreateAPIView):
    """Get a cart."""
    description = 'This route is used to get a single cart.'
    serializer_class = OrderSerializer
    # permission_classes = (IsOwner,)

    def get_queryset(self):
        return Order.objects.filter(user=self.request.user)

    def post(self, request, *args, **kwargs):
        serializer = OrderSerializer(data=request.data, context={'user': self.request.user})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # def get_object(self, owner):
    #     try:
    #         return Cart.objects.get(owner=owner)
    #     except Cart.DoesNotExist as e:
    #         raise serializers.ValidationError({'not_found': _('You has no cart.')})

    # def get(self, request):
    #     cart = self.get_object(request.user)
    #     serializer = CartSerializer(cart)
    #     return Response(serializer.data)