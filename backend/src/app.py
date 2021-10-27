
from flask import Flask, request, jsonify
from flask_pymongo import PyMongo, ObjectId
from flask_cors import CORS


app = Flask(__name__)
app.config['MONGO_URI']='mongodb://localhost/mibasededatos'
mongo = PyMongo(app)


CORS(app)

db = mongo.db.users

'''@app.route('/')
def index():
    return '<h1>received</h1>' '''


@app.route('/users', methods=['POST'])
def createUser():
    id = db.insert({
        'name' : request.json['name'],
        'email' : request.json['email'],
        'password' : request.json['password']
    })
    return jsonify(str(ObjectId(id)))
    

@app.route('/users', methods=['GET'])
def getUsers():
    users = []
    for user in db.find():
        users.append({
            '_id' : str(ObjectId(user['_id'])),
            'name' : user['name'],
            'email' : user['email'],
            'password' : user['password']
        })
    return jsonify(users)

@app.route('/user/<id>', methods=['GET'])
def getUser(id):
    user = db.find_one({'_id' : ObjectId(id)})
    return jsonify({
        '_id' : str(ObjectId(user['_id'])),
        'name' : user['name'],
        'email' : user['email'],
        'password' : user['password']
    })

@app.route('/users/<id>', methods=['DELETE'])
def deleteUser(id):
    db.delete_one({'_id' : ObjectId(id)})
    return jsonify({'msg' : 'User Deleted'})


@app.route('/users/<id>', methods=['PUT'])
def updateUser(id):
    db.update_one({'_id' : ObjectId(id)}, {'$set': {
        'name' : request.json['name'],
        'email' : request.json['email'],
        'password' : request.json['password']
    }})
    return jsonify({'msg' : 'User Updated'}) 


if __name__ == "__main__":
    app.run(debug=True)


