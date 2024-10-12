import sqlite3

connection = sqlite3.connect("db.sl3", 5)
cur = connection.cursor()
#======CREATE=========

#cur.execute("CREATE TABLE LOGIN (name TEXT, password TEXT);")
#connection.commit()

#======INSERT======

'''user = input("Username  : ")
passw = input("Password : ")
cur.execute(f"INSERT INTO LOGIN (name, password) VALUES ('{user}','{passw}');")
connection.commit()'''

#=======SELECT=========

#user = input('Username  : ')
#cur.execute(f"SELECT rowid, name FROM USERS WHERE name='{user}'")
#cur.execute(f"SELECT rowid, name FROM USERS")
#connection.commit()


#res = cur.fetchall()
#print(res)

'''if len(res) == 0:
    print("User not found!")
else:
    print(res[0][1])'''

#======UPDATE=========

#cur.execute(f"UPDATE USERS SET name='Katerina' WHERE rowid=2")
#connection.commit()


#======DELETE========

#cur.execute(f"DELETE FROM USERS WHERE rowid=2")
#connection.commit()

while True:
    varik = input('Увійти/зареєструватися в аккаунт (1/2): ')

    if varik == '1':
#=========VHOD=========

        login = input('LOGIN       : ')


        cur.execute(f"SELECT rowid, name FROM LOGIN WHERE name='{login}'")
        connection.commit()
        res = cur.fetchall()

        if len(res) != 0:
            id_1 = res[0][0]
            password = input('PASSWORD : ')
            cur.execute(f"SELECT rowid, name FROM LOGIN WHERE password='{password}'")
            connection.commit()
            res = cur.fetchall()
            if len(res) != 0:
                id_2 = res[0][0]
                if id_1 == id_2:
                    print('Ви вошлі в аккаунт!')
                    break
                else:
                    print('Пароль невірний')
            else:
                print('Пароль невірний')

        else:
            print('Логін не вірний ')
    elif varik == '2':

# ======REGISTER========
        login = input('LOGIN       : ')

        cur.execute(f"SELECT rowid, name FROM LOGIN WHERE name='{login}'")
        connection.commit()
        res = cur.fetchall()
        if len(res) != 0:
            print('Такий логін вже є')
        else:
            password = input('PASSWORD : ')
            cur.execute(f"INSERT INTO LOGIN (name, password) VALUES ('{login}','{password}');")
            connection.commit()
            print('Ви створили обліковий запис!')
            break


    varik = 0

connection.close()








