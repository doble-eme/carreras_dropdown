import numpy as np
from flask import Flask, request, jsonify, render_template, redirect, url_for
import pickle
import pandas as pd
import csv

#Initialize Flask app
app = Flask(__name__)

#Loads the trained model
model = pickle.load(open('modelo_udg.pkl', 'rb'))

@app.route("/", methods = ['GET', 'POST']) # Homepage and data read
def index():
    '''
    Reads data from csv file
    '''
    with open('.data/PuntajesMinimos_last.csv') as csv_file:
        data = csv.reader(csv_file, delimiter=',')
        carreras = []
        for row in data:
            carreras.append({
                "CALENDARIO": row[0],
                "CENTRO": row[1],
                "CARRERA": row[2],
                "PUNTAJE_MINIMO": row[3],
                "CUPO": row[4],
                "ADMITIDOS": row[5],
                "ASPIRANTES": row[6]
            })

    return render_template("index.html", carreras=carreras)

@app.route("/select_value", methods=['GET','POST'])
def select_value():
    '''
    Reads the selection from the dropdown menu
    '''
    seleccion = request.form.get('seleccion_carrera')
        
    #Clean list to remove white spaces and new lines
    seleccion_nnl = seleccion.replace('\r\n','')
    selection_clean = seleccion_nnl.replace(' ','')
    seleccion_list = selection_clean.split(',')
        
    #Creates the data frame to be sent to the predicion model
    input_variables = pd.DataFrame(seleccion_list).T

    #Executes the prediction using the trained model
    # print(input_variables)
    prediction = model.predict(input_variables)[0]

    #if statement to determine if the probability is high or low according to the prediction result
    if prediction == 0:
        result = 'Probabilidad baja'
    elif prediction == 1:
        result = 'Probabilidad alta'

    # rendering the predicted result on the page
    return render_template('index.html', prediction_text=result)

if __name__ == "__main__":
    app.run(debug=True)