from flask import Flask, jsonify
app = Flask(__name__)

@app.route('/app/users')
def users_action():
    pass