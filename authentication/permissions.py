from rest_framework.permissions import BasePermission


class IsStaff(BasePermission):
    """
    Allows access only administrators.
    """

    def has_permission(self, request, view):
        return bool(request.user and request.user.is_staff is True)


class IsAdmin(BasePermission):
    """
    Allows access only administrators.
    """

    def has_permission(self, request, view):
        return bool(request.user and request.user.admin is True)


class IsSuperUser(BasePermission):
    """
    Allows access only administrators.
    """

    def has_permission(self, request, view):
        return bool(request.user and request.user.is_superuser is True)
