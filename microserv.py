from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

@app.route('/inventory', methods=['GET'])
def inventory():
    name = request.args.get('name')
    category = request.args.get('category')
    response = requests.get(f'https://python-poetry.org/')
    return jsonify(response.json())

if __name__ == '__main__':
    app.run(debug=True, port=5001)
    
