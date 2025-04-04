from flask import Flask, render_template, request
from werkzeug.utils import secure_filename
import os

# Define o diretório de uploads
UPLOAD_FOLDER = 'uploads'

# Garante que a pasta de uploads existe
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16 MB limite

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
            print(f'[DEBUG] Recebi um arquivo: {filename}')
            print(f'[DEBUG] Arquivo salvo em: {path}')

            return f'Formulário recebido com sucesso!<br>Nome: {nome}<br>Email: {email}<br>Análise: {analise}<br>Arquivo salvo em: {path}'

        return 'Erro: Envie um arquivo PDF válido.'

    return render_template('form.html')

if __name__ == '__main__':
    app.run(debug=True)
