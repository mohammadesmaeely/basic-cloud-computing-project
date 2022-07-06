from rest_framework.permissions import SAFE_METHODS
from rest_framework.viewsets import ModelViewSet


from assessments_service.auth_utils import IsAuthenticated
from assessments.filters import AssessmentPublicFilters
from assessments.models import Assessment
from assessments.serialziers import AssessmentPublicSerializer


class StudentAssessmentViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Assessment.objects.none()
    serializer_class = AssessmentPublicSerializer
    filterset_class = AssessmentPublicFilters

    def get_queryset(self):
        if self.request.method in SAFE_METHODS:
            return Assessment.objects.all()
        else:
            user = self.request.user
            return Assessment.objects.filter(registrar=user)

    def perform_create(self, serializer):
        registrar = self.request.user
        serializer.save(registrar=registrar)
