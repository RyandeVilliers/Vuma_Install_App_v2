from django.shortcuts import render

from rest_framework.mixins import CreateModelMixin,\
                                    ListModelMixin, \
                                    RetrieveModelMixin,\
                                    UpdateModelMixin

from .models import Installation, Status
from .serializers import InstallationSerializer, StatusSerializer


class InstallationViewSet(CreateModelMixin, ListModelMixin,
                            RetrieveModelMixin, UpdateModelMixin):

    queryset = Installation.objects.prefetch_related('status').all()
    serializer_class = InstallationSerializer


class StatusViewSet(CreateModelMixin, RetrieveModelMixin, UpdateModelMixin):
    
    queryset = Status.objects.all()
    serializer_class = StatusSerializer
