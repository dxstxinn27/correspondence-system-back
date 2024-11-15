from django.db import models
from MyApps.persons.models import *
from MyApps.logistics.models import *
from MyApps.branches.models import *
import random
import string


# Create your models here.

class Correspondence(models.Model):
    code = models.CharField(max_length=6, unique=True, editable=False, verbose_name="code follow")
    correspondenceType = models.CharField(max_length=30, verbose_name="correspondence type")
    weight = models.DecimalField(max_digits=5, decimal_places=2, verbose_name="weight")
    dimensions = models.CharField(max_length=50, verbose_name="dimensions")
    shipmentDate = models.DateField(verbose_name="shipment date")
    deliveryDate = models.DateField(verbose_name="delivery date")
    sender = models.ForeignKey(Customer, related_name='sent_correspondences', verbose_name="sender", on_delete=models.CASCADE)
    receiver = models.ForeignKey(Customer,  related_name='received_correspondences', verbose_name="receiver", on_delete=models.CASCADE)
    service = models.ForeignKey(Service, on_delete=models.CASCADE, verbose_name="service")

    def generate_tracking_code(self):
        characters = string.ascii_uppercase + string.digits
        return ''.join(random.choices(characters, k=6))

    def save(self, *args, **kwargs):
        if not self.code:
            self.code = self.generate_tracking_code()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.code
    
    class Meta:
        verbose_name = "correspondence"
        verbose_name_plural = "correspondences"

class Shipping(models.Model):
    SHIPPING_STATUS_CHOICES = [
        ['AT ORIGIN', 'At origin'],
        ['AT DESTINATION', 'At destination'],
        ['ON THE WAY', 'On the way'],
        ['DELIVERED', 'Delivered'],
    ]

    status = models.CharField(max_length=20, choices=SHIPPING_STATUS_CHOICES, help_text="Select shipping status.")
    dateTime = models.DateTimeField(verbose_name="date and time")
    correspondence = models.ForeignKey(Correspondence, verbose_name="correspondence", on_delete=models.CASCADE)
    branch = models.ForeignKey(Branch, on_delete=models.CASCADE, verbose_name="branch")
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, verbose_name="employee")

    def __str__(self):
        return f'{self.status} -> {self.dateTime}'
    
    class Meta:
        verbose_name = "shipping"
        verbose_name_plural = "shippings"

class Incident(models.Model):
    description = models.TextField(max_length=250, verbose_name="description")
    incidentDate = models.DateTimeField(verbose_name="incident date")
    RESOLUTION_STATUS_CHOICES = [
        ['REPORTED', 'Reported'],
        ['SCALED', 'Scaled'],
        ['IN RESOLUTION', 'In resolution'],
        ['RESOLVED', 'Resolved'],
        ['CLOSED', 'Closed'],
    ]

    resolutionStatus = models.CharField(max_length=20, choices=RESOLUTION_STATUS_CHOICES)
    correspondence = models.ForeignKey(Correspondence, verbose_name="correspondence", on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.description} -> {self.resolutionStatus}'