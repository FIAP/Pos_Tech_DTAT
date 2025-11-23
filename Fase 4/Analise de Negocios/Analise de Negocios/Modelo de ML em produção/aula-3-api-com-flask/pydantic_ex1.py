from flask import Flask, request, jsonify
from pydantic import BaseModel, ValidationError

app = Flask(__name__)


# Modelo de validação para dados do usuário
class UserModel(BaseModel):
    name: str
    age: int


@app.route("/users", methods=["POST"])
def create_user():
    """
    POST: Cria um novo usuário com validação de dados.
    """
    data = request.json  # Obtém os dados enviados na requisição
    try:
        # Valida os dados usando o Pydantic
        user = UserModel(**data)
        return jsonify({"message": "User created successfully!", "user": user.dict()})
    except ValidationError as e:
        # Retorna erros de validação
        return jsonify({"errors": e.errors()}), 400


if __name__ == "__main__":
    app.run(debug=True)
