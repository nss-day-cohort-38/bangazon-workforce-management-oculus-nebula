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
            (title, start_date, end_date, capacity
            )
            VALUES (?, ?, ?, ?)
            """,
                (form_data['title'], form_data['start_date'],
                    form_data['end_date'], form_data['capacity']))
        return redirect(reverse('hrapp:trainingprograms'))


def get_count(training_program_id):
    with sqlite3.connect(Connection.db_path) as conn:
        db_cursor = conn.cursor()
        db_cursor.execute("""
                SELECT COUNT(training_program_id)
                FROM hrapp_trainingprogramemployee
                WHERE training_program_id = ?
            """, (training_program_id,))
        return db_cursor.fetchone()


def list_count(request, training_program_id):
    if request.method == 'GET':
        get_count = get_count(training_program_id)
        template = 'training_programs/training_program_list.html'
        context = {
            "list_count": get_count
        }
        return render(request, template, context)
