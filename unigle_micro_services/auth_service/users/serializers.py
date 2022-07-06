from django.utils.translation import ugettext_lazy as _
from rest_framework import serializers

from .models import User


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=False)

    class Meta:
        model = User
        fields = '__all__'
        extra_kwargs = {
            'last_login': {'read_only': True}
        }

    def create(self, validated_data):
        if 'password' not in validated_data:
            raise serializers.ValidationError(_("password is required"))
        user = super().create(validated_data)
        user.set_password({'password': validated_data['password']})
        user.save()
        return user

    def update(self, instance, validated_data):
        user = super().update(instance, validated_data)
        if 'password' in validated_data and validated_data['password'] is not None and validated_data['password'] != "":
            user.set_password(validated_data['password'])
        user.save()
        return user
