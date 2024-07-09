from app import app
from flask import render_template
#uma deretiva para colocar a rota de onde quero que abra o meu app
#aqui terá a rota padrão e a alternativa para abrir o método abaixo
@app.route('/')
@app.route('/index')
def index():
    nome="Mariany"
    dados={"País": "Espanha", "Cidade":"Madrid"}
    return render_template('index.html', nome=nome, dados=dados)

@app.route('/contato')
def contato():
    return render_template('contato.html')