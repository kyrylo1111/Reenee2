from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Api

app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://kiril:@localhost/Main'
db = SQLAlchemy(app)
api = Api(app)



class Plant(db.Model):
    __tablename__ = 'Plants'
    id = db.Column(db.Integer, primary_key=True)
    location = db.Column(db.String(64), nullable=False)
    name = db.Column(db.String(64), nullable=False)
    director_id = db.Column(db.Integer, nullable=False)


class Employee(db.Model):
    __tablename__ = 'Employees'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(64), nullable=False)
    name = db.Column(db.String(64), nullable=False)
    department_type = db.Column(db.Integer, nullable=False)
    department_id = db.Column(db.Integer, nullable=False)


class Salon(db.Model):
    __tablename__ = 'Salons'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(64), nullable=False)
    name = db.Column(db.String(64), nullable=False)
    department_type = db.Column(db.String(64), nullable=False)
    department_id = db.Column(db.Integer, nullable=False)
    salon = db.Column(db.String(64), nullable=False)


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
@app.route('/')
def mainpage():
        return render_template('mainpage.html')
if __name__ == '__main__':
    app.run(debug=True)





