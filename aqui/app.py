from flask import Flask, render_template, request, redirect, url_for, session,jsonify
from DAO_BD import GenericDAO, PacienteDAO, ProfissionalDAO, ConsultasDAO, ProntuarioDAO
from conexao_BD import ConexaoBD
from classes import Usuario
#Importar outras bibliotecas necessárias e módulos do banco de dados

app = Flask(__name__)
app.config['SECRET_KEY'] = 'RaposaCinza'

# Lista de usuários mockados
usuarios_mock = [
    Usuario('João Silva', 'joao@examplo.com', '12345', '21432141', 'Paciente'),
    Usuario('Maria Souza', 'maria@examplo.com', '12345', '12321421','Profissional', ''),
]

# Função para autenticar o usuário
def autenticar_usuario(email, senha):
    usuario_bd = Visualizar_Usuario(usuario_dao, email=email) 
    print(usuario_bd)
    for usuario in usuarios_mock:
        if usuario.email == email and usuario.senha == senha:
            return usuario  # Credenciais válidas, retorna o objeto usuário
    if usuario_bd:
            # Criação da instância do usuário com os dados retornados
            usuario = Usuario(
                nome=usuario_bd[0]["nome"],
                email=usuario_bd[0]["email"],
                senha=usuario_bd[0]["senha"],
                tipo_usuario=usuario_bd[0]["tipo_usuario"],
                telefone=usuario_bd[0]["telefone"],
                especialidade=usuario_bd[0]["especialidade"],
                crm=usuario_bd[0]["crm"]
            )
            if usuario and usuario.senha == senha:  # Comparar a senha corretamente
                return usuario
    return None  # Credenciais inválidas

@app.route('/')
def index():
    return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        senha = request.form['senha']
        # Lógica de autenticação
        usuario = autenticar_usuario(email, senha)
        if usuario:
            session['usuario_id'] = usuario.id
            session['usuario_nome'] = usuario.nome
            session['tipo_usuario'] = usuario.tipo_usuario
            if usuario.tipo_usuario == 'Paciente':
                #return redirect(url_for('paciente_dashboard'))
                return render_template('paciente_dashboard.html', usuario_nome=session['usuario_nome'])
            else:
                return redirect(url_for('profissional_dashboard'))
        else:
            return render_template('login.html', mensagem='Credenciais inválidas')
    return render_template('login.html')

@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('login'))

@app.route('/paciente_dashboard')
def paciente_dashboard(usuario_nome):
    if 'usuario_id' in session and session['tipo_usuario'] == 'Paciente':
        return render_template('paciente_dashboard.html', usuario_nome=session['usuario_nome'])
    else:
        return redirect(url_for('login'))
    #if

@app.route('/profissional_dashboard')
def profissional_dashboard():
    if 'usuario_id' in session and session['tipo_usuario'] == 'Profissional':
        return render_template('profissional_dashboard.html', usuario_nome=session['usuario_nome'])
    else:
        return redirect(url_for('login'))

# Rota para agendar consulta
@app.route('/agendar_consulta', methods=['GET', 'POST'])
def agendar_consulta():
    if 'usuario_id' in session and session['tipo_usuario'] == 'Paciente':
        if request.method == 'POST':
            profissional_id = request.form['profissional_id']
            data_hora = request.form['data_hora']
            # Lógica para agendar a consulta no banco de dados
            consulta = {
                'paciente_id': session['usuario_id'],
                'profissional_id': profissional_id,
                'data_hora': data_hora
            }
            consultas_agendadas.append(consulta)  # Armazena a consulta
            return render_template('paciente_dashboard.html', usuario_nome=session['usuario_nome'])
        else:
            # Obter lista de profissionais do banco de dados
            profissionais = obter_profissionais()
            return render_template('agendar_consulta.html', profissionais=profissionais)
    else:
        return redirect(url_for('login'))

# Rota para obter dados de um paciente
@app.route('/paciente/<int:id>', methods=['GET'])
def get_paciente(email):
    paciente = Visualizar_Usuario(usuario_dao, email=email)  # Obter paciente do banco de dados
    if paciente:
        return jsonify(paciente.to_dict())
    return jsonify({'error': 'Paciente não encontrado'}), 404

def obter_pacientes_banco_de_dados():
  pass


# Função fictícia para obter profissionais (deve ser implementada)
def obter_profissionais_banco_de_dados():
    lista_profissionais=[]
    for usuario in usuarios_mock:
        if usuario.tipo_usuario == "Profissional":
            lista_profissionais.append(usuario)
    return lista_profissionais  # Credenciais válidas, retorna o objeto usuário

# Outras rotas e lógica de negócio

if __name__ == '__main__':
    app.run(debug=True)
    conexao = ConexaoBD()
    conexao.criar_tabela()
    usuario_dao = UsuarioDAO(conexao.conn)
    consultas_dao = ConsultasDAO(conexao.conn)
    prontuario_dao = ProntuarioDAO(conexao.conn)
    usuario_dao = UsuarioDAO(conexao.conn)

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
        nome="Dr. João",
        email="joao1@clinica.com",
        senha="12345",
        telefone="99999-8888",
        tipo_usuario="profissional",
        especialidade="Cardiologia",
        crm="123456"
    )
    usuario_dao.cadastrar(
        nome="João",
        email="joaopaciente@email.com",
        senha="1245",
        telefone="123456789",
        tipo_usuario="paciente"
    )
    
    usuario_dao.cadastrar(
        nome="Fabricio",
        email="fabricio@email.com",
        senha="popop",
        telefone="123456789",
        tipo_usuario="paciente"
    )from flask import Flask, render_template, request, redirect, url_for, session,jsonify
