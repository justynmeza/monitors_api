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
    
    
    @data.route('/data/monitors/selling')
    def monitors_more_selling_action():
        connect = Connection()
        monitors = connect.monitors_more_selling()

        print(monitors)
        return(monitors)
    
    @data.route('/data/monitors/high-qualification')
    def monitors_high_qualification_action():
        connect = Connection()
        monitors = connect.monitor_high_qualification()

        print(monitors)
        return(monitors)
    
    @data.route('/data/monitors/all-records')
    def monitors_all_records_action():
        connect = Connection()
        monitors = connect.monitors_all_records()

        print(monitors)
        return(monitors)
    
    @data.route('/data/monitors/sum-values')
    def monitors_sum_values_action():
        connect = Connection()
        monitors = connect.monitors_sum_values()

        print(monitors)
        return(monitors)
    
    @data.route('/data/monitors/all-brands')
    def monitors_all_brands_action():
        connect = Connection()
        monitors = connect.monitors_all_brands()

        print(monitors)
        return(monitors)
    
    @data.route('/data/monitors/sell-by-brand')
    def monitors_sell_by_brand_action():
        connect = Connection()
        monitors = connect.monitors_sell_by_brand()

        print(monitors)
        return(monitors)
    
    @data.route('/data/monitors/best-brands')
    def monitors_3_best_brands_action():
        connect = Connection()
        monitors = connect.monitors_3_best_brands()

        print(monitors)
        return(monitors)
    
    @data.route('/data/monitors/price-best-brands')
    def monitors_price_3_best_brands_action():
        connect = Connection()
        monitors = connect.monitors_price_3_best_brands()

        print(monitors)
        return(monitors)
    
    @data.route('/data/monitors/price-x-size')
    def monitors_price_x_size_action():
        connect = Connection()
        monitors = connect.monitors_price_x_size()

        print(monitors)
        return(monitors)


    @data.route('/data/monitors/update-rate')
    def monitors_update_rate_action():
        connect = Connection()
        monitors = connect.monitors_update_rate()

        print(monitors)
        return(monitors)


    data.run(debug=True)

Main()

