from flask import Flask, render_template
from flask_cors import CORS
import math as mt
from flask import jsonify

app = Flask(__name__)
CORS(app)

#SUMA
@app.route("/")
@app.route("/<float:numero1>/<float:numero2>")
@app.route("/<int:numero1>/<int:numero2>")
@app.route("/<int:numero1>/<float:numero2>")
@app.route("/<float:numero1>/<int:numero2>")
def suma():
    resultado=numero1+numero2
    ##return f"<h1>El resultado es: {resultado}</h1> <hr>"
    data={
        "resultado":resultado,
        "operacion":"suma",
    }
    return jsonify(data)

##RESTA
@app.route("/resta/<float:numero1>/<float:numero2>")
@app.route("/resta/<int:numero1>/<int:numero2>")
@app.route("/resta/<int:numero1>/<float:numero2>")
@app.route("/resta/<float:numero1>/<int:numero2>")
def resta(numero1=0,numero2=0):
    resultado=numero1-numero2
    ##resturn f" <h1> El resultado es: {resultado}</h1> <hr>"
    data={
        "resultado":resultado,
        "operacion":"resta",
    }
    return jsonify(data)

##MULTIPLICACION
@app.route("/multiplicacion/<float:numero1>/<float:numero2>")
@app.route("/multiplicacion/<int:numero1>/<float:numero2>")
@app.route("/multiplicacion/<float:numero1>/<int:numero2")
@app.route("/multiplicacion/<int:numero1>/<float:numero2>")
def multiplicacion(numero1=0,numero2=0):
    resultado=numero1*numero2
    ##resturn f" <h1> El resultado es: {resultado}</h1> <hr>"
    data={
        "resultado":resultado,
        "operacion":"multiplicacion",
    }
    return jsonify(data)

##DIVISION
@app.route("7division/<float:numero1>/<float:numero2>")
@app.route("division/<int:numero1>/<float:numero2>")
@app.route("/division/<float:numero1>/<int:numero2>")
@app.route("/division/<int:numero1>/<float:numero2>")
def division(numero1=0,numero2=0):
    resultado=numero1/numero2
    ##resturn f" <h1> El resultado es: {resultado}</h1> <hr>"
    data={
        "resultado":resultado,
        "operacion":"division",
    }
    return jsonify(data)

##POTENCIACION
@app.route("/potenciacion/<float:numero1>/<float:numero2>")
@app.route("/potenciacion/<int:numero1>/<int:numero2>")
@app.route("/potenciacion/<int:numero1>/<float:numero2>")
@app.route("/potenciacion/<float:numero1>/<int:numero2>")
def potenciacion(numero1=0,numero2=0):
    resultado=numero1**numero2
    ##resturn f" <h1> El resultado es: {resultado}</h1> <hr>"
    data={
        "resultado":resultado,
        "operacion":"potenciacion",
    }
    return jsonify(data)

#SENO
@app.route("/seno/<float:numero1>")
@app.route("/seno/<int:numero1>")
def seno(numero1=0):
    resultado=mt.sin(numero1)
    ##resturn f" <h1> El resultado es: {resultado}</h1> <hr>"
    data={
        "resultado":resultado,
        "operacion":"seno",
    }
    return jsonify(data)

#COSENO
@app.route("/coseno/<float:numero1>")
@app.route("/coseno/<int:numero1>")
def seno(numero1=0):
    resultado=mt.cos(numero1)
    ##resturn f" <h1> El resultado es: {resultado}</h1> <hr>"
    data={
        "resultado":resultado,
        "operacion":"coseno",
    }
    return jsonify(data)


if __name__ == '__main__':
    app.run(debug=True) 
    