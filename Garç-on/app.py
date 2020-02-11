from flask import Flask, request,jsonify , render_template

lista = []

app = Flask(__name__)

@app.route('/admin/<string:key>')
def admin_page(key):
    password = 'CaPfjGVCyFjgPJFCSSuqzkra'
    if password == key:
        return render_template('admin.html')
    else:
        return render_template('404.html')

@app.route('/mesa/<string:mesa>')
def mesa(mesa):
    return render_template('client.html',mesa = mesa)

@app.route('/chamar/<string:mesa>')
def Adiciona_mesa(mesa):
    if mesa in lista:
        return('False')
    else:
        lista.append(mesa)
        return("True")

@app.route('/remover/<string:mesa>')
def Remover_mesa(mesa):
    lista.remove(mesa)
    return("True")

@app.route('/list')
def Listar():
    return jsonify(lista = lista)


if __name__ == '__main__':
    app.run(host='192.168.0.17')