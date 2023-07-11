from rest_framework import permissions
from orders.models import Order


class IsOwnerOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.user == request.user


class IsOwnerOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return request.method in permissions.SAFE_METHODS or obj.user == request.user


class IsProductOwner(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.product.user == request.user


class IsStaffPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method == "GET":
            return request.user
        elif request.method == "POST":
            return request.user.is_authenticated and request.user.is_staff
        return False
