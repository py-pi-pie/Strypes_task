import datetime

UPDATED_USER_DATA = {'first_name': 'Dimitar', 'last_name': 'Berbatov', 'mobile_num': '098675675',
                     'start_date': datetime.datetime.now().date(), 'position': 'CEO', 'salary': '1000',
                     'employee_id': 'S-12345'}

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

FORMATED_WS_DATA = [
    {'first_name': 'John', 'last_name': 'Smith', 'mobile_num': 811123456.0, 'start_date': datetime.date(2001, 1, 1),
     'position': 'junior_dev', 'salary': 1000, 'employee_id': 'S-1212'},
    {'first_name': 'Jack', 'last_name': 'Daniels', 'mobile_num': 811654321.0, 'start_date': datetime.date(2000, 2, 3),
     'position': 'CEO', 'salary': 3300, 'employee_id': 'S-0001'},
    {'first_name': 'Michael ', 'last_name': 'Jordan', 'mobile_num': 811213122.0,
     'start_date': datetime.date(2003, 5, 9), 'position': 'senior_dev', 'salary': 2000, 'employee_id': 'S-0201'},
    {'first_name': 'Christian', 'last_name': 'Bale', 'mobile_num': 811213543.0,
     'start_date': datetime.date(2005, 10, 12), 'position': 'senior_dev', 'salary': 1800, 'employee_id': 'S-3212'},
    {'first_name': 'Hugh', 'last_name': 'Grant', 'mobile_num': 811138848.0, 'start_date': datetime.date(2006, 8, 22),
     'position': 'team_lead', 'salary': 1500, 'employee_id': 'S-2000'},
    {'first_name': 'Jim', 'last_name': 'Beam', 'mobile_num': 811654321.0, 'start_date': datetime.date(2008, 3, 15),
     'position': 'junior_dev', 'salary': 800, 'employee_id': 'S-3213'},
    {'first_name': 'Terry', 'last_name': 'Crews', 'mobile_num': 811213122.0, 'start_date': datetime.date(2002, 4, 16),
     'position': 'junior_dev', 'salary': 800, 'employee_id': 'S-1323'},
    {'first_name': 'Brad', 'last_name': 'Pitt', 'mobile_num': 811213543.0, 'start_date': datetime.date(2012, 12, 12),
     'position': 'project_manager', 'salary': 1400, 'employee_id': 'S-5463'},
    {'first_name': 'Angelina', 'last_name': 'Jolie', 'mobile_num': 811123456.0,
     'start_date': datetime.date(2018, 1, 15), 'position': 'junior_dev', 'salary': 1000, 'employee_id': 'S-6543'},
    {'first_name': 'Michael ', 'last_name': 'Felps', 'mobile_num': 811654321.0,
     'start_date': datetime.date(2020, 9, 16), 'position': 'team_lead', 'salary': 1300, 'employee_id': 'S-8933'},
    {'first_name': 'Marshal', 'last_name': 'Matters', 'mobile_num': 811213122.0,
     'start_date': datetime.date(2005, 1, 31), 'position': 'project_manager', 'salary': 1700, 'employee_id': 'S-5782'},
    {'first_name': 'Christian', 'last_name': 'Bale', 'mobile_num': 811213544.0,
     'start_date': datetime.date(2000, 8, 28), 'position': 'junior_dev', 'salary': 700, 'employee_id': 'S-9356'},
    {'first_name': 'Tupac', 'last_name': 'Shakur', 'mobile_num': 811123456.0, 'start_date': datetime.date(2013, 7, 19),
     'position': 'junior_dev', 'salary': 600, 'employee_id': 'S-5432'},
    {'first_name': 'Lebron', 'last_name': 'James', 'mobile_num': 811654321.0, 'start_date': datetime.date(2010, 6, 17),
     'position': 'team_lead', 'salary': 1500, 'employee_id': 'S-9934'},
    {'first_name': 'Lena', 'last_name': 'Headey', 'mobile_num': 811213122.0, 'start_date': datetime.date(2020, 2, 22),
     'position': 'junior_dev', 'salary': 1100, 'employee_id': 'S-5673'},
    {'first_name': 'Emma', 'last_name': 'Stone', 'mobile_num': 811213543.0, 'start_date': datetime.date(2014, 5, 19),
     'position': 'senior_dev', 'salary': 2200, 'employee_id': 'S-7885'}]
