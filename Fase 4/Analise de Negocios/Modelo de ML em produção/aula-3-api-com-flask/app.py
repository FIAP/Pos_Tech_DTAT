from flask import Flask  # Importa o framework Flask

app = Flask(__name__)  # Cria a aplicação Flask


@app.route("/")  # Define a rota para o caminho "/"
def home():
    return {"message": "Hello world!"}  # Retorna uma resposta JSON


if __name__ == "__main__":
    app.run(debug=True)  # Inicia o servidor com debug ativado
