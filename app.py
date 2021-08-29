#Using flask to make an API
#Import necessary libraries
from flask import Flask, jsonify, request,render_template
import pickle
import pandas as pd
import numpy as np

#Creating a flask app

app = Flask(__name__)
model = pickle.load(open('model.pickle','rb'))

#@app.route('/', methods= ['GET','POST'])
@app.route('/')
def home():
    return render_template("index.html")

@app.route('/predict', methods= ['POST'])
def predict():
    #model = pickle.load(open('model.pickle','rb'))
      # For rendering results on HTML GUI
    int_features = [float(x) for x in request.form.values()]
    final_features = [np.array(int_features)] 
    prediction = model.predict(final_features)
    output = round(prediction[0],2)
    return render_template("index.html",prediction_text= 'Water Potability should be: $ {}'.format(output))

# Driver function
if __name__ == '__main__':
     app.run(port=5000,debug=True)




