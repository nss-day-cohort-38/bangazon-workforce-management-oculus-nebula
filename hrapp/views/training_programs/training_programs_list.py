import sqlite3
from django.shortcuts import render, redirect, reverse
from hrapp.models import TrainingProgram, TrainingProgramEmployee, Employee
from ..connection import Connection
from django.contrib.auth.decorators import login_required
from hrapp.models import model_factory


@login_required
def training_programs_list(request):
    if request.method == 'GET':
        with sqlite3.connect(Connection.db_path) as conn:
            conn.row_factory = model_factory(TrainingProgram)
            # conn.row_factory = create_training_program
            db_cursor = conn.cursor()
            db_cursor.execute("""
                SELECT
                    tp.id,
                    tp.title,
                    tp.start_date,
                    tp.end_date,
                    tp.capacity
                FROM hrapp_trainingprogram tp
                """)
            data = db_cursor.fetchall()

        template_name = 'training_programs/training_program_list.html'
        context = {
            'all_training_programs': data
        }
        return render(request, template_name, context)

    elif request.method == 'POST':
        form_data = request.POST
        with sqlite3.connect(Connection.db_path) as conn:
            db_cursor = conn.cursor()

            db_cursor.execute("""
            INSERT INTO hrapp_trainingprogram
            (
                title, start_date, end_date,
                capacity
            )
            VALUES (?, ?, ?, ?)
            """,
            (form_data['title'], form_data['start_date'],
                form_data['end_date'], form_data['capacity']))

        return redirect(reverse('hrapp:trainingprograms'))

# def create_training_program(cursor, row):
#     _row = sqlite3.Row(cursor, row)

#     training_program = TrainingProgram()
#     training_program.id = _row["id"]
#     training_program.title = _row["title"]
#     training_program.start_date = _row["start_date"]
#     training_program.end_date = _row["end_date"]
#     training_program.capacity = _row["capacity"]


#     training_program.employees = []

#     employee = Employee()
#     employee.id = _row["employee_id"]
#     employee.first_name= _row["first_name"]
#     employee.last_name = _row["last_name"]
#     employee.start_date = _row["start_date"]
#     employee.is_supervisor = _row["is_supervisor"]

#     return (training_program, employee,)
    # training_program.employee = employee
    # return training_program

# @login_required
# def training_programs_list(request):
#     if request.method == 'GET':
#         with sqlite3.connect(Connection.db_path) as conn:
#             conn.row_factory = create_training_program
#             # conn.row_factory = create_training_program
#             db_cursor = conn.cursor()
#             db_cursor.execute("""
#             SELECT
#               tp.id,
#               tp.title,
#               tp.start_date,
#               tp.end_date,
#               tp.capacity,
#               e.id,
#               e.first_name,
#               e.last_name,
#               e.start_date,
#               e.is_supervisor,
#               etp.employee_id,
#               etp.training_program_id
#             FROM hrapp_trainingprogramemployee etp
#             JOIN hrapp_trainingprogram tp ON tp.id = etp.training_program_id
#             JOIN hrapp_employee e ON etp.training_program_id = tp.id
#                 """)
#             data = db_cursor.fetchall()

#             all_training_programs = {}

#             for (training_program, employee) in data:
#                 if training_program.id not in all_training_programs:
#                     all_training_programs[training_program.id] = training_program
#                     all_training_programs[training_program.id].employees.append(employee)
#                 else:
#                     all_training_programs[training_program.id].employees.append(employee)

#             template = 'training_programs/training_programs_list.html'
#             context = {
#               "all_training_programs": all_training_programs.values()
#             }
#             return render(request, template, context)

    # elif request.method == 'POST':
    #     form_data = request.POST
    #     with sqlite3.connect(Connection.db_path) as conn:
    #         db_curser = conn.cursor()
    #         db_curser.execute("""
    #                 INSERT INTO hrapp_trainingprogram
    #                 (title, start_date, end_date, capacity)
    #                 VALUES (?, ?, ?, ?)
    #             """,
    #                           (form_data['title'], form_data['start_date'],
    #                            form_data['end_date'], form_data['capacity']))
    #     return redirect(reverse('hrapp:trainingprograms'))
