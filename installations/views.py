from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import CreateModelMixin,\
                                    ListModelMixin, \
                                    RetrieveModelMixin,\
                                    UpdateModelMixin

from .models import Installation, Status
from .serializers import InstallationSerializer, StatusSerializer


class InstallationViewSet(CreateModelMixin, ListModelMixin,
                            RetrieveModelMixin, UpdateModelMixin, GenericViewSet):

    queryset = Installation.objects.prefetch_related('status').all()
    serializer_class = InstallationSerializer


class StatusViewSet(CreateModelMixin, RetrieveModelMixin, UpdateModelMixin, GenericViewSet):
    
    queryset = Status.objects.all()
    serializer_class = StatusSerializer
