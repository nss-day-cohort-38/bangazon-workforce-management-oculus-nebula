import sqlite3
from django.shortcuts import render
from hrapp.models import Department, model_factory
from ..connection import Connection



def department_list(request):
    if request.method == 'GET':
        with sqlite3.connect(Connection.db_path) as conn:
            conn.row_factory = sqlite3.Row
            db_cursor = conn.cursor()

            db_cursor.execute("""
          SELECT COUNT(department_name) employees,
                d.id,
                d.department_name,
                d.budget
            FROM hrapp_department d, hrapp_employee e
            WHERE d.id = e.department_id
            GROUP BY d.department_name
            """)

            all_departments = []
            dataset = db_cursor.fetchall()

            for row in dataset:
                department = Department()
                department.id = row['id']
                department.department_name = row['department_name']
                department.budget = row['budget']
                department.employees = row['employees']

                all_departments.append(department)

    template = 'departments/departments_list.html'
    context = {
        'departments': all_departments
    }

    return render(request, template, context)
