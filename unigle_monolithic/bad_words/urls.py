from rest_framework.routers import DefaultRouter

from bad_words.views.admin_views import BadWordAdminViewSet

router = DefaultRouter()

router.register('admin/bad_words', BadWordAdminViewSet, basename='admin_bad_word')

urlpatterns = [

] + router.urls
