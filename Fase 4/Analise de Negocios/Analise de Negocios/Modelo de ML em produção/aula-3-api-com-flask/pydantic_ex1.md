# Validação simples com Pydantic 

Neste exemplo, usaremos o Pydantic para validar os dados de um usuário enviado em uma requisição `POST`.

```python 
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
``` 

Explicando o exemplo, a classe `UserModel` define o formato esperado dos dados do usuário com os campos obrigatórios: 

- name: Uma string; 
- age: Um inteiro. 

Fazemos uma requisição `POST` com dados válidos: 

```powershell
$body = @{
    name = "Alice"
    age = 25
} | ConvertTo-Json

$response = Invoke-RestMethod -Uri "http://127.0.0.1:5000/users" -Method Post -Body $body -ContentType "application/json"
$response | ConvertTo-Json -Depth 10
```

```bash 
curl -X POST -H "Content-Type: application/json" -d '{"name": "Alice", "age": 25}' http://127.0.0.1:5000/users 
``` 

Resposta da requisição: 

```bash 
{
  "message": "User created successfully!",
  "user": {
    "age": 25,
    "name": "Alice"
  }
}
``` 

Agora vamos checar o comportamento da requisição `POST` realizada com dados inválidos (com uma entrada em string para o age, quando o correto seria um inteiro): 

```powershell
$body = @{
    name = "Alice"
    age = "invalid"
} | ConvertTo-Json

$response = Invoke-RestMethod -Uri "http://127.0.0.1:5000/users" -Method Post -Body $body -ContentType "application/json"
$response | ConvertTo-Json -Depth 10
```

```bash 
curl -X POST -H "Content-Type: application/json" -d '{"name": "Alice", "age": "invalid"}' http://127.0.0.1:5000/users 
```

Resposta da requisição 

```bash 
{
  "errors": [
    {
      "input": "invalid",
      "loc": [
        "age"
      ],
      "msg": "Input should be a valid integer, unable to parse string as an integer",
      "type": "int_parsing",
      "url": "https://errors.pydantic.dev/2.4/v/int_parsing"
    }
  ]
}
```

 