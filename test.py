import random
import pyodbc
from flask import Flask, session
server = 'ispj-database.database.windows.net'
database = 'ISPJ Database'
username = 'Peter'
password = 'p@ssw0rd'
driver= '{ODBC Driver 17 for SQL Server}'
conn = pyodbc.connect('DRIVER='+driver+';SERVER='+server+';PORT=1433;DATABASE='+database+';UID='+username+';PWD='+password)

cursor = conn.cursor()

account_status = 1
firstname = 'Darren Kang'
email = 'darrenkang@gmail.com'
password = '987654321'
isadmin = 'False'
profile_image = '../static/images/profile.jpg'
previous_passwords = "['123456789']"
query = 'INSERT INTO user_accounts VALUES(?, ?, ?, ?, ?, ?, ?, ?);'


""" Inserting into database """
# constructAndExecuteQuery(query, random.randint(100000, 999999), 1, email, password, isadmin, profile_image, previous_passwords, fullname)

def query(query, *args):
    try:
        cursor.execute(query, *args)
        result = cursor.fetchall()
    except: 
        result = []
    return result

"""Deleting user from database"""
# cursor.execute('DELETE FROM user_accounts WHERE Id = 349568')
    
email = 'MarcusWang@gmail.com'
# li = query('SELECT Id FROM user_accounts WHERE email = ?', email)[0][0]
# print(li)




# user = query("SELECT * FROM user WHERE user_id = ?", session['user_id'])

# user = query('SELECT * FROM user_accounts WHERE email = ?', email)
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