from DAO_BD import GenericDAO, PacienteDAO, ProfissionalDAO, ConsultasDAO, ProntuarioDAO
from conexao_BD import ConexaoBD
from classes import Usuario
#Importar outras bibliotecas necessárias e módulos do banco de dados

app = Flask(__name__)
app.config['SECRET_KEY'] = 'RaposaCinza'

# Lista de usuários mockados
usuarios_mock = [
    Usuario('João Silva', 'joao@examplo.com', '12345', '21432141', 'Paciente'),
    Usuario('Maria Souza', 'maria@examplo.com', '12345', '12321421','Profissional', ''),
]

# Função para autenticar o usuário
def autenticar_usuario(email, senha):
    usuario_bd = Visualizar_Usuario(usuario_dao, email=email) 
    print(usuario_bd)
    for usuario in usuarios_mock:
        if usuario.email == email and usuario.senha == senha:
            return usuario  # Credenciais válidas, retorna o objeto usuário
    if usuario_bd:
            # Criação da instância do usuário com os dados retornados
            usuario = Usuario(
                nome=usuario_bd[0]["nome"],
                email=usuario_bd[0]["email"],
                senha=usuario_bd[0]["senha"],
                tipo_usuario=usuario_bd[0]["tipo_usuario"],
                telefone=usuario_bd[0]["telefone"],
                especialidade=usuario_bd[0]["especialidade"],
                crm=usuario_bd[0]["crm"]
            )
            if usuario and usuario.senha == senha:  # Comparar a senha corretamente
                return usuario
    return None  # Credenciais inválidas

@app.route('/')
def index():
    return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        senha = request.form['senha']
        # Lógica de autenticação
        usuario = autenticar_usuario(email, senha)
        if usuario:
            session['usuario_id'] = usuario.id
            session['usuario_nome'] = usuario.nome
            session['tipo_usuario'] = usuario.tipo_usuario
            if usuario.tipo_usuario == 'Paciente':
                #return redirect(url_for('paciente_dashboard'))
                return render_template('paciente_dashboard.html', usuario_nome=session['usuario_nome'])
            else:
                return redirect(url_for('profissional_dashboard'))
        else:
            return render_template('login.html', mensagem='Credenciais inválidas')
    return render_template('login.html')

@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('login'))

@app.route('/paciente_dashboard')
def paciente_dashboard(usuario_nome):
    if 'usuario_id' in session and session['tipo_usuario'] == 'Paciente':
        return render_template('paciente_dashboard.html', usuario_nome=session['usuario_nome'])
    else:
        return redirect(url_for('login'))
    #if

@app.route('/profissional_dashboard')
def profissional_dashboard():
    if 'usuario_id' in session and session['tipo_usuario'] == 'Profissional':
        return render_template('profissional_dashboard.html', usuario_nome=session['usuario_nome'])
    else:
        return redirect(url_for('login'))

# Rota para agendar consulta
@app.route('/agendar_consulta', methods=['GET', 'POST'])
def agendar_consulta():
    if 'usuario_id' in session and session['tipo_usuario'] == 'Paciente':
        if request.method == 'POST':
            profissional_id = request.form['profissional_id']
            data_hora = request.form['data_hora']
            # Lógica para agendar a consulta no banco de dados
            consulta = {
                'paciente_id': session['usuario_id'],
                'profissional_id': profissional_id,
                'data_hora': data_hora
            }
            consultas_agendadas.append(consulta)  # Armazena a consulta
            return render_template('paciente_dashboard.html', usuario_nome=session['usuario_nome'])
        else:
            # Obter lista de profissionais do banco de dados
            profissionais = obter_profissionais()
            return render_template('agendar_consulta.html', profissionais=profissionais)
    else:
        return redirect(url_for('login'))

# Rota para obter dados de um paciente
@app.route('/paciente/<int:id>', methods=['GET'])
def get_paciente(email):
    paciente = Visualizar_Usuario(usuario_dao, email=email)  # Obter paciente do banco de dados
    if paciente:
        return jsonify(paciente.to_dict())
    return jsonify({'error': 'Paciente não encontrado'}), 404

def obter_pacientes_banco_de_dados():
  pass


# Função fictícia para obter profissionais (deve ser implementada)
def obter_profissionais_banco_de_dados():
    lista_profissionais=[]
    for usuario in usuarios_mock:
        if usuario.tipo_usuario == "Profissional":
            lista_profissionais.append(usuario)
    return lista_profissionais  # Credenciais válidas, retorna o objeto usuário

# Outras rotas e lógica de negócio

if __name__ == '__main__':
    app.run(debug=True)
    conexao = ConexaoBD()
    conexao.criar_tabela()
    usuario_dao = UsuarioDAO(conexao.conn)
    consultas_dao = ConsultasDAO(conexao.conn)
    prontuario_dao = ProntuarioDAO(conexao.conn)
    usuario_dao = UsuarioDAO(conexao.conn)

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
        nome="Dr. João",
        email="joao1@clinica.com",
        senha="12345",
        telefone="99999-8888",
        tipo_usuario="profissional",
        especialidade="Cardiologia",
        crm="123456"
    )
    usuario_dao.cadastrar(
        nome="João",
        email="joaopaciente@email.com",
        senha="1245",
        telefone="123456789",
        tipo_usuario="paciente"
    )
    
    usuario_dao.cadastrar(
        nome="Fabricio",
        email="fabricio@email.com",
        senha="popop",
        telefone="123456789",
        tipo_usuario="paciente"
    )
