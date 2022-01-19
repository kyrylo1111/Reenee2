from models.models import Plant, Employee, Salon
from flask import render_template, request, redirect
from app import app, db


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
    boba = request.args.get('boba')
    if boba:
        plants = Plant.query.filter(Plant.name.contains(boba) | Plant.location.contains(boba))
        employees = Employee.query.filter(Employee.name.contains(boba) | Employee.email.contains(boba))
        salons = Salon.query.filter(Salon.name.contains(boba) | Salon.salon.contains(boba))
        return render_template('search.html', plant=plants, employee=employees, salon=salons)
    else:
        employee = Employee.query.all()
        plant = Plant.query.all()
        salon = Salon.query.all()
    return render_template('search.html', plant=plant, employee=employee, salon=salon)

