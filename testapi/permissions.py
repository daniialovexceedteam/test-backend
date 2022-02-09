from rest_framework.permissions import BasePermission


class CardPermission(BasePermission):

    def has_object_permission(self, request, view, obj):
        user = request.user
        if not user.is_superuser:
            view.queryset = view.queryset.filter(account__owner=user)
            print(view)
        return True