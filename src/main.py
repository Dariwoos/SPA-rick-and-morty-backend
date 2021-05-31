"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
import os
from flask import Flask, request, jsonify, url_for
from flask_migrate import Migrate
from flask_swagger import swagger
from flask_cors import CORS
from utils import APIException, generate_sitemap
from admin import setup_admin
from models import db, User
#from models import Person

app = Flask(__name__)
app.url_map.strict_slashes = False
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DB_CONNECTION_STRING')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
MIGRATE = Migrate(app, db)
db.init_app(app)
CORS(app)
setup_admin(app)

# Handle/serialize errors like a JSON object
@app.errorhandler(APIException)
def handle_invalid_usage(error):
    return jsonify(error.to_dict()), error.status_code

# generate sitemap with all your endpoints
@app.route('/')
def sitemap():
    return generate_sitemap(app)

@app.route("/json/<int:id>", methods=["GET"])
def dataBank(id):
    data = User.query.filter_by(id=id).first()
    data_json = data.serialize()
    if data_json is not None:
        return jsonify(data_json),200
    else:
        return jsonify("not found"), 404

@app.route('/all/json', methods=['GET'])
def all_proffesionals():
        users = User.query.all()
        json_list = list(map(lambda user: user.serialize(), users))
        return jsonify(json_list), 201


@app.route('/edit/json',methods=['PUT'])
def edit_json():
    body = request.get_json()
    sender_id = body["sender_id"]
    resiver_id= body["resiver_id"]
    amount = body["amount"]
    sender = User.query.filter_by(id=sender_id).first()
    resiver = User.query.filter_by(id=resiver_id).first()
    if sender and resiver is not None:
        sender.balance = sender.balance - amount
        resiver.balance = resiver.balance + amount
        db.session.commit()
        return jsonify({"resiver":resiver.serialize(),"sender":sender.serialize()}),200
    else:
        return jsonify("data no existe"),400
    
# this only runs if `$ python src/main.py` is executed
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=False)
