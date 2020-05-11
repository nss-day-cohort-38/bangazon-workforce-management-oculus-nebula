import sqlite3
from ...connection import Connection

def get_all_employees():
    with sqlite3.connect(Connection.db_path) as conn:
            conn.row_factory = sqlite3.Row
            db_cursor = conn.cursor()

            '''
            Joins employee table with department table
            returns
            - Employee Id
            - Employee First Name
            - Employee Last Name
            - Employee Start Date
            - Employee is supervisor
            - Employee Department
            '''

            db_cursor.execute("""
                SELECT
                    e.id,
                    e.first_name,
                    e.last_name,
                    e.start_date,
                    e.is_supervisor,
                    d.id department_id
                FROM
                    hrapp_employee e
                JOIN hrapp_department d ON
                    d.id = e.department_id
            """)

            return db_cursor.fetchall()