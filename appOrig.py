#Using flask to make an API
#Import necessary libraries
from flask import Flask, jsonify, request
import pickle
import pandas as pd

#Creating a flask app

app = Flask(__name__)


@app.route('/', methods= ['GET','POST'])
def home():
    if(request.method == 'GET'):

        data = "Hello World"
        return jsonify({'data':data})

@app.route('/predict/', methods= ['GET','POST'])
def potability_predict():
    model = pickle.load(open('model.pickle','rb'))

    income = request.args.get('income')
    house_age = request.args.get('house_age')
    rooms = request.args.get('rooms')
    bedooms = request.args.get('bedrooms')
    population = request.args.get('population')

    # income = request.args.get('Avg. Area Income')
    # house_age = request.args.get('Avg. Area House Age')
    # rooms = request.args.get('Avg. Area Number of Rooms')
    # bedooms = request.args.get('Avg. Area Number of Bedrooms')
    # population = request.args.get('Area Population')

    test_df = pd.DataFrame({'income':[income], 'house_age':[house_age],'rooms':[rooms],'bedooms':[bedooms],'population':[population]})
 
    pred_price = model.predict(test_df)
    return jsonify({'House Price': str(pred_price)})

# Driver function
if __name__ == '__main__':
     app.run(debug=True)




