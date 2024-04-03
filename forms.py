from flask_wtf import FlaskForm
from wtforms import FloatField, StringField, IntegerField, SubmitField, TextAreaField, BooleanField, SelectField
from wtforms.validators import InputRequired, Optional, URL, NumberRange, Length

class cupcake_form(FlaskForm):
    flavor = StringField("Cupcake Flavor", validators=[InputRequired()])
    size = StringField("Cupcake Size", validators=[InputRequired()])
    rating = FloatField("Cupcake Rating", validators=[InputRequired()])
    image = StringField("Cupcake Image URL", validators=[URL()])
    submit = SubmitField("Add Cupcake")