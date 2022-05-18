from rest_framework import serializers
from .models import Installation, Status


class StatusSerializer(serializers.ModelSerializer):

    class Meta:
        model = Status
        fields = ['id', 'status', 'notes', 'date']


class InstallationSerializer(serializers.ModelSerializer):

    status = StatusSerializer(many=True, read_only=True)

    class Meta:
        model = Installation
        fields = ['id', 'date_created', 'customer_name', 'address', 'appointment_date', 'status' ]
    
    # 'current_status'
    # current_status = serializers.SerializerMethodField()


    # def get_current_status(self, installation: Installation):
    #     return Status.objects.filter(installation_id=installation.pk).order_by('-date')[0]

class CreateInstallationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Installation
        fields = ['customer_name', 'address', 'appointment_date']

    def save(self, **kwargs):
    
        
        installation = Installation.objects.create(
                                            customer_name=self.validated_data['customer_name'],
                                            address=self.validated_data['address'],
                                            appointment_date=self.validated_data['appointment_date'],
                                            )
        status=Status.objects.create(installation=installation)



