from flask import Flask, jsonify
data = Flask(__name__)

@data.route('/data/users')
def users_action():
    pass