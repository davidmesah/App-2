from flask import Flask, request, jsonify, render_template
import requests

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login():
    data = request.json
    username = data.get('username')
    password = data.get('password')
    # Aquí deberías verificar el usuario y la contraseña con la API correspondiente
    if username == "admin" and password == "1234":
        return jsonify({"message": "Login exitoso"}), 200
    return jsonify({"message": "Usuario o contraseña incorrectos"}), 401

@app.route('/inventory')
def inventory_page():
    return render_template('inventory.html')

@app.route('/inventory', methods=['GET'])
def inventory():
    name = request.args.get('name')
    category = request.args.get('category')
    response = requests.get(f'https://api.escuelajs.co/api/v1/products')
    return jsonify(response.json())

if __name__ == '__main__':
    app.run(debug=True)
