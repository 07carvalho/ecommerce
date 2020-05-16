from rest_framework import permissions


class IsAdminOrReadOnly(permissions.BasePermission):
    """Object-level permission to only allow admins to edit it
    """

    def has_permission(self, request, view):
        # Read permissions are allowed to any request,
        # so we'll always allow GET, HEAD or OPTIONS requests.
        if request.method in permissions.SAFE_METHODS:
            return True

        # Instance must have an attribute named `owner`.
        return request.user and request.user.is_staff
