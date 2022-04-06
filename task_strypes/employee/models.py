from django.db import models

# Create your models here.


class Employee(models.Model):
    """
    Represents the table that holds all the .....
    """

    TYPE_CEO = 'CEO'
    TYPE_JUNIOR = 'junior_dev'
    TYPE_SENIOR = 'senior_dev'
    TYPE_LEAD = 'team_lead'
    TYPE_MANAGER = 'project_manager'
    TYPE_EMPLOYEE = 'employee'

    POSITION_TYPES = (
        (TYPE_CEO, 'CEO'),
        (TYPE_JUNIOR, 'Junior Developer'),
        (TYPE_SENIOR, 'Senior Developer'),
        (TYPE_MANAGER, 'Project Manager'),
        (TYPE_LEAD, 'Team Lead'),
        (TYPE_EMPLOYEE, 'Employee'),
    )

    first_name = models.CharField(max_length=256)
    last_name = models.CharField(max_length=256)
    mobile_num = models.IntegerField()
    start_date = models.DateField()
    position = models.CharField(
        max_length=100,
        choices=POSITION_TYPES,
        default=TYPE_EMPLOYEE,
        help_text="Job position taken",
    )

    salary = models.IntegerField(default=0)
    employee_id = models.CharField(max_length=10)

    def __str__(self):
        return f'Employee Name: {self.first_name} {self.last_name}'
