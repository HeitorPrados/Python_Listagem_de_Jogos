from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Lista inicial de jogos
jogos = [
    {"nome": "The Witcher 3", "genero": "RPG"},
    {"nome": "Cyberpunk 2077", "genero": "Action RPG"},
    {"nome": "Hades", "genero": "Rogue-like"},
    {"nome": "Stardew Valley", "genero": "Simulação"},
    {"nome": "Overwatch", "genero": "FPS"}
]


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        nome = request.form['nome']
        genero = request.form['genero']
        # Adiciona um novo jogo à lista
        jogos.append({"nome": nome, "genero": genero})
        return redirect(url_for('index'))

    return render_template('index.html', jogos=jogos)


@app.route('/edit/<int:index>', methods=['GET', 'POST'])
def edit(index):
    if request.method == 'POST':
        nome = request.form['nome']
        genero = request.form['genero']
        # Atualiza os dados do jogo
        jogos[index] = {"nome": nome, "genero": genero}
        return redirect(url_for('index'))

    # Renderiza a página de edição com os dados atuais do jogo
    return render_template('edit.html', jogo=jogos[index], index=index)


@app.route('/delete/<int:index>', methods=['POST'])
def delete(index):
    if 0 <= index < len(jogos):
        jogos.pop(index)
    return redirect(url_for('index'))


if __name__ == "__main__":
    app.run(debug=True)
