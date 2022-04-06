from django.conf.urls import url
from employee.views import homePageView, EmployeesApi

employee_patterns = [
    url(r'^get-all-employees/', EmployeesApi.as_view(), name='employees'),
    ]