import sqlite3
from django.shortcuts import render, redirect
from django.urls import reverse
from hrapp.models import Department, Employee
from hrapp.models import model_factory
from ..connection import Connection

def create_department(cursor, row):
    _row = sqlite3.Row(cursor, row)
    
    department = Department()
    department.id = row["id"]
    department.department_name = row["department_name"]
    department.budget = row["budget"]
    
    department.employees = []
    
    employee = Employee()
    employee.id = row["id"]
    employee.first_name = row["first_name"]
    employee.last_name = row["last_name"]
    
    return (department, employee,)

def get_department(department_id):
    with sqlite3.connect(Connection.db_path) as conn:
        conn.row_factory = model_factory(Department)
        db_cursor = conn.cursor()

        db_cursor.execute("""
        SELECT
            d.id,
            d.department_name,
            d.budget
        FROM hrapp_department d
        WHERE d.id = ?
        """, (department_id,))

        return db_cursor.fetchone()

def department_detail(request, department_id):
    if request.method == 'GET':
        department = get_department(department_id)
        
        template = 'departments/details'
        context = {
            'department' : department
        }