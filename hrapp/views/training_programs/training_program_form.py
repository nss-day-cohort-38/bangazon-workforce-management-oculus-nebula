import sqlite3
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from hrapp.models import TrainingProgram
from hrapp.models import model_factory
from ..connection import Connection



def get_training_program(training_program_id):
    with sqlite3.connect(Connection.db_path) as conn:
        conn.row_factory = model_factory(TrainingProgram)
        db_cursor = conn.cursor()
        db_cursor.execute("""
            SELECT
                tp.id,
                tp.title,
                tp.start_date,
                tp.end_date,
                tp.capacity
            FROM hrapp_trainingprogram tp
            WHERE tp.id = ?
            """ , (training_program_id))
        return db_cursor.fetchone()

def get_training_programs():
    with sqlite3.connect(Connection.db_path) as conn:
        conn.row_factory = model_factory(TrainingProgram)
        db_cursor = conn.cursor()
        db_cursor.execute("""
            SELECT
                tp.id,
                tp.title,
                tp.start_date,
                tp.end_date,
                tp.capacity
            FROM hrapp_trainingprogram tp
            """ )
        return db_cursor.fetchall()



@login_required
def training_program_form(request):
    if request.method == 'GET':
        training_programs = get_training_programs()
        template = "training_programs/training_program_form.html"
        context = {
            "training_programs": training_programs
        }
        return render(request, template, context)

# @login_required
# def training_program_edit_form(request, training_program_id):
