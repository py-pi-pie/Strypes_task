from django.conf.urls import url
from employee.views import EmployeesApi, UploadXLSX

employee_patterns = [
    # url(r'^get-all-employees/', EmployeesApi.as_view(), name='employees'),
    url(r'^get-all-employees/', UploadXLSX.as_view(), name='employees'),
    ]