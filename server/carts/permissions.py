from django.utils.translation import ugettext_lazy as _
from rest_framework import permissions, serializers
from .models import Cart


class IsOwner(permissions.BasePermission):
    """Object-level permission to only owner admins to edit it."""

    def has_object_permission(self, request, view, obj):
        print("OKOKOKOK")
        print(request.user.is_authenticated)
        if request.user.is_authenticated:
            # Instance must have an attribute named `owner`.
            return obj.owner == request.user
        raise serializers.ValidationError({'not_allowed': _('You need to login.')})


class IsOwnerCart(permissions.BasePermission):
    """Object-level permission to only owner admins to edit it."""

    def has_permission(self, request, view):
        try:
            Cart.objects.get(owner=request.user)
            return True
        except Cart.DoesNotExist as e:
            return False
