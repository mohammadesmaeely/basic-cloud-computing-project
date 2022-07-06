from rest_framework.routers import DefaultRouter
from assessments.views import student_views

router = DefaultRouter()
router.register('student/assessments', student_views.StudentAssessmentViewSet, basename='_student_assessment')

urlpatterns = [

] + router.urls
