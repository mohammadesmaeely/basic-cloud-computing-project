from django_filters import FilterSet

from assessments.models import Assessment


class AssessmentPublicFilters(FilterSet):
    class Meta:
        model = Assessment
        fields = ['registrar', 'present', 'present__teacher', 'present__lecture']
