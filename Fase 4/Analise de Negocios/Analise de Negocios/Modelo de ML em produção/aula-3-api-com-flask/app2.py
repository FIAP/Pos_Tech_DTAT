from flask import Flask, request, jsonify

# Cria a aplicação Flask
app = Flask(__name__)

# Dados simulados
users = {"1": {"name": "Alice"}, "2": {"name": "Bob"}}

# Rota GET - Recupera a lista de usuários
@app.route("/users", methods=["GET"])
def get_users():
    """Exemplo de método HTTP GET"""
    return jsonify({"users": users}), 200

# Rota POST - Adiciona um novo usuário
@app.route("/users", methods=["POST"])
def add_user():
    """Exemplo de método HTTP POST"""
    data = request.json
    user_id = str(len(users) + 1)  # Gera um novo ID
    users[user_id] = data
    return jsonify({"message": "User created!", "user": {user_id: data}}), 201

# Rota PUT - Atualiza um usuário existente
@app.route("/users/<user_id>", methods=["PUT"])
def update_user(user_id):
    """Exemplo de método HTTP PUT"""
    if user_id not in users:
        return jsonify({"error": "User not found!"}), 404
    data = request.json
    users[user_id].update(data)  # Atualiza os dados
    return jsonify({"message": "User updated!", "user": {user_id: users[user_id]}}), 200

# Rota DELETE - Remove um usuário
@app.route("/users/<user_id>", methods=["DELETE"])
def delete_user(user_id):
    """Exemplo de método HTTP DELETE"""
    if user_id not in users:
        return jsonify({"error": "User not found!"}), 404
    deleted_user = users.pop(user_id)
    return jsonify({"message": "User deleted!", "user": {user_id: deleted_user}}), 200

# Rota HEAD - Verifica se um usuário existe
@app.route("/users/<user_id>", methods=["HEAD"])
def head_user(user_id):
    """Exemplo de método HTTP HEAD"""
    if user_id not in users:
        return "", 404
    return "", 200

# Inicia o servidor Flask
if __name__ == "__main__":
    app.run(debug=True)
