from flask import Flask, request, jsonify, render_template
import csv
import pandas as pd

app = Flask(__name__)

@app.route("/")
def index():
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

@app.route("/select_value", methods=['GET', 'POST'])
def select_value():
    seleccion = request.form.get('seleccion_carrera')
    
    #limpiar la lista de espacios en blanco y nuevas lineas
    seleccion_nnl = seleccion.replace('\r\n','')
    selection_clean = seleccion_nnl.replace(' ','')
    seleccion_list = selection_clean.split(',')
    
    input_variables = pd.DataFrame(seleccion_list)
    print(input_variables)
    
    return (seleccion)

if __name__ == "__main__":
    app.run(debug=True)