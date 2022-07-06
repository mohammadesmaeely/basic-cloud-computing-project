from django.utils.translation import gettext_lazy as _
from rest_framework import serializers

from assessments.models import Assessment
# from bad_words.models import BadWord


class AssessmentPublicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Assessment
        fields = '__all__'
        read_only_fields = ['registrar']

    # def validate_comment(self, value: str):
    #     all_bad_words = BadWord.objects.all().values_list('word', flat=True)
    #     for word in all_bad_words:
    #         if value.__contains__(word):
    #             raise serializers.ValidationError(_("please be polite"))
