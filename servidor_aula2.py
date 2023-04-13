# Importa o Flask para podermos usar o programa
from flask import Flask

# Cria um objeto para representar a aplicação web
app = Flask(__name__)

# Criação de uma rota para acessar o servidor
@app.route("/")

# Função que, ao acessar a rota, vai retornar um texto
def exibir_mensagem():
    return "Deu certo!"

# Executa a aplicação web que foi criada a partir do Flask
app.run(debug=True)