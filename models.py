"""Models for Cupcake app."""
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

DEFAULT_IMAGE_URL = "https://images.unsplash.com/photo-1576618148400-f54bed99fcfd?q=80&w=1480&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D"

class Cupcake(db.Model):

    __tablename__ = "cupcakes"

    id = db.Column(db.Integer,
                   primary_key=True,
                   autoincrement = True)
    flavor = db.Column(db.Text,
                           nullable=False)
    size = db.Column(db.Text,
                           nullable=False)
    rating = db.Column(db.Float,
                       nullable=False)
    image = db.Column(db.Text,
                       nullable = False,
                       default = DEFAULT_IMAGE_URL)
    
    @property
    def cupcake_name(self):
        

        return f"{self.flavor} {self.size}"
    
    def to_dict(self):
        return {
            'id': self.id,
            'flavor': self.flavor,
            'size': self.size,
            'rating': self.rating,
            'image': self.image
        }

   
    

    
    
def connect_db(app):
    with app.app_context():
        db.app = app
        db.init_app(app)