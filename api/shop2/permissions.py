from rest_framework import permissions

class IsAdminProduct(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS: # if request.method in ['PUT', 'PATCH']:
            # Allow read-only access (GET, HEAD, OPTIONS)
            return True
        return request.user and request.user.is_staff

class IsAdminCategory(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user and request.user.is_staff

class IsAdminImage(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user and request.user.is_staff
