Executar o script no terminal com o comando: 

```bash 
python app3.py 
``` 

Agora podemos testar cada método do script. Primeiro vamos testar o exemplo do método `GET` para Recuperar a lista de usuários fazendo a seguinte requisição: 

```powershell
$response = Invoke-WebRequest -Uri "http://127.0.0.1:5000/users" -Method Get
$response.Content
```

```bash 
curl -X GET http://127.0.0.1:5000/users 
``` 

Resposta da requisição esperada: 

```bash 
{
  "users": {
    "1": {
      "name": "Alice"
    },
    "2": {
      "name": "Bob"
    }
  }
}
``` 

Agora fazemos a requisição no método `POST` para adicionar um novo usuário: 

```powershell
$body = @{name = "Carlos"} | ConvertTo-Json
$response = Invoke-RestMethod -Uri "http://127.0.0.1:5000/users" -Method Post -Body $body -ContentType "application/json"
$response | ConvertTo-Json -Depth 10
```

```bash 
curl -X POST -H "Content-Type: application/json" -d '{"name": "Carlos"}' http://127.0.0.1:5000/users 
``` 

Resposta da requisição: 

```bash 
{
  "message": "User created!",
  "user": {
    "3": {
      "name": "Carlos"
    }
  }
}
``` 

Requisição no método `PUT` para atualizar um usuário existente: 

```powershell
$body = @{name = "Alice Updated"} | ConvertTo-Json
$response = Invoke-RestMethod -Uri "http://127.0.0.1:5000/users/1" -Method Put -Body $body -ContentType "application/json"
$response | ConvertTo-Json -Depth 10
```

```bash 

curl -X PUT -H "Content-Type: application/json" -d '{"name": "Alice Updated"}' http://127.0.0.1:5000/users/1 

``` 

Retorno da requisição esperado: 

```bash 
{
  "message": "User updated!",
  "user": {
    "1": {
      "name": "Alice Updated"
    }
  }
}
``` 

Requisição no método `DELETE` para excluir um usuário: 

```powershell
$response = Invoke-RestMethod -Uri "http://127.0.0.1:5000/users/2" -Method Delete
$response | ConvertTo-Json -Depth 10
```

```bash 
curl -X DELETE http://127.0.0.1:5000/users/2 
``` 

Resposta da requisição esperada: 

```bash 
{
  "message": "User deleted!",
  "user": {
    "2": {
      "name": "Bob"
    }
  }
}
``` 

Requisição no método `HEAD` para verificar se um usuário existe: 

```powershell
$response = Invoke-WebRequest -Uri "http://127.0.0.1:5000/users/1" -Method Head
$response.Headers
```

```bash 
curl -I http://127.0.0.1:5000/users/1 
``` 

Resposta da requisição: 

```bash 
HTTP/1.1 200 OK
Server: Werkzeug/3.0.1 Python/3.10.12
Date: Fri, 24 Jan 2025 20:04:37 GMT
Content-Type: text/html; charset=utf-8
Content-Length: 0
Connection: close
``` 

O que cada método do HTTP faz? 

O método `GET` busca informações existentes no servidor, o `POST` é para criar novos recursos, o `PUT` é para atualizar ou criar um recurso (se ele não existir), o `DELETE` remove um recurso, e o `HEAD` verifica se um recurso existe sem carregar os dados. 