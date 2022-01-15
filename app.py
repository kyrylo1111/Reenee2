from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Api
from framework.models import *


app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://kiril:@localhost/Main'
app.config['WHOOSH_BASE'] = 'whoosh'
db = SQLAlchemy(app)
api = Api(app)


@app.route('/plant', methods=['POST', 'GET'])
def createplant():
    if request.method == 'POST':
        location = request.form['location']
        name = request.form['name']
        director_id = request.form['director_id']

        plant = Plant(location=location, name=name, director_id=director_id)
        try:
            db.session.add(plant)
            db.session.commit()
            return redirect('/saved')
        except:
            return 'error'
    else:
        return render_template('createplant.html')

@app.route('/employee', methods=['POST', 'GET'])
def createemployee():
    if request.method == 'POST':
        email = request.form['email']
        name = request.form['name']
        department_type = request.form['department_type']
        department_id = request.form['department_id']

        employee = Employee(email=email, name=name, department_type=department_type, department_id=department_id)

        try:
            db.session.add(employee)
            db.session.commit()
            return redirect('/saved')
        except:
            return 'error'
    else:
        return render_template('createemployee.html')


@app.route('/salon', methods=['POST', 'GET'])
def createsalon():
    if request.method == 'POST':
        email = request.form['email']
        name = request.form['name']
        department_type = request.form['department_type']
        department_id = request.form['department_id']
        salon = request.form['salon']

        salon = Salon(email=email, name=name, department_type=department_type, department_id=department_id, salon=salon)

        try:
            db.session.add(salon)
            db.session.commit()
            return redirect('/saved')
        except:
            return 'error'
    else:
        return render_template('createsalon.html')




@app.route('/saved', methods=['GET'])
def saved():
        return render_template('index.html')


@app.route('/main')
@app.route('/')
def mainpage():
        return render_template('mainpage.html')

@app.route('/search')
def search():
    plant = Plant.query.all()
    return render_template('search.html', plant=plant)


if __name__ == '__main__':
    app.run(debug=True)





