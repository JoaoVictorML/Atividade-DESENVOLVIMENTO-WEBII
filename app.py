from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/produtos')
def produtos():
    return render_template('produtos.html')

@app.route('/usuarios')
def usuarios():
    return render_template('usuarios.html')

@app.route('/menu')
def menu():
    return render_template('menu.html')

# Rota para a Home
@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

# Rota para Usuários (Trata exibição e envio)
@app.route('/usuarios', methods=['GET', 'POST'])
def usuarios():
    if request.method == 'POST':
        # O nome dentro do get('') deve ser o mesmo do 'name' no seu HTML
        email = request.form.get('email')
        senha = request.form.get('senha')
        
        # Mostra no terminal para conferirmos o recebimento
        print(f"--- NOVO USUÁRIO ---")
        print(f"E-mail: {email}")
        print(f"Senha: {senha}")
        
        return "Usuário cadastrado com sucesso! Verifique o console do VS Code."
    
    return render_template('usuarios.html')

# Rota para Produtos (Trata exibição e envio)
@app.route('/produtos', methods=['GET', 'POST'])
def produtos():
    if request.method == 'POST':
        # Capturando conforme os IDs/Names do seu HTML
        codigo = request.form.get('codigo')
        descricao = request.form.get('descricao')
        preco = request.form.get('preco')
        
        print(f"--- NOVO PRODUTO ---")
        print(f"Cód: {codigo} | Desc: {descricao} | Preço: R${preco}")
        
        return "Produto salvo com sucesso! Verifique o console do VS Code."
    
    return render_template('produtos.html')


if __name__ == '__main__':
    app.run(debug=True, port=5000)
