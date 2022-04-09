from factory.django import DjangoModelFactory
from employee.models import Employee


class EmployeeFactory(DjangoModelFactory):
    class Meta:
        model = Employee
