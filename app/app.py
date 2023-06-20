from flask import Flask,render_template
from flask_sqlalchemy import SQLAlchemy
import mysql.connector


app = Flask(__name__)
# password="hkh72280"
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:test@localhost/'



db=SQLAlchemy(app)

class Country_master(db.Model):
    __tablename__='Country'
    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String(10),nullable=False)
    nicename=db.Column(db.String(10),nullable=False)
    iso3=db.Column(db.String(10),nullable=False)
    iso=db.Column(db.String(10),nullable=False)
    
class Client_master(db.Model): 
    client_id=db.Column(db.Integer,primary_key=True)
    client_name=db.Column(db.String(255),nullable=False)
    country_id=db.Column(db.Integer,nullable=False)
    agency_id=db.Column(db.Integer,db.ForeignKey(''))


class Brand_master(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    client_id=db.Column(db.Integer, db.ForeignKey('Client_master.id'))
    Brand_name=db.Column(db.String(255),nullable=False)
    country_id= db.Column(db.Integer, db.ForeignKey(''))
    
class Retailer_master(db.Model):
    retailer_id=db.Column(db.Integer,primary_key=True)
    retailer_name=db.Column(db.String(255),nullable=False)
    retailer_country_id=db.Column(db.Integer,nullable=False)          
    retailer_url=db.Column(db.String(255),nullable=False)

class Client_entity_master(db.Model):
    client_entity_id=db.Column(db.Integer,primary_key=True)
    client_id=db.Column(db.Integer, db.ForeignKey('Client_master.id'))
    client_entity_name=db.Column(db.String(255),nullable=False)
    country_id= db.Column(db.Integer, db.ForeignKey(''))




@app.route("/")
def hello_world():
    # return "<p>Hello, World!</p>"
    db.create_all()
    db.session.commit()
    return render_template('index.html')


app.run(debug=True,port=5002)