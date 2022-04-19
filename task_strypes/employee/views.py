from datetime import datetime

from django.http import HttpResponseBadRequest, HttpResponse
from django.urls import reverse
from django.shortcuts import redirect
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response

from employee.models import Employee
from employee.serializers import EmployeeSerializer
from employee.app_logic import read_xlsx_from_memory, get_data_from_xlsx_sheet, format_ws_fields, create_update_data
from employee.daos import bulk_create_employees, create_employee, update_employee


POSITION_FIELD_REPRESENTATION = {'ceo': 'CEO', 'junior developer': 'junior_dev',
                                 'senior developer': 'senior_dev', 'team lead': 'team_lead',
                                 'project manager': 'project_manager'}

POSITION_FIELD_REPRESENTATION_TABLE = {'ceo': 'CEO', 'junior_dev': 'Junior Developer',
                                       'senior_dev': 'Senior Developer', 'team_lead': 'Team Lead',
                                       'project_manager': 'Project Manager'}

POSITION_CONSTANT = ['ceo', 'junior developer', 'senior developer', 'team lead', 'project manager']


class Home(APIView):
    """
    Home Page View
    """

    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'home_page.html'

    def get(self, request):
        return Response(status=status.HTTP_200_OK)


class EmployeesApi(APIView):
    """
    Get All Employees from the DB
    """

    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'all_employees.html'

    def get(self, request):
        queryset = Employee.objects.all()

        if queryset:
            for employee in queryset:
                employee.position = POSITION_FIELD_REPRESENTATION_TABLE.get(employee.position.lower())

        return Response({'profiles': queryset})


class UploadXLSX(APIView):
    """
    Parse xlsx File View
    Uploads the File data to DB
    """

    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'file_upload.html'
    employee_serializer = EmployeeSerializer

    def get(self, request):
        return Response()

    def post(self, request):

        if request.FILES.get('file_xlsx'):
            if request.FILES.get('file_xlsx').name.split('.')[1] in ['xls', 'xlsx']:

                ws = read_xlsx_from_memory(request)
                employees = get_data_from_xlsx_sheet(ws)
                format_ws_fields(employees)

                serializer_employees = self.employee_serializer(data=employees, many=True)

                if serializer_employees.is_valid():
                    table_entries = serializer_employees.data
                    try:
                        bulk_create_employees(table_entries)
                    except Exception as e:
                        message = f'DB data inconsistency  {e}\n ' \
                                  f'<p><a href="{reverse("home")}">Home Page</a></p>'
                        return HttpResponse(message, status=status.HTTP_400_BAD_REQUEST)

                    message = 'Bulk data has been uploaded to db Successfully \n ' \
                              f'<p><a href="{reverse("home")}">Home Page</a></p>'
                    return HttpResponse(message, status=status.HTTP_201_CREATED)

        message = f'No File has been uploaded or not the right type (XLS, XLSX)\n ' \
                  f'<p><a href="{reverse("home")}">Home Page</a></p>'
        return HttpResponseBadRequest(message, status=status.HTTP_400_BAD_REQUEST)


class AddEmployee(APIView):
    """
    Add Employee to DB View
    """

    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'create_employee.html'
    employee_serializer = EmployeeSerializer

    def get(self, request):
        return Response()

    def post(self, request):

        employee = {'first_name': request.data.get('first_name'),
                    'last_name': request.data.get('last_name'),
                    'mobile_num': int(request.data.get('mobile_num')) if request.data.get('mobile_num') else 0,
                    'start_date': datetime.strptime(request.data.get('start_date'),
                                                    '%Y-%m-%d').date() if request.data.get(
                        'start_date') else datetime.now().date(),
                    'position': POSITION_FIELD_REPRESENTATION.get(request.data.get('position').lower())
                    if request.data.get('position').lower() in POSITION_CONSTANT else 'Employee',
                    'salary': int(request.data.get('salary')) if request.data.get('salary') else 0,
                    'employee_id': request.data.get('employee_id'),
                    }

        serializer_employees = self.employee_serializer(data=employee)

        if serializer_employees.is_valid():
            try:
                create_employee(employee)
            except Exception as e:
                message = f'DB data inconsistency  {e}\n ' \
                          f'<p><a href="{reverse("home")}">Home Page</a></p>'
                return HttpResponse(message, status=status.HTTP_400_BAD_REQUEST)

            message = 'Employee has been created Successfully \n ' \
                      f'<p><a href="{reverse("home")}">Home Page</a></p>'
            return HttpResponse(message, status=status.HTTP_201_CREATED)


class EditEmployee(APIView):
    """
    Edit existing employee View
    """

    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'update_employee.html'
    employee_serializer = EmployeeSerializer

    def get(self, request):
        return Response()

    def post(self, request):

        employee_to_update_set = Employee.objects.filter(employee_id=request.data.get('id_to_update'))

        if employee_to_update_set:
            employee_to_update = employee_to_update_set[0]
            employee = create_update_data(request, employee_to_update)

            serializer_employees = self.employee_serializer(data=employee)

            if serializer_employees.is_valid():
                try:
                    update_employee(employee_to_update_set, employee)
                except Exception as e:
                    message = f'DB data inconsistency  {e}\n ' \
                              f'<p><a href="{reverse("home")}">Home Page</a></p>'
                    return HttpResponse(message, status=status.HTTP_400_BAD_REQUEST)

                message = f'Employee with ID {request.data.get("id_to_update")} has been updated \n ' \
                          f'<p><a href="{reverse("home")}">Home Page</a></p>'
                return HttpResponse(message, status=status.HTTP_201_CREATED)

        message = f'Employee with ID {request.data.get("id_to_update")} NOT found \n ' \
                  f''f'<p><a href="{reverse("home")}">Home Page</a></p>'
        return HttpResponseBadRequest(message, status=status.HTTP_404_NOT_FOUND)


def view_404(request, exception=None):
    """
    All 404 http requests from the server will
    be redirected to the home page
    """
    return redirect(reverse("home"))
