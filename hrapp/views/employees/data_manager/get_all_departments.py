import sqlite3
from ...connection import Connection
from hrapp.models import model_factory, Department

def get_all_departments():
    with sqlite3.connect(Connection.db_path) as conn:
        conn.row_factory = model_factory(Department)
        db_cursor = conn.cursor()

        db_cursor.execute("""
            SELECT
                *
            FROM
                hrapp_department
        """)

        return db_cursor.fetchall()