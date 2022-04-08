from rest_framework import serializers


class EmployeeSerializer(serializers.Serializer):
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    mobile_num = serializers.IntegerField()
    start_date = serializers.DateField()
    position = serializers.CharField()
    salary = serializers.IntegerField()
    employee_id = serializers.CharField()