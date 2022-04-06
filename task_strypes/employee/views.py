from rest_framework.views import APIView
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response

from django.http import HttpResponse
import os

from employee.models import Employee


class EmployeesApi(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'all_employees.html'

    def get(self, request):
        queryset = Employee.objects.all()
        return Response({'profiles': queryset})


def homePageView(request):
    import pdb
    return HttpResponse(f'{os.path.dirname(os.path.dirname(os.path.abspath(__file__)))}')