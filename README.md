# Strypes_task

#How to use
1. To start the project use "python3 manage.py runserver" (using the default ip:port - Starting development server at http://127.0.0.1:8000/)
2. http://127.0.0.1:8000/employee/  - is the home page of the project
3. http://127.0.0.1:8000/employee/get-all-employees/  - THis link will show all the employees from the database. 
Initially  will be empty page with no employees.
4. http://127.0.0.1:8000/employee/upload-xlsx-file/  - in this page you can upload the XLSX file which will be parsed 
and all the employees will be added to the DB. They could be seen with the link in 2.
5. http://127.0.0.1:8000/employee/add-employee/  -  Add employee to DB. Unique field - Employee ID
6. http://127.0.0.1:8000/employee/edit-employee/  -  Edit already existing employee by Employee ID string. 
Partial or full update of the fields can be done. 


# Unit Tests
- To run the Unit tests use "python3 manage.py test"



    
