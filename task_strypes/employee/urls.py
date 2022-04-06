from django.conf.urls import url

employee_patterns = [
    url(r'^/get-all-employees$', jjj.as_view(), name='employees'),
    ]