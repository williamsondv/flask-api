"""Flask app for Cupcakes"""
from flask import Flask, render_template, redirect, request, flash, jsonify
from forms import cupcake_form
from models import Cupcake, db, connect_db


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:postgres@localhost:5432/cupcakes'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.config['SECRET_KEY'] = 'secret'


app.app_context().push()
connect_db(app)
db.create_all()

@app.route('/api/cupcakes', methods=['GET'])
def list_cupcakes():
   
        cupcakes = [cupcake.to_dict() for cupcake in Cupcake.query.all()]
        return jsonify(cupcakes=cupcakes)

@app.route('/api/cupcakes/<int:cupcake_id>', methods=['GET'])
def get_cupcake(cupcake_id):

    cupcake = Cupcake.query.get_or_404(cupcake_id)
    return jsonify(cupcake=cupcake.to_dict())

@app.route('/api/cupcakes', methods=['POST'])
def create_cupcake():
      data = request.json
      cupcake = Cupcake(
            flavor  = data['flavor'],
            rating = data['rating'],
            size = data['size'],
            image = data['image'] or None
      )
      db.session.add(cupcake)
      db.session.commit()

      return (jsonify(cupcake=cupcake.to_dict()), 201)  

@app.route('/api/cupcakes/<int:cupcake_id>', methods=['PATCH'])
def update_cupcake(cupcake_id):
      cupcake = Cupcake.query.get_or_404(cupcake_id)
      data = request.json
      
      cupcake.flavor = data['flavor']
      cupcake.rating = data['rating']
      cupcake.size = data['size']
      cupcake.image = data['image']

      db.session.add(cupcake)
      db.session.commit()

      return (jsonify(cupcake = cupcake.to_dict()))

@app.route('/api/cupcakes/<int:cupcake_id>', methods=['DELETE'])
def delete_cupcake(cupcake_id):
      cupcake = Cupcake.query.get_or_404(cupcake_id)
      print(cupcake)
      db.session.delete(cupcake)
      db.session.commit()

      return jsonify(message= f'cupcake with id {cupcake_id} deleted')

@app.route('/', methods=['GET','POST'])
def root():
      form = cupcake_form();
      if form.is_submitted():
            print("here form")

            flavor = form.flavor.data
            size = form.size.data
            rating = form.rating.data
            image = form.image.data or None

            cupcake = Cupcake(
                  flavor = flavor,
                  size = size,
                  rating = rating,
                  image = image
            )
            db.session.add(cupcake)
            db.session.commit()
            return redirect('/')
      else:
            return render_template('index.html', form = form)