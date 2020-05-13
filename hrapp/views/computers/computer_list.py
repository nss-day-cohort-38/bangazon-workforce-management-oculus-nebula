import sqlite3
import datetime
from django.shortcuts import render ,redirect
from django.urls import reverse
from hrapp.models import Computer, model_factory, EmployeeComputer
from ..connection import Connection

def computer_list(request):

    #This is just a function to get all the computers and verifies that it is a fet method
    if request.method == "GET":
        with sqlite3.connect(Connection.db_path) as conn:
            conn.row_factory = model_factory(Computer)
            db_cursor = conn.cursor()
            #fetch the table computers from the DB
            db_cursor.execute("""
               SELECT
                c.id,
                c.make,
                c.manufacturer
                from hrapp_computer c
            """)
            #Place the rows into readabel format and fetch them 
            all_computers = db_cursor.fetchall()
            
        #supply the correct information for the render function 1. the location of the html and 2. the info it needs.
        template = 'computers/computer_list.html'

        context = {
            'computers': all_computers
        }
        return render(request, template, context)
    #check if it is  post method coming in
    elif request.method == "POST":
        #this form_data grabs the needed info from the computer_form.html page and gets ready to appropriate it to sqlite3
        form_data = request.POST
        #connect to that sweet database
        with sqlite3.connect(Connection.db_path) as conn:
            conn.row_factory = model_factory(Computer)
            db_cursor = conn.cursor()
            now = datetime.datetime.now()
            assigned_date = now.strftime("%Y-%m-%d")
            
            

            #get the correct information from the db
            db_cursor.execute("""
                INSERT into hrapp_computer (manufacturer, make, purchase_date)
                values ( ?, ? , ?)
            """, (
                #fetch the information by name or by id
                form_data['manufacturer'], form_data['make'], form_data['purchase_date']
            ))
            if form_data["employee"] != "Not Assigned":
                conn.row_factory = model_factory(EmployeeComputer)
                db_cursor = conn.cursor()
                computer = get_last_computer()
                db_cursor.execute("""
                    INSERT into hrapp_employeecomputer (computer_id, employee_id, assign_date, unassign_date)
                    values(?,?,?, null)

                """, (
                    (computer.id+1), form_data['employee'], assigned_date
                ))

            #send the user back to the master list with the updated computer
            return redirect(reverse('hrapp:computers'))



def get_last_computer():
    with sqlite3.connect(Connection.db_path) as conn:
        conn.row_factory = model_factory(Computer)
        db_cursor = conn.cursor()

        db_cursor.execute("""
            SELECT *
            from hrapp_computer c
        """)

        data= db_cursor.fetchall()[-1]

        return data
    