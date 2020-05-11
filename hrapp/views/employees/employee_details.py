from .data_manager.get_employee_computer import get_employee_computers
from .data_manager.get_employee_trainings import get_employee_training
from .data_manager.get_employee import get_employee
from django.shortcuts import render

def employee_details(request, employee_id):
    """
    This function handles all of the request to the employee's detail page
    """
    if request.method == "GET":
        employee = get_employee(employee_id)
        employee_computers = [i.computer for i in get_employee_computers(employee_id)]
        employee_programs = [i.training_program for i in get_employee_training(employee_id)]
        template = "employees/employee_details.html"

        context = {
            "employee_computers": employee_computers,
            "employee_programs": employee_programs,
            "employee": employee
        }

        return render(request, template, context)