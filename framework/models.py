from app import db

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
