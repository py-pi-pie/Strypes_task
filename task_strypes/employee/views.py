from rest_framework.views import APIView
from rest_framework import serializers
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from openpyxl import load_workbook
from io import BytesIO
from datetime import datetime


from django.http import HttpResponse
import os

from employee.models import Employee
import re

MOBILE_REGEX = re.compile(r'\d+')

class EmployeesApi(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'all_employees.html'

    def get(self, request):
        queryset = Employee.objects.all()
        return Response({'profiles': queryset})


class UploadXLSX(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'file_upload.html'

    class EmployeeSerializer(serializers.Serializer):
        first_name = serializers.CharField()
        last_name = serializers.CharField()
        mobile_num = serializers.IntegerField()
        start_date = serializers.DateField()
        position = serializers.CharField()
        salary = serializers.IntegerField()
        employee_id = serializers.CharField()


    def get(self, request):
        return Response()

    def post(self, request):

        if request.FILES['file_xlsx']:
            file_in_memory = request.FILES['file_xlsx'].read()
            wb = load_workbook(filename=BytesIO(file_in_memory))
            # wb.iso_dates = True

            ws = wb.active
            var = ws.cell(row=1, column=2)

            employees = []
            n = 2
            columns = ['first_name', 'last_name', 'mobile_num', 'start_date', 'position', 'salary', 'employee_id']
            while ws.cell(row=n, column=1).value:
                employee = []

                for i in range(1, 8):
                    employee.append(ws.cell(row=n, column=i).value)

                employees.append(
                    dict(zip(columns, employee))
                )
                n += 1

            POSITION_FIELD_REPRESENTATION = {'CEO': 'CEO', 'Junior Developer': 'junior_dev',
                                             'Senior Developer': 'senior_dev', 'Team Lead': 'team_lead',
                                             'Project Manager': 'project_manager' }
            for i in employees:
                if type(i.get('start_date')) == str:
                    formatted_date = datetime.strptime(i.get('start_date'), '%d/%m/%Y').date()
                else:
                    formatted_date = i.get('start_date').date()

                position_db_represented = POSITION_FIELD_REPRESENTATION.get(i.get('position'))

                salary_extracted = int(re.search(MOBILE_REGEX, i.get('salary')).group(0))

                i.update({'start_date': formatted_date,
                          'salary': salary_extracted,
                          'position': position_db_represented}
                         )






            serializer_employees = self.EmployeeSerializer(data=employees, many=True)

            if serializer_employees.is_valid():
                table_entries = serializer_employees.data

                db_bulk_data = [Employee(first_name=table_entry.get('first_name'),
                                         last_name=table_entry.get('last_name'),
                                         mobile_num=table_entry.get('mobile_num'),
                                         start_date=table_entry.get('start_date'),
                                         position=table_entry.get('position'),
                                         salary=table_entry.get('salary'),
                                         employee_id=table_entry.get('employee_id'),
                                         )
                                for table_entry in table_entries]

                Employee.objects.bulk_create(db_bulk_data)
        import pdb; pdb.set_trace()






def homePageView(request):
    import pdb
    return HttpResponse(f'{os.path.dirname(os.path.dirname(os.path.abspath(__file__)))}')


def simple_upload(request):
    import pdb; pdb.set_trace()
    # if request.method == 'POST' and request.FILES['myfile']:
    #     myfile = request.FILES['myfile']
    #     fs = FileSystemStorage()
    #     filename = fs.save(myfile.name, myfile)
    #     uploaded_file_url = fs.url(filename)
    #     return render(request, 'core/simple_upload.html', {
    #         'uploaded_file_url': uploaded_file_url
    #     })
    # return render(request, 'core/simple_upload.html')