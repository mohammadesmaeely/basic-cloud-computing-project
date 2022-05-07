from rest_framework import serializers

from assessments.models import Assessment


class AssessmentPublicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Assessment
        fields = '__all__'
        read_only_fields = ['registrar']
