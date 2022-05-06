from flask import Flask, request, jsonify, render_template
import csv

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

if __name__ == "__main__":
    app.run(debug=True)