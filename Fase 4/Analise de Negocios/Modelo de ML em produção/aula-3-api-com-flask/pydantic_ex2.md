# Validação com dados opcionais e valores padrão 

Neste exemplo, ampliaremos o uso do Pydantic para incluir campos opcionais e valores padrão. 

```python 
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

``` 

 

A classe `UserModel` nesse exemplo adiciona dois novos campos: 

- email: Opcional (pode estar ausente na requisição). 
- is_active: Sempre será True se não for enviado. 

Agora vamos fazer uma requisição POST com dados opcionais: 

```powershell
$body = @{
    name = "Bob"
    age = 30  # Valor válido para idade
} | ConvertTo-Json

$response = Invoke-RestMethod -Uri "http://127.0.0.1:5000/users" -Method Post -Body $body -ContentType "application/json"
$response | ConvertTo-Json -Depth 10
```

```bash 
curl -X POST -H "Content-Type: application/json" -d '{"name": "Bob", "age": 30}' http://127.0.0.1:5000/users 
``` 

Resposta da requisição: 

```bash 
{
  "message": "User created successfully!",
  "user": {
    "age": 30,
    "email": null,
    "is_active": true,
    "name": "Bob"
  }
}
``` 

Agora vamos checar o comportamento da aplicação realizando uma requisição `POST` com todos os campos: 

```powershell
$body = @{
    name      = "Charlie"
    age       = 22
    email     = "charlie@example.com"
    is_active = $false
} | ConvertTo-Json

$response = Invoke-RestMethod -Uri "http://127.0.0.1:5000/users" -Method Post -Body $body -ContentType "application/json"
$response | ConvertTo-Json -Depth 10
```

```bash 
curl -X POST -H "Content-Type: application/json" -d '{"name": "Charlie", "age": 22, "email": "charlie@example.com", "is_active": false}' http://127.0.0.1:5000/users 
``` 

Retorno da requisição: 

```bash 
{
  "message": "User created successfully!",
  "user": {
    "age": 22,
    "email": "charlie@example.com",
    "is_active": false,
    "name": "Charlie"
  }
}
``` 

E por fim, vamos verificar o comportamento da aplicação para uma requisição `POST` com dados inválidos: 

```powershell
$body = @{
    name = "Charlie"
    age  = "invalid"
} | ConvertTo-Json

$response = Invoke-RestMethod -Uri "http://127.0.0.1:5000/users" -Method Post -Body $body -ContentType "application/json"
$response | ConvertTo-Json -Depth 10
```

```bash 
curl -X POST -H "Content-Type: application/json" -d '{"name": "Charlie", "age": "invalid"}' http://127.0.0.1:5000/users
``` 

Resposta da requisição: 

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