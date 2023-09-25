from django.test import TestCase
from uav_management.models import UAVRental,UAV
from django.core.exceptions import ValidationError
from datetime import date
from uavrental.users.models import User


class TestUAVModel(TestCase):
    def test_uav_str(self):
        uav = UAV(brand="Test Brand", model="Test Model")
        self.assertEqual(str(uav), "Test Brand Test Model")


# pytest tests/test_models.py
class TestUAVRentalModel(TestCase):
    def setUp(self):
        # Create a user instance for testing
        self.user = User.objects.create_user(
            username="testuser",
            email="test@example.com",
            password="testpassword"
        )
        
        # Create a UAV instance for testing
        self.uav = UAV.objects.create(
            user=self.user,
            brand="Test Brand",
            model="Test Model",
            weight=10.0,
            category="Tactical",
        )

    def test_rental_str(self):
        uav_rental = UAVRental(
            user=self.user,
            uav=self.uav,
            rental_start_date=date.today(),
            rental_end_date=date.today(),
        )
        self.assertEqual(
            str(uav_rental), f"{uav_rental.user.username} rented {uav_rental.uav.brand} {uav_rental.uav.model}"
        )

         # Create a UAV instance for testing
        self.uav = UAV.objects.create(
            user=self.user,  # Use the user instance created above
            brand="Test Brand",
            model="Test Model",
            weight=10.0,
            category="Tactical",
            )


    def test_rental_start_date_in_past(self):
        with self.assertRaises(ValidationError):
            uav_rental = UAVRental(
                user_id=1,
                uav_id=2,
                rental_start_date=date(2020, 1, 1),
                rental_end_date=date(2020, 1, 10),
            )
            uav_rental.clean()

    

    def test_rental_start_date_equals_end_date(self):
        with self.assertRaises(ValidationError):
            uav_rental = UAVRental(
                user_id=1,
                uav_id=2,
                rental_start_date=date(2023, 1, 1),
                rental_end_date=date(2023, 1, 1),
            )
            uav_rental.clean()

    def test_rental_start_date_after_end_date(self):
        with self.assertRaises(ValidationError):
            uav_rental = UAVRental(
                user_id=1,
                uav_id=2,
                rental_start_date=date(2023, 1, 10),
                rental_end_date=date(2023, 1, 1),
            )
            uav_rental.clean()


# Checking the string representation.
# Testing if an exception is raised when the rental_start_date is in the past.
# Testing if an exception is raised when the rental_start_date is equal to the rental_end_date.
# Testing if an exception is raised when the rental_start_date is after the rental_end_date.
# Step 4: Run the Tests
# pytest tests/test_models.py

