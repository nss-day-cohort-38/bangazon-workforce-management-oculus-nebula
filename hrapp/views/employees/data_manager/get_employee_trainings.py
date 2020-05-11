import sqlite3
from ...connection import Connection
from hrapp.models import model_factory, TrainingProgramEmployee
def get_employee_training(employee_id):
    with sqlite3.connect(Connection.db_path) as conn:
        conn.row_factory = model_factory(TrainingProgramEmployee)

        db_cursor = conn.cursor()

        db_cursor.execute("""
        SELECT
            *
        FROM
            hrapp_trainingprogramemployee te
        WHERE
            te.employee_id = ?
        """, (employee_id, ))

        dataset = db_cursor.fetchall()

        return dataset


