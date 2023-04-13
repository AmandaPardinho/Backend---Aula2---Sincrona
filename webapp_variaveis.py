# Criação de um dicionário com duas chaves e retorná-lo pela rota

dicionario = {
    "nome": "Amanda",
    "nascimento": "03/01/1989"
}


# Import do Flask
from flask import Flask

# Criação da aplicação Flask
app = Flask(__name__)

# Criação da rota e acionamento da função que retorna um dicionário
@app.route("/teste")
def mostra_dicionario():
    return dicionario

@app.route("/")
def dados_usuario():
    return f"<b>O usuário {dicionario['nome']} nasceu em {dicionario['nascimento']}</b>"

# Faz a aplicação rodar
app.run(debug=True)