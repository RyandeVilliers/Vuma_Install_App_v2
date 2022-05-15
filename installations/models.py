from django.db import models

class installation(models.Model):

    customer_name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    appointment_date = models.DateField()
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['date_modified']

class status(models.Model):

    INSTALLATION_REQUESTED = 'Installation Requested'
    INSTALLATION_IN_PROGRESS = 'Installation in Progress'
    INSTALLATION_COMPLETE= 'Installation Complete'
    INSTALLATION_REJECTED = 'Installation Rejected'

    INSTALLATION_STATUSES = [
        (INSTALLATION_REQUESTED, 'Installation Requested'),
        (INSTALLATION_IN_PROGRESS, 'Installation in Progress'),
        (INSTALLATION_COMPLETE, 'Installation Complete'),
        (INSTALLATION_REJECTED, 'Installation Rejected')]

    status = models.CharField(
        max_length=30,
        choices=INSTALLATION_STATUSES,
        default=INSTALLATION_REQUESTED
    )

    notes = models.CharField(max_length=255)
    date = models.DateTimeField(auto_now=True)
