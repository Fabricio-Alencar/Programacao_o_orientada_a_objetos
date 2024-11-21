from flask import Flask, flash, render_template, request, redirect, url_for, session, jsonify, g
from DAO_BD import ConexaoBD, UsuarioDAO, ConsultasDAO, ProntuarioDAO
from classes import Usuario, Visualizar_Usuario

app = Flask(__name__)
app.config['SECRET_KEY'] = 'RaposaCinza'

# Função para obter a conexão com o banco de dados
def get_db():
    if 'db' not in g:
        g.db = ConexaoBD().conn  # Cria uma nova conexão
    return g.db

@app.before_request
def before_request():
    get_db()  # Obtém a conexão antes de cada requisição

@app.teardown_appcontext
def close_db(exception):
    db = g.pop('db', None)  # Remove a conexão do g
    if db is not None:
        db.close()  # Fecha a conexão após a requisição

def criar_tabelas():
    db = get_db()
    cursor = db.cursor()
    # Criar as tabelas (você pode mover essa lógica para o ConexaoBD)
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Usuario (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        email TEXT UNIQUE NOT NULL,
        senha TEXT UNIQUE NOT NULL,
        telefone TEXT NOT NULL,
        tipo_usuario TEXT NOT NULL,
        especialidade TEXT,
        crm TEXT UNIQUE
    )''')

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Consultas (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        data DATE NOT NULL,
        hora TIME NOT NULL,
        status TEXT NOT NULL,
        observacoes TEXT,
        id_paciente_FK INTEGER,
        id_profissional_FK INTEGER,
        FOREIGN KEY (id_profissional_FK) REFERENCES Usuario(id),
        FOREIGN KEY (id_paciente_FK) REFERENCES Usuario(id)
    )''')

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Prontuario (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        data DATE NOT NULL,
        anotacoes_medicas TEXT NOT NULL,
        prescricoes TEXT,
        id_paciente_FK INTEGER,
        id_profissional_FK INTEGER,
        id_consulta_FK INTEGER,
        FOREIGN KEY (id_profissional_FK) REFERENCES Usuario(id),
        FOREIGN KEY (id_consulta_FK) REFERENCES Consultas(id),
        FOREIGN KEY (id_paciente_FK) REFERENCES Usuario(id)
    )''')

    db.commit()
    print("Tabelas criadas com sucesso!")

def cadastrar_usuarios_iniciais():
    usuario_dao = UsuarioDAO(get_db())
    usuario_dao.cadastrar(
        nome="Dr. João",
        email="joao@clinica.com",
        senha="1234",
        telefone="99999-8888",
        tipo_usuario="profissional",
        especialidade="Cardiologia",
        crm="12345"
    )
    usuario_dao.cadastrar(
        nome="Dr. Maria",
        email="maria@clinica.com",
        senha="12345",
        telefone="99999-8889",
        tipo_usuario="profissional",
        especialidade="Pediatria",
        crm="123456"
    )
    usuario_dao.cadastrar(
        nome="João",
        email="joaopaciente@email.com",
        senha="1245",
        telefone="123456789",
        tipo_usuario="paciente"
    )

@app.before_request
def before_first_request():
    criar_tabelas()  # Cria as tabelas no banco de dados
    cadastrar_usuarios_iniciais()  # Cadastra os usuários iniciais

# Função para autenticar o usuário
def autenticar_usuario(email, senha):
    usuario_dao = UsuarioDAO(get_db())
    usuario_bd = Visualizar_Usuario(usuario_dao, email=email)
    
    if usuario_bd and usuario_bd[0]["senha"] == senha:
        return Usuario(
            id=usuario_bd[0]["id"],
            nome=usuario_bd[0]["nome"],
            email=usuario_bd[0]["email"],
            senha=usuario_bd[0]["senha"],
            tipo_usuario=usuario_bd[0]["tipo_usuario"],
            telefone=usuario_bd[0]["telefone"],
            especialidade=usuario_bd[0]["especialidade"],
            crm=usuario_bd[0]["crm"]
        )
    return None  # Credenciais inválidas

@app.route('/')
def index():
    return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        senha = request.form['senha']
        usuario = autenticar_usuario(email, senha)
        if usuario:
            session['usuario_id'] = usuario.id
            session['usuario_nome'] = usuario.nome
            session['tipo_usuario'] = usuario.tipo_usuario
            if usuario.tipo_usuario == 'paciente':
                return render_template('paciente_dashboard.html', usuario_nome=session['usuario_nome'],usuario_id=session['usuario_id'])
            else:
                flash('Credenciais inválidas')
                return redirect(url_for('profissional_dashboard'))
        else:
            return render_template('login.html', mensagem='Credenciais inválidas')
    return render_template('login.html')

@app.route('/cadastrar_paciente', methods=['GET', 'POST'])
def cadastrar_paciente():
    if request.method == 'POST':
        nome = request.form['nome']
        sobrenome = request.form['sobrenome']
        email = request.form['email']
        senha = request.form['senha']
        telefone = request.form['telefone']
        # Verifica se o email já existe
        if verificar_email_existente(email):
            flash('Email já está cadastrado.')  # Mensagem de erro
            return render_template('cadastrar_paciente.html')  # Renderiza a mesma página
        try:
            usuario_dao = UsuarioDAO(get_db())
            usuario_dao.cadastrar(
            nome=nome,
            email=email,
            senha=senha,
            telefone=telefone,
            tipo_usuario="paciente",
            )
            flash('Paciente cadastrado com sucesso!')  # Mensagem de sucesso
            return redirect(url_for('login'))  # Redireciona para a página de login
        except Exception as e:
            print(f"Erro ao cadastrar: {e}")
            flash('Ocorreu um erro ao cadastrar o paciente. Tente novamente.')  # Mensagem de erro
            return render_template('cadastrar_paciente.html')  # Renderiza a mesma página em caso de erro
    return render_template('cadastrar_paciente.html')  # Renderiza a página de cadastro para GET

@app.route('/cadastrar_profissional', methods=['GET', 'POST'])
def cadastrar_profissional():
    if request.method == 'POST':
        nome = request.form['nome']
        sobrenome = request.form['sobrenome']
        email = request.form['email']
        senha = request.form['senha']
        telefone = request.form['telefone']
        especialidade = request.form['especialidade']
        crm = request.form['crm']
        # Verifica se o email já existe
        if verificar_email_existente(email):
            flash('Email já está cadastrado.')  # Mensagem de erro
            return render_template('cadastrar_profissional.html')  # Renderiza a mesma página
        elif verificar_crm_existente(crm):
            flash("CRM já está cadastrado.")  # Mensagem de erro
            return render_template('cadastrar_profissional.html')  # Renderiza a mesma página
        try:
            usuario_dao = UsuarioDAO(get_db())
            usuario_dao.cadastrar(
            nome=nome,
            email=email,
            senha=senha,
            telefone=telefone,
            tipo_usuario="profissional",
            especialidade = especialidade,
            crm = crm
            )
            flash('Profissional cadastrado com sucesso!')  # Mensagem de sucesso
            return redirect(url_for('login'))  # Redireciona para a página de login
        except Exception as e:
            print(f"Erro ao cadastrar: {e}")
            flash('Ocorreu um erro ao cadastrar o profissional. Tente novamente.')  # Mensagem de erro
            return render_template('cadastrar_profissional.html')  # Renderiza a mesma página em caso de erro
    return render_template('cadastrar_profissional.html')  # Renderiza a página de cadastro para GET

    
@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('login'))

@app.route('/paciente_dashboard')
def paciente_dashboard():
    if 'usuario_id' in session and session['tipo_usuario'] == 'paciente':
        return render_template('paciente_dashboard.html', usuario_nome=session['usuario_nome'], usuario_id=session['usuario_id'])
    else:
        return redirect(url_for('login'))

@app.route('/profissional_dashboard')
def profissional_dashboard():
    if 'usuario_id' in session and session['tipo_usuario'] == 'profissional':
        return render_template('profissional_dashboard.html', usuario_nome=session['usuario_nome'])
    else:
        return redirect(url_for('login'))

@app.route('/agendar_consulta', methods=['GET', 'POST'])
def agendar_consulta():
    if 'usuario_id' in session and session['tipo_usuario'] == 'paciente':
        consultas_dao = ConsultasDAO(get_db())  # Obtém o DAO aqui
        if request.method == 'POST':
            profissional_id = request.form['profissional_id']
            data_hora = request.form['data_hora']
            consulta = {
                'paciente_id': session['usuario_id'],
                'profissional_id': profissional_id,
                'data_hora': data_hora
            }
            consultas_dao.cadastrar(**consulta)  # Armazena a consulta
            return render_template('paciente_dashboard.html', usuario_nome=session['usuario_nome'])
        else:
            profissionais = obter_profissionais_banco_de_dados()
            return render_template('agendar_consulta.html', profissionais=profissionais)
    else:
        return redirect(url_for('login'))

@app.route('/paciente/<int:id>', methods=['GET'])  #OQUE ISSO FAZ?
def get_paciente(id):
    usuario_dao = UsuarioDAO(get_db())  # Obtém o DAO aqui
    paciente = Visualizar_Usuario(usuario_dao, id=id)
    if paciente:
        return jsonify(paciente.to_dict())
    return jsonify
    return jsonify({"error": "Paciente não encontrado"}), 404

def obter_profissionais_banco_de_dados():
    usuario_dao = UsuarioDAO(get_db())
    profissionais = usuario_dao.visualizar(tipo_usuario='profissional')
    return profissionais

def obter_pacientes_banco_de_dados():
    usuario_dao = UsuarioDAO(get_db())
    pacientes = usuario_dao.visualizar(tipo_usuario='paciente')
    return pacientes

def verificar_email_existente(email):
    usuario_dao = UsuarioDAO(get_db())
    usuario = usuario_dao.visualizar(email=email)
    return len(usuario) > 0 #retorna true se o email existir

def verificar_crm_existente(crm):
    usuario_dao = UsuarioDAO(get_db())
    usuario = usuario_dao.visualizar(crm=crm)
    return len(usuario) > 0 #retorna true se o crm existir

@app.route('/visualizar_consultas', methods=['GET'])
def visualizar_consultas():
    if 'usuario_id' in session and session['tipo_usuario'] == 'paciente':
        consultas_dao = ConsultasDAO(get_db())
        consultas = consultas_dao.visualizar(id_paciente_FK=session['usuario_id'])
        return render_template('visualizar_consultas.html', consultas=consultas, usuario_nome=session['usuario_nome'])
    else:
        return redirect(url_for('login'))

@app.route('/visualizar_prontuario', methods=['GET'])
def visualizar_prontuario():
    if 'usuario_id' in session and session['tipo_usuario'] == 'paciente':
        prontuario_dao = ProntuarioDAO(get_db())
        prontuarios = prontuario_dao.visualizar(id_paciente_FK=session['usuario_id'])
        return render_template('visualizar_prontuario.html', prontuarios=prontuarios, usuario_nome=session['usuario_nome'])
    else:
        return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True)
