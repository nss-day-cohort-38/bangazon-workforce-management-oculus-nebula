from django.shortcuts import render
from .data_manager import (
    get_employee_training, 
    get_all_trainings,
    get_all_departments,
    get_employee
)


def employee_add_program(request, employee_id):
    """
    This function handles all of the request to the edit employee page
    """
    if request.method == "GET":
        employee = get_employee(employee_id)
        all_programs = get_all_trainings()
        employee_trainings = [i.training_program.title for i in get_employee_training(employee_id)]
        programs = [i for i in all_programs if i.title not in employee_trainings]

        template = "employees/employee_add_program.html"
        context = {
            "programs": programs,
            "employee": employee
        }
        return render(request, template, context)
