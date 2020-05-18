from rest_framework import generics, serializers, status
from rest_framework.response import Response
from .models import Order
from .serializers import OrderSerializer


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
