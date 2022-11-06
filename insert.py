import mysql.connector

mydb = mysql.connector.connect(
  host="103.69.196.66",
  user="dba",
  password="Pass123$",
  database="RAMS"
)

mycursor = mydb.cursor()

sql = "INSERT INTO tbl_machine_data_last_log (fk_machine_id, time_stamp) VALUES(%s, %s)"
val = ("7", "12345")
mycursor.execute(sql, val)

mydb.commit()

print(mycursor.rowcount, "record inserted.")