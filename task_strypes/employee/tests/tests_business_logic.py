from django.test import TestCase
from django.conf import settings
from employee.app_logic import read_xlsx_from_memory, get_data_from_xlsx_sheet, format_start_date_field, \
    format_ws_fields, create_update_data
from unittest.mock import MagicMock
from datetime import datetime

from employee.tests.static_test_data import WS_DATA, FORMATED_WS_DATA, UPDATED_USER_DATA

from copy import deepcopy
from employee.tests.factories import EmployeeFactory


class AppLogicTestCase(TestCase):
    maxDiff = None

    def setUp(self) -> None:
        self.employee = EmployeeFactory(first_name='Peter',
                                        last_name='Petrov',
                                        mobile_num='098675675',
                                        start_date=datetime.now().date(),
                                        position='CEO',
                                        salary='1000',
                                        employee_id='S-12345')

        self.xlsx_file = settings.BASE_DIR + '/static_files/table_emp.xlsx'

    def test_read_xlsx_from_memory(self):
        with open(self.xlsx_file, 'rb') as fp:
            request_mock = MagicMock(FILES={'file_xlsx': fp})
            ws = read_xlsx_from_memory(request_mock)

            self.assertTrue(f'{ws.cell(row=2, column=1).value} '
                            f'{ws.cell(row=2, column=2).value}' == 'John Smith')

    def test_get_data_from_xlsx_sheet(self):
        with open(self.xlsx_file, 'rb') as fp:
            request_mock = MagicMock(FILES={'file_xlsx': fp})
            ws = read_xlsx_from_memory(request_mock)
        employees_from_file = get_data_from_xlsx_sheet(ws)

        self.assertEqual(employees_from_file, WS_DATA)

    def test_format_start_date_field_string(self):
        date_r = format_start_date_field(WS_DATA[7])
        created_date = datetime.strptime('12/12/2012', '%d/%m/%Y').date()

        self.assertEqual(date_r, created_date)

    def test_format_start_date_field_time_removed(self):
        date_r = format_start_date_field(WS_DATA[0])
        created_date = datetime.strptime('1/1/2001', '%d/%m/%Y').date()

        self.assertEqual(date_r, created_date)

    def test_format_ws_fields(self):
        test_data = deepcopy(WS_DATA)
        format_ws_fields(test_data)

        self.assertEqual(test_data, FORMATED_WS_DATA)

    def test_create_update_data(self):
        fields_to_update = MagicMock(data={'first_name': 'Dimitar', 'last_name': 'Berbatov'})
        updated_user_data = create_update_data(fields_to_update, self.employee)

        self.assertEqual(UPDATED_USER_DATA, updated_user_data)
