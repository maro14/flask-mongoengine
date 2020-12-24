from flask import Flask, request, Response
from database.models import User
from database.db import initialize_db

app = Flask(__name__)
app.config['MONGODB_SETTINGS'] = {
    'host' : 'mongodb://localhost:27017/customer.user'
}

initialize_db(app)

@app.route('/')
def hello():
    return 'welcome flask-mongoengine'


@app.route('/user', methods=["GET"])
def all_users():
    users = User.objects().to_json()
    return Response(users, mimetype='application/json', status=200)


@app.route('/user', methods=["POST"])
def add_user():
    body = request.get_json()
    user = User(**body).save()
    id = user.id
    return {'id': str(id)}, 201


if __name__ == "__main__":
    app.run(debug=True)