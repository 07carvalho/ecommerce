from rest_framework import permissions
from .models import Cart


class IsOwner(permissions.BasePermission):
    """Object-level permission to only owner admins to edit it."""

    def has_object_permission(self, request, view, obj):
        # Instance must have an attribute named `owner`.
        return request.user.is_authenticated and obj.owner == request.user


class IsOwnerCart(permissions.BasePermission):
    """Object-level permission to only owner admins to edit it."""

    def has_permission(self, request, view):
        try:
            Cart.objects.get(owner=request.user)
            return True
        except Cart.DoesNotExist as e:
            return False
