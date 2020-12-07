from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsOwner(BasePermission):
    """
        Allows access only to objects owners.
    """

    def has_object_permission(self, request, view, obj):
        return bool(
            request.user and
            request.user.is_authenticated and
            request.user == obj.owner
        )


class IsAuthenticatedAndReadOnly(BasePermission):
    """
        Allows read-only access for authenticated user.
    """

    def has_permission(self, request, view):
        return bool(
            request.user and request.method in SAFE_METHODS
        )
