import mysql.connector
conn = mysql.connector.connect(
    host="103.69.196.66",
    user="dba",
    password="Pass123$",
    database="RAMS")

cursor = conn.cursor()

sql = '''SELECT time_stamp from tbl_machine_data_last_log'''

cursor.execute(sql)

result = cursor.fetchone();
print(result)

result = cursor.fetchall();
print(result)

conn.close()