from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/ejercicio1', methods=['GET', 'POST'])
def ejercicio1():
    resultado = None
    promedio = None
    estado = None
    
    if request.method == 'POST':
        nota1 = float(request.form['nota1'])
        nota2 = float(request.form['nota2'])
        nota3 = float(request.form['nota3'])
        asistencia = float(request.form['asistencia'])
        
        promedio = (nota1 + nota2 + nota3) / 3
        
        if promedio >= 40 and asistencia >= 75:
            estado = "APROBADO"
        else:
            estado = "REPROBADO"

        resultado = True

    return render_template('ejercicio1.html', resultado=resultado, promedio=round(promedio, 1) if promedio else None, estado=estado)

@app.route('/ejercicio2', methods=['GET', 'POST'])
def ejercicio2():
    nombre_largo = None
    longitud = None

    if request.method == 'POST':
        n1 = request.form['nombre1']
        n2 = request.form['nombre2']
        n3 = request.form['nombre3']

        nombre_largo = max(n1, n2, n3, key=len)
        longitud = len(nombre_largo)

    return render_template('ejercicio2.html', nombre_largo=nombre_largo, longitud=longitud)

if __name__ == '__main__':
    app.run(debug=True)