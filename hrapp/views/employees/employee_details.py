from .data_manager.get_employee_computer import get_employee_computer
from django.shortcuts import render
def employee_details(request, employee_id):
    employee_computer = get_employee_computer(employee_id)
    print(employee_computer.computer)
    template = "employees/employee_details.html"
    context = {
        "employee_computer": employee_computer
    }

    return render(request, template, context)