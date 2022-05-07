from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from django.utils.translation import ugettext_lazy as _
from rest_framework.validators import UniqueTogetherValidator

from presents.models import Present, University, Teacher, Lecture


class UniversitySerializer(serializers.ModelSerializer):
    class Meta:
        model = University
        fields = '__all__'


class LectureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lecture
        fields = '__all__'


class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = '__all__'


class PresentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Present
        fields = '__all__'
