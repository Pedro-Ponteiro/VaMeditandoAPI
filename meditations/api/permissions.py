from rest_framework import permissions


class IsAuthenticatedAndOwner(permissions.IsAuthenticated):
    def has_object_permission(self, request, view, obj):
        is_auth = super().has_object_permission(request, view, obj)
        return is_auth and request.user == obj.user


class IsAdminOrReadOnly(permissions.IsAdminUser):
    def has_permission(self, request, view):
        is_admin = super().has_permission(request, view)

        return request.method in permissions.SAFE_METHODS or is_admin
