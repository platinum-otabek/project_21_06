from rest_framework import permissions


class IsOwnerPermission(permissions.BasePermission):
    # def has_permission(self, request, view):
    #     return request.user and request.user.is_authenticated

    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to any request,
        # so we'll always allow GET, HEAD or OPTIONS requests.
        print(obj.author.user==request.user)


        # Instance must have an attribute named `owner`.
        return obj.author.user == request.user