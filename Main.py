from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin
from Connection import Connection

class Main():
    data = Flask(__name__)
    CORS(data, resources={r"/*": {"origins": "*"}})

    #GET
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
    

    #POST
    @data.route('/data/monitors', methods=['POST'])
    def monitor_insert_action():
        try:
            price = request.json['price']
            qualification = request.json['qualification']
            size_screen = request.json['size_screen']
            max_resolution = request.json['max_resolution']
            brand = request.json['brand']
            update_rate = request.json['update_rate']

            connect = Connection()
            connect.monitor_insert(price=price, qualification=qualification, size_screen=size_screen, max_resolution=max_resolution, brand=brand, update_rate=update_rate)

            return jsonify({'messaje': 'input successfully'})
        except Exception as ex:
            return jsonify({'messaje': 'Error'})

    @data.route('/data/users', methods=['POST'])
    def user_insert_action():
        try:
            name = request.json['name']
            lastname = request.json['lastname']
            username = request.json['username']
            password = request.json['password']

            connect = Connection()
            connect.user_insert(name=name, lastname=lastname, username=username, password=password)

            return jsonify({'messaje': 'input successfully'})
        except Exception as ex:
            return jsonify({'messaje': 'Error'})
        
    #UPDATE
    
    @data.route('/data/monitors/<id>', methods=['PUT'])
    def monitors_update_action(id):
        try:
            price = request.json['price']
            qualification = request.json['qualification']
            size_screen = request.json['size_screen']
            max_resolution = request.json['max_resolution']
            brand = request.json['brand']
            update_rate = request.json['update_rate']

            connect = Connection()
            connect.monitor_update(id=id, price=price, qualification=qualification, size_screen=size_screen, max_resolution=max_resolution, brand=brand, update_rate=update_rate)

            return jsonify({'messaje': 'update successfully'})
        except Exception as ex:
            return jsonify({'messaje': 'Error'})
        

    @data.route('/data/monitors/<id>', methods=['DELETE'])
    def monitors_delete_action(id):
        try:
            connect = Connection()
            connect.monitor_delete(id=id)

            return jsonify({'messaje': 'delete successfully'})
        except Exception as ex:
            return jsonify({'messaje': 'Error'})

    data.run(debug=True)

Main()

