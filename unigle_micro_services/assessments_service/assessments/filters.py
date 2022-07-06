from django_filters import FilterSet

from assessments.models import Assessment


class AssessmentPublicFilters(FilterSet):
    class Meta:
        model = Assessment
        fields = ['id']
