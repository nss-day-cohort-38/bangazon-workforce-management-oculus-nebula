import sqlite3
from ...connection import Connection
from hrapp.models import model_factory, EmployeeComputer
def get_employee_computer(employee_id):
    with sqlite3.connect(Connection.db_path) as conn:
        conn.row_factory = model_factory(EmployeeComputer)
        # conn.row_factory = sqlite3.Row

        db_cursor = conn.cursor()

        db_cursor.execute("""
        SELECT
            ec.id,
            ec.computer_id,
            ec.employee_id,
            ec.assign_date,
            ec.unassign_date
        FROM
            hrapp_employeecomputer ec
            JOIN hrapp_employee e ON e.id = ec.employee_id
        WHERE
            e.id = 1
            AND ec.unassign_date IS NULL
        """)

        dataset = db_cursor.fetchone()

        # db_cursor.execute("""
        # SELECT
        #     *
        # FROM
        #     hrapp_trainingprogram
        # """)
        
        # em_start_dates = []
        # for row in db_cursor.fetchall():
        #     key_name = "start_date"
        #     other_key = "end_date"
        #     id = row["id"]
        #     date = "-".join([row[key_name].split("/")[2], row[key_name].split("/")[0], row[key_name].split("/")[1]])
        #     other_date = "-".join([row[other_key].split("/")[2], row[other_key].split("/")[0], row[other_key].split("/")[1]])
        #     print(date, other_date)
        #     em_start_dates.append([id, date, other_date])

        # for info in em_start_dates:
        #     db_cursor.execute("""
        #     UPDATE
        #         hrapp_trainingprogram
        #     SET
        #         start_date = ?,
        #         end_date = ?
        #     WHERE
        #         hrapp_trainingprogram.id = ?
        #  """, ( info[1], info[2], info[0]))

        return dataset


