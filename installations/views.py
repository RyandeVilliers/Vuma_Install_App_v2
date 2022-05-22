import re
from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import CreateModelMixin,\
                                    ListModelMixin, \
                                    RetrieveModelMixin,\
                                    UpdateModelMixin

from .models import Installation, Status
from .serializers import CreateInstallationSerializer, \
                        InstallationSerializer, \
                        UpdateStatusSerializer


class InstallationViewSet(CreateModelMixin, ListModelMixin,
                            RetrieveModelMixin, UpdateModelMixin, GenericViewSet):
    http_method_names = ['get','post', 'patch', 'delete']


    queryset = Installation.objects.prefetch_related('status').all()
    serializer_class = InstallationSerializer

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return CreateInstallationSerializer
        return InstallationSerializer


class StatusViewSet(CreateModelMixin, RetrieveModelMixin, UpdateModelMixin, GenericViewSet):
    
    serializer_class = UpdateStatusSerializer

    def get_queryset(self):
        return Status.objects.filter(installation_id=self.kwargs['installation_pk'])

    def get_serializer_context(self):
        return {'installation_id': self.kwargs['installation_pk']}




