from flask import Flask , render_template, request
import joblib
app = Flask(__name__)


model = joblib.load('regression_model.pkl')


@app.route('/')
def hello_world1():
    return render_template('base.html')

@app.route('/predict', methods = ['POST'])
def predict():
    area = request.form.get('area')
    rooms = request.form.get('rooms')
    bathroom = request.form.get('bathroom')
    floors = request.form.get('floors')
    driveway = request.form.get('driveway')
    game_room = request.form.get('game_room')
    cellar = request.form.get('cellar')
    gas = request.form.get('gas')
    air = request.form.get('air')
    garage = request.form.get('garage')
    situation = request.form.get('situation')

     
    prediction = model.predict([[int(area),int(rooms), int(bathroom),int(floors),int(driveway), int(game_room),int(cellar), int(gas),int(air),int(garage), int(situation)]])
    output = round(prediction[0],2)
    return render_template('base.html',prediction_text=f"House Price Will be $ {output}")

if __name__ =='__main__':
    app.run(debug = True)

