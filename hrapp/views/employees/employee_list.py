import sqlite3
from django.shortcuts import render
from hrapp.models import Employee
from ..connection import Connection


def employee_list(request):
    if request.method == 'GET':
        with sqlite3.connect(Connection.db_path) as conn:
            conn.row_factory = sqlite3.Row
            db_cursor = conn.cursor()

            '''
            Joins employee table with department table
            returns
            - Employee Id
            - Employee First Name
            - Employee Last Name
            - Employee Start Date
            - Employee is supervisor
            - Employee Department
            '''

            db_cursor.execute("""
                SELECT
                    e.id,
                    e.first_name,
                    e.last_name,
                    e.start_date,
                    e.is_supervisor,
                    d.id department_id
                FROM
                    hrapp_employee e
                JOIN hrapp_department d ON
                    d.id = e.department_id
            """)

            all_employees = []
            dataset = db_cursor.fetchall()

            for row in dataset:
                employee = Employee()
                employee.id = row['id']
                employee.first_name = row['first_name']
                employee.last_name = row['last_name']
                employee.start_date = row['start_date']
                # Adds entire department class to employee.department
                employee.department_id = row['department_id']

                all_employees.append(employee)

    template = 'employees/employees_list.html'
    context = {
        'employees': all_employees
    }

    return render(request, template, context)
