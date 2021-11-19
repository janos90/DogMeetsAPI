from rest_framework import permissions


class IsOwnerOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to any request,
        # so we'll always allow GET, HEAD or OPTIONS requests.

        if request.method in permissions.SAFE_METHODS:
            return True

        # Write AND Delete permissions are only allowed to the owner of the object.
        return obj.owner == request.user


class IsOwner(permissions.BasePermission):
    message = 'you are not an owner'

    def has_permission(self, request, view):
        user_groups = request.user.groups.values_list('name', flat=True)
        if "owner" in user_groups:
            return True
        return False
