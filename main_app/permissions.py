from rest_framework.permissions import BasePermission


class IsActiveStaff(BasePermission):
    """Только активные сотрудники должны иметь доступ к API"""
    def has_permission(self, request, view):
        if request.user.is_staff and request.user.is_active:
            return True
        return False
