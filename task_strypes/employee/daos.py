from employee.models import Employee
from django.db.models import QuerySet


def bulk_create_employees(table_entries: dict) -> None:
    """
    Creates Bulk db entries

    """

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


def create_employee(employee: dict) -> None:
    """
    Add single employee to db
    """
    Employee.objects.create(first_name=employee.get('first_name'),
                            last_name=employee.get('last_name'),
                            mobile_num=employee.get('mobile_num'),
                            start_date=employee.get('start_date'),
                            position=employee.get('position'),
                            salary=employee.get('salary'),
                            employee_id=employee.get('employee_id'),
                            )


def update_employee(queryset: QuerySet[Employee], employee: dict) -> None:
    """
    Update existing employee
    """
    queryset.update(first_name=employee.get('first_name'),
                    last_name=employee.get('last_name'),
                    mobile_num=employee.get('mobile_num'),
                    start_date=employee.get('start_date'),
                    position=employee.get('position'),
                    salary=employee.get('salary'),
                    employee_id=employee.get('employee_id')
                    )
