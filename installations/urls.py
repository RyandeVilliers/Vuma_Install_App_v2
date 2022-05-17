from rest_framework_nested import routers

from . import views

router = routers.DefaultRouter()

router.register('installation', views.InstallationViewSet)
router.register('status', views.StatusViewSet)

urlpatterns = router.urls
