from rest_framework import serializers
from .models import Installation, Status


class InstallationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Installation
        fields = ['id', 'customer_name', 'address', 'appointment_date', 'current_status' ]
    

    current_status = serializers.SerializerMethodField()


    def get_current_status(self, installation: Installation):
        return Status.objects.filter(installation_id=installation.pk).order_by('-date')[0]


class StatusSerializer(serializers.ModelSerializer):

    class Meta:
        model = Status
        fields = ['id', 'status', 'notes', 'date']