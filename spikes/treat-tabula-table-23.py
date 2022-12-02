#import sqlite3 as sql3
#
#conection = sql3.connect("spikes/vestunb_23.db")
#cursor =conection.cursor()
#cursor.execute("DROP TABLE vest_2023")
#cursor.execute("""CREATE TABLE vest_2023(
#    Curso varchar(200),
#    Vagas_Universais int,
#    Vagas_Deficientes int,
#    Total int
#);""")

import mysql.connector

connection = mysql.connector.connect(
    host="localhost"
    password=""
)