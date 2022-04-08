from django.conf.urls import url
from employee.views import EmployeesApi, UploadXLSX, AddEmployee

employee_patterns = [
    # url(r'^get-all-employees/', EmployeesApi.as_view(), name='employees'),
    url(r'^get-all-employees/', AddEmployee.as_view(), name='employees'),
    ]