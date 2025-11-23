# Exercício 4

Agora vamos utilizar um volume Docker para criar um banco de dados SQL persistente usando a imagem oficial do MySQL, incluindo a inserção de registros e a execução de queries SQL para checar o retorno. 

1. Crie um volume nomeado para armazenar os dados do banco 

```bash 
docker volume create dados_mysql 
``` 

2. Inicie um container MySQL utilizando o volume criado 

```bash 
docker run -d --name mysql_container \
  -e MYSQL_ROOT_PASSWORD=senha_secreta \
  -e MYSQL_DATABASE=meu_banco \
  -v dados_mysql:/var/lib/mysql \
  -p 3306:3306 \
  mysql:8.0 
``` 

Explicação: 

- `MYSQL_ROOT_PASSWORD`: Define a senha para o usuário root; 
- `MYSQL_DATABASE`: Cria automaticamente um banco de dados chamado meu_banco; 
- `-v dados_mysql`:/var/lib/mysql: Conecta o volume ao diretório de dados do MySQL; 
- `-p 3306:3306`: Expõe a porta do banco de dados para acesso local. 

Vamos inserir registros no banco de dados. 

3. Acesse o container: 

```bash 
docker exec -it mysql_container bash 
``` 
 
4. Abra o cliente MySQL: 

```bash 
mysql -uroot -p 
``` 

5. Conecte-se ao banco de dados meu_banco: 

```bash 
USE meu_banco; 
``` 

6. Crie uma tabela chamada usuarios: 

```bash 
CREATE TABLE usuarios (id INT AUTO_INCREMENT PRIMARY KEY, nome VARCHAR(50) NOT NULL, email VARCHAR(50) NOT NULL); 
``` 

7. Insira registros na tabela: 

```mysql 
INSERT INTO usuarios (nome, email) VALUES ('Alice', 'alice@email.com'); INSERT INTO usuarios (nome, email) VALUES ('Bob', 'bob@email.com'); INSERT INTO usuarios (nome, email) VALUES ('Carlos', 'carlos@email.com'); 
``` 

8. Cheque se os registros foram inseridos: 

```bash 
SELECT * FROM usuarios; 
``` 

O resultado esperado: 

```
+----+--------+------------------+
| id | nome   | email            |
+----+--------+------------------+
|  1 | Alice  | alice@email.com  |
|  2 | Bob    | bob@email.com    |
|  3 | Carlos | carlos@email.com |
+----+--------+------------------+
``` 

Agora vamos testar a persistência dos dados, uma propriedade de volume do Docker. 

9. Pare e remova o container: 

```bash 
docker stop mysql_container 
docker rm mysql_container 
``` 

10. Recrie o container utilizando o mesmo volume: 

```bash 
docker run -d --name mysql_container -e MYSQL_ROOT_PASSWORD=senha_secreta -v dados_mysql:/var/lib/mysql -p 3306:3306 mysql:8.0 
``` 

Verifique se os registros ainda existem. Acesse o container e o cliente MySQL: 

```bash 
docker exec -it mysql_container bash 
``` 

E depois: 

```bash
mysql -uroot -p 
``` 

Conecte-se ao banco meu_banco e consulte a tabela usuarios: 

```bash 
USE meu_banco; SELECT * FROM usuarios; 
```

O resultado deve exibir os registros previamente inseridos: 

```
+----+--------+------------------+
| id | nome   | email            |
+----+--------+------------------+
|  1 | Alice  | alice@email.com  |
|  2 | Bob    | bob@email.com    |
|  3 | Carlos | carlos@email.com |
+----+--------+------------------+
```

 

 

 