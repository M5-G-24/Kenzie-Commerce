from rest_framework import permissions
from rest_framework.views import Request, View


class IsObjectOwner(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if obj.username == request.user.username:
            return True
        return False
