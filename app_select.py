from flask import Flask, request, jsonify, render_template
import csv

app = Flask(__name__)

@app.route("/")
def index():
  with open('.data/PuntajesMinimos_last.csv') as csv_file:
    data = csv.reader(csv_file, delimiter=',')
    first_line = True
    carreras = []
    for row in data:
      if not first_line:
        carreras.append({
          "CENTRO": row[0],
          "CARRERA": row[1],
          "ASPIRANTES": row[2],
          "ADMITIDOS": row[3],
          "CUPO": row[4],
          "PUNTAJE_MINIMO": row[5],
          "CALENDARIO": row[6]
        })
      else:
        first_line = False
  return render_template("index.html", carreras=carreras)

if __name__ == "__main__":
    app.run(debug=True)