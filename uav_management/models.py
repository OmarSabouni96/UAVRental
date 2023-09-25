# models.py
from django.db import models
import uuid

from django.utils import timezone
from datetime import date  # Import date class from datetime module
from uavrental.users.models import User
from django.core.exceptions import ValidationError




class UAV(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)  # Member who rented
    CATEGORY_CHOICES = (
        ('Tactical', 'Tactical'),
        ('MALE', 'Medium Altitude Long Endurance (MALE)'),
        ('HALE', 'High Altitude Long Endurance (HALE)'),
        ('Mini UAV', 'Mini UAV'),

        # Add more categories as needed
    )

    brand = models.CharField(max_length=50)
    model = models.CharField(max_length=100)
    weight = models.DecimalField(max_digits=5, decimal_places=1)
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES, default="Tactical")
    # availability = models.BooleanField(default=True)

    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField (default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    def __str__(self):
        return f"{self.brand} {self.model}"

    class Meta:
        ordering = ['-created']  



class UAVRental(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Member who rented
    uav = models.ForeignKey(UAV, on_delete=models.CASCADE)    # Rented UAV
    rental_start_date = models.DateField()
    rental_end_date = models.DateField()


    def clean(self):
        if self.rental_start_date < date.today():
            raise ValidationError("Rental start date cannot be in the past.")

        elif self.rental_start_date >= self.rental_end_date:
            raise ValidationError("Rental start date must be earlier than the end date.")



    def __str__(self):
        return f"{self.user.username} rented {self.uav.brand} {self.uav.model}"

    class Meta:
        ordering = ['-rental_start_date','-rental_end_date']  