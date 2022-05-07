import django_filters

from .models import User


class UserAdminFilter(django_filters.FilterSet):

    class Meta:
        model = User
        fields = ['is_active', 'is_admin']
