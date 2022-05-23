
from rest_framework_nested import routers

from . import views
from pprint import pprint

router = routers.DefaultRouter()

router.register('installation', views.InstallationViewSet, basename='installation')
# router.register('status', views.StatusViewSet)
pprint(router.urls)

installation_router = routers.NestedDefaultRouter(router, 'installation', lookup='installation')
installation_router.register('status', views.StatusViewSet, basename='installation-status')

urlpatterns = router.urls + installation_router.urls
