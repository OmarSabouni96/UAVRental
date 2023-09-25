from django.test import TestCase
from django.urls import reverse
from uav_management.models import UAV  # Import your UAV model
from uavrental.users.models import User
from django.test import Client

class TestUAVListView(TestCase):
    def setUp(self):
        # Create a test user
        self.user = User.objects.create_user(
            username="testuser",
            email="test@example.com",
            password="testpassword"
        )

        # Create test UAV instances
        self.uav1 = UAV.objects.create(
            user=self.user,
            brand="Test Brand 1",
            model="Test Model 1",
            weight=10.0,
            category="Tactical",
        )
        self.uav2 = UAV.objects.create(
            user=self.user,
            brand="Test Brand 2",
            model="Test Model 2",
            weight=20.0,
            category="MALE",
        )

    def test_uav_list_view(self):
        client = Client()
        client.login(username="testuser", password="testpassword")

        # Test the UAVList view
        response = client.get(reverse("uav_list"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "uav/uav_list.html")
        
        # Check if the UAV instances are in the context, unordered
        uavs_in_context = response.context["uavs"]
        self.assertIn(self.uav1, uavs_in_context)
        self.assertIn(self.uav2, uavs_in_context)


    def test_uav_list_api_view(self):
        client = Client()
        client.login(username="testuser", password="testpassword")

        # Test the UAVListApi view
        response = client.get(reverse("uav_list_api"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "uav/uav_list_api.html")

