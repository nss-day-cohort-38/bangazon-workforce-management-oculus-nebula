import sqlite3
from django.shortcuts import render
from hrapp.models import Computer, model_factory
from ..connection import Connection

def computer_list(request):
    if request.method == "GET":
        with sqlite3.connect(Connection.db_path) as conn:
            conn.row_factory = model_factory(Computer)
            db_cursor = conn.cursor()

            db_cursor.execute("""
                SELECT
                c.id,
                c.make,
                c.manufacturer,
                c.assign_date,
                e.first_name,
                e.last_name
                from hrapp_computer c
                join hrapp_employeecomputer ec on ec.computer_id = c.id
                join hrapp_employee e on ec.employee_id = e.id;
            """)