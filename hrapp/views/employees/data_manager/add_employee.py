import sqlite3
from ...connection import Connection


def add_employee(form_data):
    """
    This function adds an employee to the hrapp_employee table
    """
    with sqlite3.connect(Connection.db_path) as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        # Got rid of join
        print(form_data)
        db_cursor.execute("""
                INSERT INTO hrapp_employee (first_name, last_name, start_date, is_supervisor, department_id)
                VALUES (?, ?, ?, ?, ?)
            """,
                          (form_data["first_name"],
                           form_data["last_name"],
                           form_data["start_date"],
                           form_data["is_supervisor"],
                           form_data["department"]
                           )
                          )

