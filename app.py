from flask import Flask, render_template, url_for, flash, session, redirect
from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SECRET_KEY'] = 'kmykey' 
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
db = SQLAlchemy()
db.init_app(app)

class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(200), nullable=False)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)
    def __repr__(self):
        return '<Task %r>' % self.id

class SimpleForm(FlaskForm):
    submit = SubmitField('jsem veverka')

@app.route('/', methods=['GET', 'POST'])
def index():  
    return 
    # form = SimpleForm()
    # if form.validate_on_submit():
    #     flash('You just clicked the button')
    #     return redirect(url_for('index'))
    # return render_template('index.html', form=form, maja=["Ahoj", "Nazdar", "Fuuu"])


@app.route('/ahoj', methods=['GET', 'POST'])
def ahoj_view():  
    return "AHOJ MAJO"


if __name__ == "__main__":
    app.run(debug=True)

