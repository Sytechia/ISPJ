import random
import pyodbc
from flask import Flask, session
server = "ispj-database.database.windows.net"
database = "ISPJ Database"
username = "Peter"
password = "p@ssw0rd"
driver= "{ODBC Driver 17 for SQL Server}"
conn = pyodbc.connect("DRIVER="+driver+";SERVER="+server+";PORT=1433;DATABASE="+database+";UID="+username+";PWD="+password)

cursor = conn.cursor()

# cursor.execute('DELETE FROM user_accounts WHERE fullname=?',"Marcus")
# conn.commit()

# account_status = 1
# firstname = "Darren Kang"
# email = "darrenkang@gmail.com"
# password = "987654321"
# isadmin = "False"
# profile_image = "../static/images/profile.jpg"
# previous_passwords = "["123456789"]"
# query = "INSERT INTO user_accounts VALUES(?, ?, ?, ?, ?, ?, ?, ?);"


""" Inserting into database """
# constructAndExecuteQuery(query, random.randint(100000, 999999), 1, email, password, isadmin, profile_image, previous_passwords, fullname)

# def query(query, *args):
#     try:
#         cursor.execute(query, *args)
#         result = cursor.fetchall()
#     except: 
#         result = []
#     return result
# strip_address = '528 bishan road'
# result = query('SELECT * FROM Addresses WHERE user_id=? AND address=?', '2037560', strip_address)
# print(result)

def constructAndExecuteQuery(query, *args):
    cursor.execute(query, *args)
    conn.commit()

"""Deleting user from database"""
# cursor.execute("DELETE FROM user_accounts WHERE Id = 349568")
    
# email = "MarcusWang@gmail.com"
# li = query("SELECT Id FROM user_accounts WHERE email = ?", email)[0][0]
# print(li)
# query = "INSERT INTO prev_transactions VALUES(?, ?, ?, ?, ?, ?);"
# constructAndExecuteQuery(query, 1, "[game1, game2, game3]", random.randint(100000, 999999), "2017-06-15", "awaiting order", 203756)
# user = query("SELECT * FROM user WHERE user_id = ?", session["user_id"])


# user = query("SELECT * FROM user WHERE user_id = ?", session["user_id"])

# user = query("SELECT * FROM user_accounts WHERE email = ?", email)
# user_id = user[0][0]
# user_active = user[0][1]
# user_email = user[0][2]
# user_password = user[0][3]
# user_isAdmin = user[0][4]
# user_pic = user[0][5]
# user_passwords = user[0][6]
# user_name = user[0][7]

# print(user)
# print(user_id)
# print(user_active)
# print(type(user_active))
# print(user_email)
# print(user_password)
# print(user_isAdmin)
# print(user_pic)
# print(user_passwords)
# print(user_name)

import datetime



# query = "INSERT INTO prev_transactions VALUES(?,?,?,?,?,?)"

# constructAndExecuteQuery(query,2, '[("Hades",22,1,"https://upload.wikimedia.org/wikipedia/en/c/cc/Hades_cover_art.jpg"), ("GTA V",41,2,"https://upload.wikimedia.org/wikipedia/en/thumb/a/a5/Grand_Theft_Auto_V.png/220px-Grand_Theft_Auto_V.png"), ("Phasmophobia",14,3,"https://upload.wikimedia.org/wikipedia/en/thumb/f/f2/Phasmophobia_VG.jpg/330px-Phasmophobia_VG.jpg")]',random.randint(100000,999999),str(datetime.datetime.now())[:11],"Awaiting Order","895904")
# constructAndExecuteQuery(query,3,'[("Resident Evil 3", 20, 2, "https://upload.wikimedia.org/wikipedia/en/d/dc/Resident_Evil_3.jpg"), ("The Last of Us Part II", 30, 1, "https://upload.wikimedia.org/wikipedia/en/4/4f/TLOU_P2_Box_Art_2.png")]',random.randint(100000,999999),str(datetime.datetime.now())[:11], "Awaiting Order", "895904")
# cursor.execute("SELECT * FROM prev_transactions WHERE fk_user_id=?", "895904")
# for row in cursor.fetchall():
#     print(row)
# cursor.execute("DELETE FROM prev_transactions")
# conn.commit()
# cursor.execute("SELECT * FROM Addresses")
# for row in cursor.fetchall():
#     print(row)


# items = '[("Hades",22,1,"https://upload.wikimedia.org/wikipedia/en/c/cc/Hades_cover_art.jpg"), ("GTA V",41,2,"https://upload.wikimedia.org/wikipedia/en/thumb/a/a5/Grand_Theft_Auto_V.png/220px-Grand_Theft_Auto_V.png"), ("Phasmophobia",14,3,"https://upload.wikimedia.org/wikipedia/en/thumb/f/f2/Phasmophobia_VG.jpg/330px-Phasmophobia_VG.jpg")]'

# from functools import reduce 
import ast

# total = 0

# for y in ast.literal_eval(items):
#     total += (y[1] * y[2])

# print(total)

# prev_transactions = query('SELECT * FROM prev_transactions WHERE fk_user_id=?', 203756)
# transactions = []
# for y in prev_transactions:
#     total = 0
#     for z in ast.literal_eval(y[1]):
#         total += (z[1] * z[2])
#     transactions.append([(y[2], str(y[3]),y[4], y[1], total)])
# print(transactions)

constructAndExecuteQuery('INSERT INTO cart VALUES(?,?,?,?,?,?)',1,1,)