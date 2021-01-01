import pyodbc


server = 'ispj-database.database.windows.net'
database = 'ISPJ Database'
username = 'Peter'
password = 'p@ssw0rd'
driver= '{ODBC Driver 17 for SQL Server}'
conn = pyodbc.connect('DRIVER='+driver+';SERVER='+server+';PORT=1433;DATABASE='+database+';UID='+username+';PWD='+password)

cursor = conn.cursor()

# account_status = 'Active'
# firstname = 'Darren'
# lastname = 'Kang'
# email = 'darrenkang@gmail.com'
# password = '987654321'
# isadmin = 'False'
# profile_image = '../static/images/profile.jpg'
# previous_passwords = "['123456789']"
# cursor.execute('INSERT INTO user_accounts VALUES(NULL, ?, ?, ?, ?, ?, ?, ?, ?);', account_status, firstname, lastname, email, password, isadmin, profile_image, previous_passwords)
# conn.commit()

# conn.createStatement()

# cursor.execute('select * from user_accounts')
# for row in cursor:
#     print(row)

import datetime

print(str(datetime.datetime.now())[:11])