# Códigos de status com Flask 

Nessa seção iremos travar contato com diferentes tipos de códigos de status HTTP com Flask. Os códigos de status são essenciais para indicar o resultado da solicitação HTTP do cliente para a API. Os tipos mais comuns são: 

- 200: Indica que a solicitação foi bem-sucedida. Esse é o status padrão para respostas que retornam dados sem erros; 

- 201: Indica que um recurso foi criado com sucesso. Geralmente usado para requisições `POST`; 

- 400: Indica que há algo errado com a solicitação enviada pelo cliente, como dados inválidos ou ausentes; 

- 401: Indica que o cliente não está autenticado. É usado quando a API exige autenticação; 

- 403: Indica que o cliente não tem permissão para acessar o recurso, mesmo estando autenticado; 

- 404: Indica que o recurso solicitado não foi encontrado; 

- 500: Indica que houve um erro interno no servidor. Isso geralmente é retornado automaticamente quando há uma exceção não tratada. 

Agora vamos testar cada exemplo utilizando o cURL. Execute no terminal: 

```bash 
python app3.py 
``` 

Acesse o endpoint correspondente (http://127.0.0.1:5000/). 

Teste do exemplo da rota com código 200: 

```powershell
Invoke-RestMethod -Uri "http://127.0.0.1:5000/" -Method Get
```

```bash 
curl http://127.0.0.1:5000/ 
``` 

Resposta da requisição esperada: 

```bash 
{
  "data": {
    "message": "Welcome to the API!"
  },
  "status": "200 OK"
}
``` 

Teste do exemplo com código 201: 

```powershell
Invoke-RestMethod -Uri "http://127.0.0.1:5000/create" -Method Post
```

```bash 
curl -X POST http://127.0.0.1:5000/create 
``` 

Output esperado da requisição: 

```bash 
{
  "data": {
    "message": "Resource successfully created!"
  },
  "status": "201 CREATED"
}
```` 

Teste da rota com código 400: 

```powershell
$body = @{
    invalid_name = "John"
} | ConvertTo-Json

Invoke-RestMethod -Uri "http://127.0.0.1:5000/validate" -Method Post -Body $body -ContentType "application/json"
```

```bash 
curl -X POST -H "Content-Type: application/json" -d '{"invalid_name": "John"}' http://127.0.0.1:5000/validate 
``` 

Output esperado da requisição: 

```bash 
{
  "data": {
    "error": "Invalid data or 'name' field is missing!"
  },
  "status": "400 BAD REQUEST"
}
``` 

Exemplo da rota com código 401: 

```powershell
Invoke-RestMethod -Uri "http://127.0.0.1:5000/private" -Method Get
```

```bash 
curl http://127.0.0.1:5000/private 
``` 

Resposta da requisição esperada: 

```bash 
{
  "data": {
    "error": "Authentication required!"
  },
  "status": "401 UNAUTHORIZED"
}
``` 

Teste da rota com código 403: 

```powershell
$headers = @{
    "Role" = "user"
}

Invoke-RestMethod -Uri "http://127.0.0.1:5000/admin" -Method Get -Headers $headers
```

```bash 
curl -H "Role: user" http://127.0.0.1:5000/admin 
``` 

Output esperado: 

```bash 
{
  "data": {
    "error": "Access forbidden! Admins only."
  },
  "status": "403 FORBIDDEN"
}
``` 

Exemplo com código 404: 

```powershell
Invoke-RestMethod -Uri "http://127.0.0.1:5000/item/999" -Method Get
```

```bash 
curl http://127.0.0.1:5000/item/999 
``` 

Output esperado da requisição: 

```bash 
{
  "data": {
    "error": "Item not found!"
  },
  "status": "404 NOT FOUND"
}
```

Teste da rota com código 500: 

```powershell
Invoke-RestMethod -Uri "http://127.0.0.1:5000/error" -Method Get
```

```bash 
curl http://127.0.0.1:5000/error 
``` 

Output esperado: 

```bash 
{
  "data": {
    "error": "Internal server error!"
  },
  "status": "500 INTERNAL SERVER ERROR"
}
```

Esses são os códigos de status básicos mais comuns em APIs. Outros códigos também podem ser utilizados para situações específicas (ex.: 422 Unprocessable Entity, 429 Too Many Requests). 