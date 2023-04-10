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
            info_users.append({
                    'id': user[0], 
                    'name': user[1], 
                    'lastname': user[2], 
                    'username': user[3]
                })
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

    def user_insert(self, name, lastname, username, password):
        query = (
            "INSERT INTO tbl_users (name, lastname, username, password) "+
            f"VALUES ('{name}', '{lastname}', '{username}', '{password}')"
        )

        self.cursor.execute(query)
        self.connect.commit()
        self.cursor.close()

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

    def monitor_insert(self, price, qualification, size_screen, max_resolution, brand, update_rate):
        query = (
            "INSERT INTO TBL_MONITORS (price, qualification, size_screen, max_resolution, brand, update_rate) "+
            f"VALUES ('{price}', '{qualification}', '{size_screen}', '{max_resolution}', '{brand}', '{update_rate}')"
        )

        self.cursor.execute(query)
        self.connect.commit()
        self.cursor.close()

    def monitor_delete(self, id):
        query = (
            f"DELETE FROM TBL_MONITORS WHERE id_monitor = '{id}'"
        )

        self.cursor.execute(query)
        self.connect.commit()
        self.cursor.close()

    def monitor_update(self, id, price, qualification, size_screen, max_resolution, brand, update_rate):
        query = (
            "UPDATE TBL_MONITORS "+
            f"SET price = '{price}', qualification = '{qualification}', size_screen = '{size_screen}', max_resolution = '{max_resolution}', brand = '{brand}', update_rate = '{update_rate}' "+ 
            f"WHERE id_monitor = '{id}'"
        )

        self.cursor.execute(query)
        self.connect.commit()
        self.cursor.close()

    def monitors_more_selling(self):
        monitors_info = []

        query = (
            "SELECT brand, COUNT(*) as count "+
            "FROM tbl_monitors "+
            "GROUP BY brand "+
            "ORDER BY count DESC "+
            "LIMIT 1"
        )

        self.cursor.execute(query)

        for (monitor) in self.cursor:
            monitors_info.append({
                    'brand': monitor[0],
                    'count': monitor[1]
                })
            
        self.cursor.close()

        monitors_json = json.dumps(monitors_info)
        print(monitors_info)
        return monitors_json
    
    def monitor_high_qualification(self):
        monitors_info = []

        query = (
            "SELECT MAX(qualification) as max_qualification "+
            "FROM tbl_monitors"
        )

        self.cursor.execute(query)

        for (monitor) in self.cursor:
            monitors_info.append({
                    'qualification': monitor[0]
                })
            
        self.cursor.close()

        monitors_json = json.dumps(monitors_info)

        return monitors_json
    
    def monitors_all_records(self):
        monitors_info = []

        query = (
            "SELECT COUNT(*) as total_records "+
            "FROM tbl_monitors"
        )

        self.cursor.execute(query)

        for (monitor) in self.cursor:
            monitors_info.append({
                    'count': monitor[0]
                })
            
        self.cursor.close()

        monitors_json = json.dumps(monitors_info)

        return monitors_json
    
    def monitors_sum_values(self):
        monitors_info = []

        query = (
            "SELECT SUM(price) as total_price "+
            "FROM tbl_monitors"
        )

        self.cursor.execute(query)

        for (monitor) in self.cursor:
            monitors_info.append({
                    'sum_price': monitor[0]
                })
            
        self.cursor.close()

        monitors_json = json.dumps(monitors_info)

        return monitors_json
    
    def monitors_all_brands(self):
        monitors_info = []

        query = (
            "SELECT DISTINCT brand "+
            "FROM tbl_monitors "+
            "ORDER BY brand ASC"
        )

        self.cursor.execute(query)

        for (monitor) in self.cursor:
            monitors_info.append({
                    'brand': monitor[0]
                })
            
        self.cursor.close()

        monitors_json = json.dumps(monitors_info)

        return monitors_json
    
    def monitors_sell_by_brand(self):
        monitors_info = []

        query = (
            "SELECT brand, COUNT(*) as count "+
            "FROM tbl_monitors "+
            "GROUP BY brand"
        )

        self.cursor.execute(query)

        for (monitor) in self.cursor:
            monitors_info.append({
                    'brand': monitor[0],
                    'count': monitor[1]
                })
            
        self.cursor.close()

        monitors_json = json.dumps(monitors_info)

        return monitors_json
    
    def monitors_3_best_brands(self):
        monitors_info = []

        query = (
            "SELECT brand, COUNT(*) as count  "+
            "FROM tbl_monitors  "+
            "GROUP BY brand  "+
            "ORDER BY count DESC  "+
            "LIMIT 3"
        )

        self.cursor.execute(query)

        for (monitor) in self.cursor:
            monitors_info.append({
                    'brand': monitor[0],
                    'count': monitor[1]
                })
            
        self.cursor.close()

        monitors_json = json.dumps(monitors_info)

        return monitors_json
    
    def monitors_price_3_best_brands(self):
        monitors_info = []

        query = (
            "SELECT m.brand, GROUP_CONCAT(m.price ORDER BY m.price ASC SEPARATOR ', ') AS prices "+
            "FROM tbl_monitors m "+
            "INNER JOIN ( "+
                "SELECT brand, COUNT(*) AS count "+
                "FROM tbl_monitors "+
                "GROUP BY brand "+
               "ORDER BY count DESC "+
                "LIMIT 3 "+
            ") b ON m.brand = b.brand "+
            "GROUP BY m.brand"
        )

        self.cursor.execute(query)

        for (monitor) in self.cursor:
            monitors_info.append({
                    'brand': monitor[0],
                    'prices': self.convert_to_list(monitor[1])
                })
            
        self.cursor.close()

        monitors_json = json.dumps(monitors_info)
        print(monitors_info)
        return monitors_json
    
    def monitors_price_x_size(self):
        monitors_info = []

        query = (
            "SELECT size_screen, GROUP_CONCAT(price SEPARATOR ', ') AS prices "+
            "FROM tbl_monitors "+
            "GROUP BY size_screen "+
            "ORDER BY size_screen"
        )

        self.cursor.execute(query)

        for (monitor) in self.cursor:
            monitors_info.append({
                    'size_screen': monitor[0],
                    'prices': self.convert_to_list(monitor[1])
                })
            
        self.cursor.close()

        monitors_json = json.dumps(monitors_info)

        return monitors_json
    
    def monitors_update_rate(self):
        monitors_info = []

        query = (
            "SELECT update_rate, COUNT(*) AS cantidad "+
            "FROM tbl_monitors "+
            "GROUP BY update_rate"
        )

        self.cursor.execute(query)

        for (monitor) in self.cursor:
            monitors_info.append({
                    'update_rate': monitor[0],
                    'count': monitor[1]
                })
            
        self.cursor.close()

        monitors_json = json.dumps(monitors_info)

        return monitors_json
    
    def convert_to_list(self, data):
        list = data.split(",")
        return list

#connect = Connection()

#connect.monitors_price_3_best_brands()

