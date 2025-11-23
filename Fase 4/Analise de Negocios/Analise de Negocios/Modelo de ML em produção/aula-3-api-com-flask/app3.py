from flask import Flask, request, jsonify, Response

# Inicia o servidor Flask
app = Flask(__name__)

@app.route("/")
def home():
    """ Exemplo para status 200. """
    status_code = 200
    status_message = Response(status=status_code).status
    return jsonify({
        "status": status_message,
        "data": {"message": "Welcome to the API!"}
    }), status_code

@app.route("/create", methods=["POST"])
def create():
    """ Exemplo para status 201. """
    status_code = 201
    status_message = Response(status=status_code).status
    return jsonify({
        "status": status_message,
        "data": {"message": "Resource successfully created!"}
    }), status_code

@app.route("/validate", methods=["POST"])
def validate():
    """ Exemplo para status 400. """
    data = request.json
    if not data or "name" not in data:
        status_code = 400
        status_message = Response(status=status_code).status
        return jsonify({
            "status": status_message,
            "data": {"error": "Invalid data or 'name' field is missing!"}
        }), status_code
    # Caso os dados sejam válidos, retorna sucesso
    status_code = 200
    status_message = Response(status=status_code).status
    return jsonify({
        "status": status_message,
        "data": {"message": "Data is valid!"}
    }), status_code

@app.route("/private")
def private():
    """ Exemplo para status 401. """
    auth = request.headers.get("Authorization")
    if not auth:
        # Caso não tenha autenticação, retorna erro 401
        status_code = 401
        status_message = Response(status=status_code).status
        return jsonify({
            "status": status_message,
            "data": {"error": "Authentication required!"}
        }), status_code
    # Retorna mensagem de sucesso se autenticado
    status_code = 200
    status_message = Response(status=status_code).status
    return jsonify({
        "status": status_message,
        "data": {"message": "Welcome to the private area!"}
    }), status_code

@app.route("/admin")
def admin():
    """ Exemplo para status 403. """
    user_role = request.headers.get("Role")
    if user_role != "admin":
        # Caso não seja administrador, retorna erro 403
        status_code = 403
        status_message = Response(status=status_code).status
        return jsonify({
            "status": status_message,
            "data": {"error": "Access forbidden! Admins only."}
        }), status_code
    # Caso seja administrador, retorna sucesso
    status_code = 200
    status_message = Response(status=status_code).status
    return jsonify({
        "status": status_message,
        "data": {"message": "Welcome, Admin!"}
    }), status_code

@app.route("/item/<int:item_id>")
def get_item(item_id):
    """ Exemplo para status 404. """
    items = {1: "Item 1", 2: "Item 2"}
    if item_id not in items:
        # Caso o item não seja encontrado, retorna erro 404
        status_code = 404
        status_message = Response(status=status_code).status
        return jsonify({
            "status": status_message,
            "data": {"error": "Item not found!"}
        }), status_code
    # Retorna o item se encontrado
    status_code = 200
    status_message = Response(status=status_code).status
    return jsonify({
        "status": status_message,
        "data": {"item": items[item_id]}
    }), status_code

@app.route("/error")
def error():
    """ Exemplo para status 500. """
    try:
        # Gera um erro proposital (divisão por zero)
        1 / 0
    except ZeroDivisionError:
        # Captura o erro e retorna um status 500
        status_code = 500
        status_message = Response(status=status_code).status
        return jsonify({
            "status": status_message,
            "data": {"error": "Internal server error!"}
        }), status_code

if __name__ == "__main__":
    # Inicia o servidor Flask com debug ativado
    app.run(debug=True)
