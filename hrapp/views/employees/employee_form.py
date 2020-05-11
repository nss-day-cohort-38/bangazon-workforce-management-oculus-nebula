from django.shortcuts import render
from .data_manager.get_all_departments import get_all_departments

def employee_add(request):
    if request.method == "GET":
        departments = get_all_departments()
        template = "employees/employee_form.html"
        context = {
            "departments": departments
        }

        return render(request, template, context)

        

def employee_edit(request, employee_id):
    pass