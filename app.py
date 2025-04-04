from flask import Flask, render_template, request
from werkzeug.utils import secure_filename
import os

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16 MB limite

# Garante que a pasta de uploads exista
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

@app.route('/', methods=['GET', 'POST'])
def form():
    if request.method == 'POST':
        nome = request.form['nome']
        email = request.form['email']
        analise = request.form['analise']
        arquivo = request.files['arquivo']

        if arquivo and arquivo.filename.endswith('.pdf'):
            filename = secure_filename(arquivo.filename)
            path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            arquivo.save(path)
            return f'Formulário recebido com sucesso!<br>Nome: {nome}<br>Email: {email}<br>Análise: {analise}<br>Arquivo salvo em: {path}'

        return 'Erro: Envie um arquivo PDF válido.'

    return render_template('form.html')

if __name__ == '__main__':
    app.run(debug=True)

