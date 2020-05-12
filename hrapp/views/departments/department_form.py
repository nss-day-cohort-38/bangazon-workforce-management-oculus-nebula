import sqlite3
from django.shortcuts import render






def department_form(request):
    if request.method == 'GET':

        template = 'departments/department_form.html'
        return render(request, template)

