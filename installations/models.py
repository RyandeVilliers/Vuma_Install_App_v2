from itertools import permutations
from django.db import models

class Installation(models.Model):

    customer_name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    appointment_date = models.DateField()
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-date_modified']
        permissions = [
            ('view_history', 'Can view history')
        ]

    def __str__(self) -> str:
        return self.customer_name

class Status(models.Model):

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
    installation = models.ForeignKey(Installation, on_delete=models.CASCADE, related_name='status')

    def __str__(self):
        return self.status
