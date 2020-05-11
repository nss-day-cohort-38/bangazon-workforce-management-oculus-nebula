import sqlite3
from ...connection import Connection
from hrapp.models import model_factory, EmployeeComputer
def get_employee_computers(employee_id):
    """
    This function gets all of the active computers a user has from hrapp_employeecomputer
    """
    with sqlite3.connect(Connection.db_path) as conn:
        conn.row_factory = model_factory(EmployeeComputer)

        db_cursor = conn.cursor()

        db_cursor.execute("""
        SELECT
            *
        FROM
            hrapp_employeecomputer ec
        WHERE
            ec.employee_id = ?
            AND ec.unassign_date IS NULL
        """, (employee_id, ))

        dataset = db_cursor.fetchall()
        
        return dataset


