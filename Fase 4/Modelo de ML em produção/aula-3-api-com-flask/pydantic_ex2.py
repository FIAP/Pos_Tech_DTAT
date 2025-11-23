from flask import Flask, request, jsonify
from pydantic import BaseModel, ValidationError
from typing import Optional

app = Flask(__name__)

# Modelo de validação para dados do usuário
class UserModel(BaseModel):
    name: str
    age: int
    email: Optional[str] = None  # Campo opcional
    is_active: bool = True       # Campo com valor padrão

@app.route("/users", methods=["POST"])
def create_user():
    """
    POST: Cria um novo usuário com validação e valores padrão.
    """
    data = request.json
    try:
        user = UserModel(**data)
        return jsonify({"message": "User created successfully!", "user": user.dict()})
    except ValidationError as e:
        return jsonify({"errors": e.errors()}), 400

if __name__ == "__main__":
    app.run(debug=True)
