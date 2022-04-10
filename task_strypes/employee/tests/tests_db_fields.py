from django.test import TestCase
from employee.tests.factories import EmployeeFactory
from datetime import datetime

from django.core.exceptions import ValidationError


class DBTestCase(TestCase):
    maxDiff = None

    def setUp(self) -> None:
        self.employee = EmployeeFactory(first_name='Peter',
                                        last_name='Petrov',
                                        mobile_num='098675675',
                                        start_date=datetime.now().date(),
                                        position='CEO',
                                        salary='1000',
                                        employee_id='S-12345')

        self.employee_2 = EmployeeFactory(first_name='Peter',
                                          last_name='Parcker',
                                          mobile_num='098675785',
                                          start_date=datetime.now().date(),
                                          position='CEO',
                                          salary='2000',
                                          employee_id='S-12347')

    def test_first_name_field_length(self):
        name = 'Dimitrinka' * 20

        self.employee.first_name = name
        with self.assertRaises(ValidationError):
            self.employee.full_clean()

    def test_last_name_field_length(self):
        name = 'Dimitrinkova' * 20

        self.employee.last_name = name
        with self.assertRaises(ValidationError):
            self.employee.full_clean()

    def test_mobile_field_chars(self):
        mobile = '09isjjdnaafs'

        self.employee.mobile_num = mobile
        with self.assertRaises(ValidationError):
            self.employee.full_clean()

    def test_position_field(self):
        position = 'Chancellor'

        self.employee.position = position
        with self.assertRaises(ValidationError):
            self.employee.full_clean()

    def test_salary_field(self):
        salary = 'BGN 100'

        self.employee.salary = salary
        with self.assertRaises(ValidationError):
            self.employee.full_clean()

    def test_employee_id_field_unique(self):
        employee_id = 'S-12345'

        self.employee_2.employee_id = employee_id
        with self.assertRaises(ValidationError):
            self.employee_2.full_clean()
