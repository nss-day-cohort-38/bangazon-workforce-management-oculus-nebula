import sqlite3
from django.shortcuts import render ,redirect
from django.urls import reverse
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
                c.manufacturer
                from hrapp_computer c
            """)

            all_computers = db_cursor.fetchall()

        template = 'computers/computer_list.html'

        context = {
            'computers': all_computers
        }
        return render(request, template, context)
    
    elif request.method == "POST":
        form_data = request.POST

        with sqlite3.connect(Connection.db_path) as conn:
            conn.row_factory = model_factory(Computer)
            db_cursor = conn.cursor()

            db_cursor.execute("""
                INSERT into hrapp_computer (manufacturer, make, purchase_date)
                values ( ?, ? , ?)
            """, (
                form_data['manufacturer'], form_data['make'], form_data['purchase_date']
            ))

            return redirect(reverse('hrapp:computers'))
    