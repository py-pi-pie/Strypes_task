from django.contrib import admin
from employee.models import Employee


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):

    list_display = [
        'id',
        'first_name',
        'last_name',
        'mobile_num',
        'start_date',
        'position',
        'salary',
        'employee_id',
    ]

    search_fields = [
        'id',
        'first_name',
        'last_name',
        'mobile_num',
    ]

    save_on_top = True
    list_per_page = 40
