from rest_framework import status
from rest_framework.decorators import action
from rest_framework.mixins import RetrieveModelMixin, UpdateModelMixin
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet, ModelViewSet

from ..filters import UserAdminFilter
from ..models import User
from ..serialziers import ProfileSerializer, AdminUserSerializer


class ProfileView(RetrieveModelMixin, UpdateModelMixin, GenericViewSet):
    serializer_class = ProfileSerializer
    permission_classes = [IsAuthenticated]
    queryset = User.objects.none()

    def get_object(self):
        return self.request.user


class AdminUserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = AdminUserSerializer
    permission_classes = [IsAdminUser]
    filterset_class = UserAdminFilter
    search_fields = ['username', 'phone_number', 'name']

    @action(detail=True, methods=['post'])
    def activate(self, request, pk):
        user = self.get_object()
        user.is_active = True
        user.save()
        return Response(self.get_serializer(user).data, status=status.HTTP_200_OK)

    @action(detail=True, methods=['post'])
    def deactivate(self, request, pk):
        user = self.get_object()
        user.is_active = False
        user.save()
        return Response(self.get_serializer(user).data, status=status.HTTP_200_OK)
