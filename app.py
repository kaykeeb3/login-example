from flask import Flask, request, render_template, redirect, url_for

app = Flask(__name__)

# obs: Dados de usuários (substitua isso por um banco de dados real)
users = {'...': '...'}

@app.route('/')
def login_page():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']

    if username in users and users[username] == password:
        return redirect(url_for('home'))
    else:
        return 'Credenciais incorretas.'

@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/cadastro', methods=['POST'])
def cadastro():
    username = request.form['username']
    password = request.form['password']
    
    # Verifica se o usuário já existe
    if username in users:
        return 'Usuário já existe. Faça login.'
    
    # Adiciona o novo usuário aos dados (substitua por um banco de dados real)
    users[username] = password
    return 'Cadastro bem-sucedido. Faça login.'

@app.route('/cadastro_page')
def cadastro_page():
    return render_template('cadastro.html')

@app.route('/logout')
def logout():
    return redirect(url_for('login_page'))

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
