from flask import Flask
from Connection import Connection

class Main():
    data = Flask(__name__)

    @data.route('/data/users')
    def users_action():
        connect = Connection()
        users = connect.users()

        print(users)
        return users
    
    @data.route('/data/users/<username>/<password>')
    def users_by_u_p(username, password):
        connect = Connection()
        users = connect.users_by_username_password(username=username, password=password)

        print(users)
        return users

    @data.route('/data/monitors')
    def monitors_action():
        connect = Connection()
        monitors = connect.monitors()

        print(monitors)
        return(monitors)
    
    '''
    @data.route('/data/monitors/selling')
    def monitors_more_selling_action():
        connect = Connection()
        monitors = connect.monitors_more_selling()

        print(monitors)
        return(monitors)
    '''

Main()

