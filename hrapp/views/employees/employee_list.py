from django.shortcuts import render, redirect, reverse
from hrapp.models import Employee
from .data_manager.get_all_employees import get_all_employees
from .data_manager.add_employee import add_employee

def employee_list(request):
    if request.method == 'GET':
        all_employees = get_all_employees()

        template = 'employees/employees_list.html'
        context = {
            'employees': all_employees
        }

        return render(request, template, context)
    elif request.method == "POST":
        form_data = request.POST
        
        add_employee(form_data)
        return redirect(reverse("hrapp:employee_list"))
