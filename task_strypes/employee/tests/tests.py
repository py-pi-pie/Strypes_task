from django.test import TestCase
from employee.tests.factories import EmployeeFactory
from rest_framework.test import APIClient
from django.urls import reverse
import datetime
from rest_framework import status
from django.conf import settings
import io


class HomeViewTestCase(TestCase):

    def setUp(self) -> None:

        self.client = APIClient()
        self.client.login(username='admin', password='strypes')

    def test_get_home(self):

        get_response = self.client.get(reverse('home'))
        self.assertEqual(get_response.status_code, status.HTTP_200_OK)


class EmployeesApiTestCase(TestCase):

    def setUp(self) -> None:
        self.employee = EmployeeFactory(first_name='Peter',
                                        last_name='Petrov',
                                        mobile_num='098675675',
                                        start_date=datetime.datetime.now().date(),
                                        position='CEO',
                                        salary='1000',
                                        employee_id='S-12345')
        self.client = APIClient()
        self.client.login(username='admin', password='strypes')

    def test_get_all_employees_from_db(self):

        get_response = self.client.get(reverse('employees'))
        self.assertEqual(get_response.status_code, status.HTTP_200_OK)
        self.assertTrue(len(get_response.data) == 1)
        self.assertTrue(get_response.data.get('profiles')[0].employee_id == 'S-12345')


class UploadXLSXTestCase(TestCase):

    def setUp(self) -> None:

        self.client = APIClient()
        self.client.login(username='admin', password='strypes')
        self.xlsx_file = settings.BASE_DIR + '/static_files/table_emp.xlsx'

    def test_post_method_success(self):
        with open(self.xlsx_file, 'rb') as fp:
            fio = io.FileIO(fp.fileno())
            fio.name = 'table_emp.xlsx'
            post_response = self.client.post(reverse('upload_file'), {'file_xlsx': fio, 'extraparameter': 5})

        self.assertEqual(post_response.status_code, status.HTTP_201_CREATED)

    def test_wrong_file_format(self):
        with open(self.xlsx_file, 'rb') as fp:
            fio = io.FileIO(fp.fileno())
            fio.name = 'table_emp.pdf'
            post_response = self.client.post(reverse('upload_file'), {'file_xlsx': fio, 'extraparameter': 5})

        self.assertEqual(post_response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_no_file_upload(self):
        fio = ''
        post_response = self.client.post(reverse('upload_file'), {'file_xlsx': fio, 'extraparameter': 5})

        self.assertEqual(post_response.status_code, status.HTTP_400_BAD_REQUEST)


class AddEmployeeTestCase(TestCase):

    def setUp(self) -> None:

        self.client = APIClient()
        self.client.login(username='admin', password='strypes')

    def test_add_employee(self):
        data = {'first_name': 'Mia', 'last_name': 'Kalinova', 'mobile_num': '098765345', 'start_date': '2021-11-19',
                'position': 'CEO', 'salary': '2500', 'employee_id': 'S-23654'
                }
        post_response = self.client.post(reverse('add_employee'), data)

        self.assertEqual(post_response.status_code, status.HTTP_201_CREATED)


class UpdateEmployeeTestCase(TestCase):

    def setUp(self) -> None:
        self.employee = EmployeeFactory(first_name='Peter',
                                        last_name='Petrov',
                                        mobile_num='098675675',
                                        start_date=datetime.datetime.now().date(),
                                        position='CEO',
                                        salary='1000',
                                        employee_id='S-12345')

        self.client = APIClient()
        self.client.login(username='admin', password='strypes')

    def test_update_employee(self):
        data = {'id_to_update': 'S-12345', 'first_name': 'Mia', 'last_name': 'Kalinova', 'start_date': '2021-11-19',
                'salary': '2500',
                }
        post_response = self.client.post(reverse('edit_employee'), data)

        self.assertEqual(post_response.status_code, status.HTTP_201_CREATED)

    def test_update_employee_not_found(self):
        data = {'id_to_update': 'S-56563', 'first_name': 'Mia', 'last_name': 'Kalinova', 'start_date': '2021-11-19',
                'salary': '2500',
                }
        post_response = self.client.post(reverse('edit_employee'), data)

        self.assertEqual(post_response.status_code, status.HTTP_404_NOT_FOUND)
