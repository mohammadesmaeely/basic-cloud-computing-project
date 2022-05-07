from rest_framework.permissions import SAFE_METHODS, IsAuthenticated, IsAdminUser
from rest_framework.viewsets import ModelViewSet

from bad_words.models import BadWord
from bad_words.serializers import BadWordSerializer


class BadWordAdminViewSet(ModelViewSet):
    permission_classes = [IsAdminUser]
    queryset = BadWord.objects.all()
    serializer_class = BadWordSerializer
