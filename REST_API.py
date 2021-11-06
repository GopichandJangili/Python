from flask import Flask,request
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres:Password01@localhost:5432/cars_api"
db = SQLAlchemy(app)
migrate = Migrate(app,db)


class CarsModel(db.Model):
    __tablename__ = 'cars'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String())
    model = db.Column(db.String())
    doors = db.Column(db.String())

    def __init__(self,n,m,d):
        self.name = n
        self.model = m
        self.doors = d
    def __repr__(self):
        return f'<Car {self.name}>'
        


@app.route('/')
def hello():
    return {"Hello":"World"}

@app.route('/cars',methods=['GET','POST'])
def handle_cars():
    if request.method == 'POST':
        if request.is_json:
            data = request.get_json()
            new_car = CarsModel(n=data['name'], m=data['model'], d=data['doors'])
            db.session.add(new_car)
            db.session.commit()
            return {"message": f"car {new_car.name} has been created succesfully"}
        else:
            return {"message": "The request payload is not in JSON format"}
    
    elif request.method == 'GET':
        cars = CarsModel.query.all()
        results = [
                {
                    "name" : car.name,
                    "model": car.model,
                    "doors": car.doors
                }for car in cars]
        return {"count":len(results),"cars" : results}

if __name__ == '__main__':
    app.run(debug=True)