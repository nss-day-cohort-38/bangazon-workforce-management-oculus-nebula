import sqlite3
from django.urls import reverse
from django.shortcuts import redirect, render
from hrapp.models import Employee, Computer, model_factory
from ..connection import Connection
from django import forms

def get_employees():
    ''' 
        This function is just to fetch all the employees and return it so we can populate a dropdown menu based off it.
    '''
    with sqlite3.connect(Connection.db_path) as conn:
        conn.row_factory = model_factory(Employee)
        db_cursor = conn.cursor()

        db_cursor.execute('''
         select 
            e.first_name,
            e.last_name,
            e.id,
            e.is_supervisor
            from hrapp_employee e;
        ''')

        return db_cursor.fetchall()


def computer_form(request):
    if request.method == "GET":
        employees = get_employees()
        template = 'computers/computer_form.html'
        context = {
            'employees': employees
        }

        return render(request, template, context)