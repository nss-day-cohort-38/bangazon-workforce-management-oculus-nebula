from django.shortcuts import render

def employee_add(request):
    if request.method == "GET":
        template = "employees/employee_form.html";
        context = {}

        return render(request, template, context)

        

def employee_edit(request, employee_id):
    pass