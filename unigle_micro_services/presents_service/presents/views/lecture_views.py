from rest_framework.permissions import SAFE_METHODS
from rest_framework.viewsets import ModelViewSet

from presents_service.auth_utils import IsAuthenticated, IsAdminUser
from presents.models import Lecture
from presents.serializers import LectureSerializer


class LectureViewSet(ModelViewSet):
    queryset = Lecture.objects.all()
    serializer_class = LectureSerializer
    search_fields = ['name']

    def get_permissions(self):
        if self.request.method in SAFE_METHODS:
            self.permission_classes = [IsAuthenticated]
        else:
            self.permission_classes = [IsAdminUser]
        return super(LectureViewSet, self).get_permissions()
