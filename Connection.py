import mysql.connector
import json

class Connection:
    def __init__(self):
        self.connect = mysql.connector.connect(
            user = 'root',
            password = '',
            host = 'localhost',
            database = 'mineria_t2_db'
        )

        self.cursor = self.connect.cursor()

    def users(self):
        info_users = []

        query = ("SELECT * FROM TBL_USERS")

        self.cursor.execute(query)

        for (user) in self.cursor:
            info_users.append({'id': user[0], 'name': user[1], 'lastname': user[2], 'username': user[3]})
        self.cursor.close()

        users_json = json.dumps(info_users)

        return users_json
    
    def users_by_username_password(self, username, password):
        info_users = []

        query = (f"SELECT USERNAME, PASSWORD FROM TBL_USERS WHERE USERNAME = '{username}' and PASSWORD = '{password}'")
        

        self.cursor.execute(query)

        for (user) in self.cursor:
            info_users.append({
                    'USERNAME': user[0],
                    'PASSWORD': user[1]
                })
        self.cursor.close()

        users_json = json.dumps(info_users)

        return users_json

    def monitors(self):
        monitors_info = []

        query = ("SELECT * FROM TBL_MONITORS")

        self.cursor.execute(query)

        for (monitor) in self.cursor:
            monitors_info.append({
                    'id': monitor[0],
                    'price': monitor[1],
                    'qualification': monitor[2],
                    'size_screen': monitor[3],
                    'max_resolution': monitor[4],
                    'brand': monitor[5],
                    'update_rate': monitor[6]
                })
            
        self.cursor.close()

        monitors_json = json.dumps(monitors_info)

        return monitors_json


#connect = Connection()

#connect.users_by_username_password(username= 'ADMIN', password= 'admin')

