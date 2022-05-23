from rest_framework import serializers
from .models import Installation, Status


class StatusSerializer(serializers.ModelSerializer):

    class Meta:
        model = Status
        fields = ['id', 'status', 'notes', 'date']


class InstallationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Installation
        fields = ['id', 'date_created', 'customer_name', 'address', 'appointment_date', 'current_status']
    
    current_status = serializers.SerializerMethodField()


    def get_current_status(self, installation: Installation):
        current_status = Status.objects.filter(installation_id=installation.pk).order_by('-date')[0]
        serializer = StatusSerializer(current_status)
        return serializer.data


class HistoryInstallationSerializer(serializers.ModelSerializer):

    status = StatusSerializer(many=True)
    
    class Meta:
        model = Installation
        fields = ['id', 'date_created', 'customer_name', 'address', 'appointment_date', 'status']

class CreateInstallationSerializer(serializers.ModelSerializer):

    status = StatusSerializer()

    class Meta:
        model = Installation
        fields = ['customer_name', 'address', 'appointment_date', 'status']


    def save(self, **kwargs):
    
        
        installation = Installation.objects.create(
                                            customer_name=self.validated_data['customer_name'],
                                            address=self.validated_data['address'],
                                            appointment_date=self.validated_data['appointment_date'],
                                            )
        status = Status.objects.create(installation=installation)


class UpdateStatusSerializer(serializers.ModelSerializer):

    class Meta:
        model = Status
        fields = ['status', 'notes']

    def save(self, **kwargs):

        installation = Installation.objects.get(pk=self.context['installation_id'])

        status = Status.objects.create(status=self.validated_data['status'],\
                                        notes=self.validated_data['notes'],\
                                        installation=installation)
        