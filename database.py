import sqlite3

def create_database_and_table():
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()
    request ='''CREATE TABLE IF NOT EXISTS active_users(
                            user_name TEXT,
                            ip TEXT,
                            port INT
                            )'''
    cursor.execute(request)
    conn.close()

def insert_user(user_name, ip, port):
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()
    a = '''
        INSERT INTO active_users(user_name, ip, port)            
        VALUES(?,?,?)
        '''
    cursor.execute(a, (user_name, ip, port))
    conn.commit()
    conn.close()


def delete_user(ip):
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()
    a = '''DELETE FROM active_users
            WHERE ip = ?'''
    cursor.execute(a, (ip,))
    conn.commit()
    conn.close()


def check_username(name):
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()
    run = True

    while run:
        cursor.execute("select user_name from active_users where user_name=?", (name,))
        data = cursor.fetchall()
        if data: # Le nom existe, return False
            print("indisponible")
            return False
        else : # Le nom n'existe pas en base de données, return True
            print("disponible")
            run = False
            return True

    conn.close()

def delete_table(name_of_table):
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()
    cursor.execute("DELETE FROM active_users")
    conn.commit()
    conn.close()