import mysql.connector

mydb = mysql.connector.connect(
    host="103.69.196.66",
    user="dba",
    password="Pass123$",
    database="RAMS"
)

mycursor = mydb.cursor()

sql = "UPDATE tbl_machine_data_last_log SET time_stamp = '123' WHERE fk_machine_id='7'"

mycursor.execute(sql)

mydb.commit()

print(mycursor.rowcount, "record(s) affected")