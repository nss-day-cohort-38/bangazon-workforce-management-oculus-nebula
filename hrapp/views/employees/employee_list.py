from django.shortcuts import render
from hrapp.models import Employee
from .data_manager.get_all_employees import get_all_employees

def employee_list(request):
    if request.method == 'GET':
            dataset = get_all_employees()
            all_employees = []

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
