# flask imports
import uuid
import random
import string
import hashlib
from flask import Flask, request, jsonify, make_response
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash

# imports for PyJWT authentication
from datetime import datetime, timedelta
from functools import wraps
from settings import DATABASE


app = Flask(__name__)
# ---------------- configuration ----------------
# database name
app.config['SQLALCHEMY_DATABASE_URI'] = f'mysql://{DATABASE["user"]}:{DATABASE["password"]}@{DATABASE["host"]}/{DATABASE["db"]}'

# creates SQLALCHEMY object
db = SQLAlchemy(app)


# Database
class User(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	public_id = db.Column(db.String(50), unique=True)
	name = db.Column(db.String(100))
	email = db.Column(db.String(70), unique=True)
	password = db.Column(db.String(200))


class Token(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	token = db.Column(db.String(200), unique=True)
	user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
	exp = db.Column(
			db.DateTime,
			nullable=False,
			default=datetime.utcnow() + timedelta(minutes=120)
		)


class Price_unit(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	currencyCode = db.Column(db.String(100), unique=True)


class Products(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(200), unique=True)
	description = db.Column(db.Text)
	picture = db.Column(db.Text)
	total = db.Column(db.Integer, primary_key=True)
	unit_id = db.Column(db.Integer, db.ForeignKey('price_unit.id'))
	categories = db.Column(db.Text)


def generate_token(user_id, email):
	allowed_chars = ''.join((string.ascii_letters, string.digits))
	ramdom_char = ''.join(random.choice(allowed_chars) for _ in range(32))
	pre_token = str(user_id) + email + ramdom_char
	token = hashlib.md5(pre_token.encode("utf")).hexdigest()
	return token


# decorator for verifying the JWT
def token_required(f):
	@wraps(f)
	def decorated(*args, **kwargs):
		token = None
		# jwt is passed in the request header
		if 'x-access-token' in request.headers:
			token = request.headers['x-access-token']
		# return 401 if token is not passed
		if not token:
			return jsonify({'message': 'Token is missing !!'}), 401

		current_user = User.query.filter_by(
				id=Token.query.filter_by(token=token).first().user_id
			).first()
		if not current_user:
			return jsonify({
				'message': 'Token is invalid !!'
			}), 401
		# returns the current logged in users contex to the routes
		return f(current_user, *args, **kwargs)

	return decorated


# route for logging user in
@app.route('/login/', methods=['POST'])
def login():
	# creates dictionary of form data
	auth = request.form

	if not auth or not auth.get('email') or not auth.get('password'):
		# returns 401 if any email or / and password is missing
		return make_response(
			'Could not verify',
			401,
			{'WWW-Authenticate': 'Basic realm ="Login required !!"'}
		)

	user = User.query.filter_by(email = auth.get('email')).first()

	if not user:
		# returns 401 if user does not exist
		return make_response(
			'Could not verify',
			401,
			{'WWW-Authenticate': 'Basic realm ="User does not exist !!"'}
		)

	if check_password_hash(user.password, auth.get('password')):
		# generates the JWT Token
		token = generate_token(user.id, user.email)
		db.session.add(Token(token=token, user_id=user.id))
		db.session.commit()
		return make_response(jsonify({'token': token}), 201)
	#password is wrong
	return make_response( 
        jsonify({'message': 'password is wrong'}), 401)


# signup route
@app.route('/signup/', methods=['POST'])
def signup():
	# creates a dictionary of the form data
	data = request.form

	# gets name, email and password
	name, email = data.get('name'), data.get('email')
	password = data.get('password')

	# checking for existing user
	user = User.query\
		.filter_by(email = email)\
		.first()
	if not user:
		# database ORM object
		user = User(
			public_id = str(uuid.uuid4()),
			name = name,
			email = email,
			password = generate_password_hash(password)
		)
		# insert user
		db.session.add(user)
		db.session.commit()

		return make_response('Successfully registered.', 201)
	# returns 202 if user already exists
	return make_response('User already exists. Please Log in.', 202)


@app.route('/products/', methods=['GET'])
@token_required
def get_products(current_user):
	#TODO
	return make_response(jsonify({'products': 'passs'}), 200)


@app.route('/recommendations/', methods=['GET'])
@token_required
def get_recommendations(current_user):
	#TODO
	return make_response(jsonify({'recommendations': 'passs'}), 200)


if __name__ == "__main__":
	"""
	setting debug to True enables hot reload
	and also provides a debugger shell
	if you hit an error while running the server
	"""
	app.run(debug=True, host='0.0.0.0', port=5000)
