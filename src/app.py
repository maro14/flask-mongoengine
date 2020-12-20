from flask import Flask, request, Response
from database.models import User
from database.db import initialize_db

app = Flask(__name__)
app.config['MONGODB_SETTINGS'] = {
    'host' : 'mongodb://localhost:27017/customer'
}

initialize_db(app)

@app.route('/')
def hello():
    return 'hello'

@app.route('/user', methods=["GET"])
def all_users():
    users = User.objects().to_json()
    return Response(users, mimetype='application/json', status=200)



if __name__ == "__main__":
    app.run()