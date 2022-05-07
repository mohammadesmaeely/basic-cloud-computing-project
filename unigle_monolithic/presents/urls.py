from rest_framework.routers import DefaultRouter
from presents.views import lecture_views, present_views, teacher_views, university_views

router = DefaultRouter()
router.register('lectures', lecture_views.LectureViewSet, basename='lecture')
router.register('presents', present_views.PresentViewSet, basename='present')
router.register('teachers', teacher_views.TeacherViewSet, 'teacher')
router.register('universities', university_views.UniversityViewSet, 'university')

urlpatterns = [

] + router.urls
