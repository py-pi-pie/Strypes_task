from django.test import TestCase
from django.conf import settings
from employee.app_logic import read_xlsx_from_memory, get_data_from_xlsx_sheet
from unittest.mock import MagicMock
import datetime

WS_DATA = [{'first_name': 'John', 'last_name': 'Smith', 'mobile_num': 811123456.0,
            'start_date': datetime.datetime(2001, 1, 1, 0, 0), 'position': 'Junior Developer', 'salary': 'BGN 1000',
            'employee_id': 'S-1212'}, {'first_name': 'Jack', 'last_name': 'Daniels', 'mobile_num': 811654321.0,
                                       'start_date': datetime.datetime(2000, 2, 3, 0, 0), 'position': 'CEO',
                                       'salary': 'BGN 3300', 'employee_id': 'S-0001'},
           {'first_name': 'Michael ', 'last_name': 'Jordan', 'mobile_num': 811213122.0,
            'start_date': datetime.datetime(2003, 5, 9, 0, 0), 'position': 'Senior Developer', 'salary': 'BGN 2000',
            'employee_id': 'S-0201'}, {'first_name': 'Christian', 'last_name': 'Bale', 'mobile_num': 811213543.0,
                                       'start_date': datetime.datetime(2005, 10, 12, 0, 0),
                                       'position': 'Senior Developer', 'salary': 'BGN 1800', 'employee_id': 'S-3212'},
           {'first_name': 'Hugh', 'last_name': 'Grant', 'mobile_num': 811138848.0, 'start_date': '22/08/2006',
            'position': 'Team Lead', 'salary': 'BGN 1500', 'employee_id': 'S-2000'},
           {'first_name': 'Jim', 'last_name': 'Beam', 'mobile_num': 811654321.0, 'start_date': '15/03/2008',
            'position': 'Junior Developer', 'salary': 'BGN 800', 'employee_id': 'S-3213'},
           {'first_name': 'Terry', 'last_name': 'Crews', 'mobile_num': 811213122.0, 'start_date': '16/04/2002',
            'position': 'Junior Developer', 'salary': 'BGN 800', 'employee_id': 'S-1323'},
           {'first_name': 'Brad', 'last_name': 'Pitt', 'mobile_num': 811213543.0,
            'start_date': datetime.datetime(2012, 12, 12, 0, 0), 'position': 'Project Manager', 'salary': 'BGN 1400',
            'employee_id': 'S-5463'},
           {'first_name': 'Angelina', 'last_name': 'Jolie', 'mobile_num': 811123456.0, 'start_date': '15/01/2018',
            'position': 'Junior Developer', 'salary': 'BGN 1000', 'employee_id': 'S-6543'},
           {'first_name': 'Michael ', 'last_name': 'Felps', 'mobile_num': 811654321.0, 'start_date': '16/09/2020',
            'position': 'Team Lead', 'salary': 'BGN 1300', 'employee_id': 'S-8933'},
           {'first_name': 'Marshal', 'last_name': 'Matters', 'mobile_num': 811213122.0, 'start_date': '31/01/2005',
            'position': 'Project Manager', 'salary': 'BGN 1700', 'employee_id': 'S-5782'},
           {'first_name': 'Christian', 'last_name': 'Bale', 'mobile_num': 811213544.0, 'start_date': '28/08/2000',
            'position': 'Junior Developer', 'salary': 'BGN 700', 'employee_id': 'S-9356'},
           {'first_name': 'Tupac', 'last_name': 'Shakur', 'mobile_num': 811123456.0, 'start_date': '19/07/2013',
            'position': 'Junior Developer', 'salary': 'BGN 600', 'employee_id': 'S-5432'},
           {'first_name': 'Lebron', 'last_name': 'James', 'mobile_num': 811654321.0, 'start_date': '17/06/2010',
            'position': 'Team Lead', 'salary': 'BGN 1500', 'employee_id': 'S-9934'},
           {'first_name': 'Lena', 'last_name': 'Headey', 'mobile_num': 811213122.0, 'start_date': '22/02/2020',
            'position': 'Junior Developer', 'salary': 'BGN 1100', 'employee_id': 'S-5673'},
           {'first_name': 'Emma', 'last_name': 'Stone', 'mobile_num': 811213543.0, 'start_date': '19/05/2014',
            'position': 'Senior Developer', 'salary': 'BGN 2200', 'employee_id': 'S-7885'}]


class UploadXLSXTestCase(TestCase):

    def setUp(self) -> None:

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


