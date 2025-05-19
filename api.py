from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Permite chamadas do navegador (CORS)

@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    # Exemplo simples de validação
    if username == 'admin' and password == '1234':
        return jsonify({"status": "success", "message": "Login realizado com sucesso!"})
    else:
        return jsonify({"status": "error", "message": "Usuário ou senha inválidos."}), 401

if __name__ == '__main__':
    app.run(debug=True)
