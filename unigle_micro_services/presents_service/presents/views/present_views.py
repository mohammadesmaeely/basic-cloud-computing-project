from rest_framework.permissions import SAFE_METHODS
from rest_framework.viewsets import ModelViewSet

from presents_service.auth_utils import IsAuthenticated, IsAdminUser
from presents.models import Present
from presents.serializers import PresentSerializer


class PresentViewSet(ModelViewSet):
    queryset = Present.objects.all()
    serializer_class = PresentSerializer
    search_fields = ['teacher__name', 'lecture__name', 'university__name']

    def get_permissions(self):
        if self.request.method in SAFE_METHODS:
            self.permission_classes = [IsAuthenticated]
        else:
            self.permission_classes = [IsAdminUser]
        return super(PresentViewSet, self).get_permissions()
