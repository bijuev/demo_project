from django.test import TestCase
from django.utils import timezone
from first_app.models import Employee
from django.contrib.auth.models import User


class EmployeeModelTest(TestCase):
    
    def setUp(self):
        # Create a User instance for testing the ForeignKey relationship
        self.user = User.objects.create(username="testuser")

    def test_employee_creation_with_defaults(self):
        # Create an Employee instance without providing name or user
        employee = Employee.objects.create()

        # Check that the name defaults to "John Doe"
        self.assertEqual(employee.name, "John Doe")

        # Check that the user can be null
        self.assertIsNone(employee.user)

        # Check that the date_joined is set automatically
        self.assertIsNotNone(employee.date_joined)

        # Check that the date_joined is close to the current time
        self.assertTrue(timezone.now() - employee.date_joined < timezone.timedelta(seconds=1))

    def test_employee_creation_with_user(self):
        # Create an Employee instance with a User
        employee = Employee.objects.create(user=self.user)

        # Check that the employee has the correct user associated
        self.assertEqual(employee.user, self.user)

    def test_employee_str_method(self):
        # Create an Employee instance with a specific name
        employee = Employee.objects.create(name="Alice Doe")

        # Check that the __str__ method returns the name
        self.assertEqual(str(employee), "Alice Doe")
