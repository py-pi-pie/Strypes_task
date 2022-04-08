from django.conf.urls import url
from employee.views import EmployeesApi, UploadXLSX, AddEmployee, EditEmployee, Home

employee_patterns = [
    url(r'^edit-employee/', EditEmployee.as_view(), name='edit_employee'),
    url(r'^add-employee/', AddEmployee.as_view(), name='add_employee'),
    url(r'^get-all-employees/', EmployeesApi.as_view(), name='employees'),
    url(r'^upload-xlsx-file/', UploadXLSX.as_view(), name='upload_file'),
    url(r'', Home.as_view(), name='home'),

    ]