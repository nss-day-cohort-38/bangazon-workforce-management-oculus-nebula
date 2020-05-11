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