from rest_framework.filters import OrderingFilter, SearchFilter
from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import CreateModelMixin,\
                                    ListModelMixin, \
                                    RetrieveModelMixin,\
                                    UpdateModelMixin

from django_filters.rest_framework import DjangoFilterBackend
from .models import Installation, Status
from .serializers import CreateInstallationSerializer, \
                        InstallationSerializer, \
                        UpdateStatusSerializer


class InstallationViewSet(CreateModelMixin, ListModelMixin,
                            RetrieveModelMixin, UpdateModelMixin, GenericViewSet):
    http_method_names = ['get','post', 'patch', 'delete']


    queryset = Installation.objects.prefetch_related('status').all()
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['status']
    search_fields = ['customer_name', 'address']
    ordering_fields = ['appointment_date']

    # def get_queryset(self):

    #     queryset = Installation.objects.all()


    #     current_status = self.request.query_params.get('current_status')
    #     if current_status is not None:
    #         queryset = Installation.objects.filter(current_status=current_status)

    #     return queryset

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




