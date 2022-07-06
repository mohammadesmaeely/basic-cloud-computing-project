from rest_framework import serializers

from bad_words.models import BadWord


class BadWordSerializer(serializers.ModelSerializer):
    class Meta:
        model = BadWord
        fields = '__all__'