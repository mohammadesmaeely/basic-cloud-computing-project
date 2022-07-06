from rest_framework import serializers
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from users.models import User


class GetUserIdView(APIView):
    class UserMicroProfile(serializers.ModelSerializer):
        class Meta:
            model = User
            fields = ['id', 'username', 'is_admin']
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):

        return Response(self.UserMicroProfile(request.user).data)
