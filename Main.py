from flask import Flask, jsonify
from Connection import Connection

class Main():
    data = Flask(__name__)

    @data.route('/data/users')
    def users_action():
        connect = Connection()
        users = connect.users()
        
        print(users)
        return users
    
    

    @data.route('/data/monitors')
    def monitors_action():
        connect = Connection()
        monitors = connect.monitors()

        print(monitors)
        return(monitors)
    
    
        

    data.run(debug=True)


Main()

