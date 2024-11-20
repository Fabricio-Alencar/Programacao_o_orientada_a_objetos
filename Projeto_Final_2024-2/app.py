from flask import Flask, render_template, request, redirect, url_for, session,jsonify, flash
# Importar outras bibliotecas necessárias e módulos do banco de dados

app = Flask(__name__)
app.config['SECRET_KEY'] = 'RaposaCinza'

# Definição da classe Usuario
class Usuario:
    def __init__(self, id, nome, email, senha, telefone, tipo_usuario, crm=None, especialidade=None):
        self.id = id
        self.nome = nome
        self.email = email
        self.senha = senha  # Em um ambiente real, as senhas devem ser armazenadas de forma segura (hash)
        self.telefone = telefone
        self.tipo_usuario = tipo_usuario  # 'Paciente' ou 'Profissional'
        self.crm = crm  # Apenas para profissionais
        self.especialidade = especialidade  # Apenas para profissionais

    # Método sobrescrito para retornar um dicionário com os dados do usuário
    def to_dict(self):
        usuario_dict = {
            'id': self.id,
            'nome': self.nome,
            'email': self.email,
            'senha': self.senha,
            'telefone': self.telefone,
            'tipo_usuario': self.tipo_usuario
        }
        # Adiciona informações específicas para profissionais
        if self.tipo_usuario == 'Profissional':
            usuario_dict['crm'] = self.crm
            usuario_dict['especialidade'] = self.especialidade
        return usuario_dict

# Lista de usuários mockados

usuarios_mock = [
    Usuario(1, 'João Silva', 'joao@examplo.com', '12345',1599678456, 'Paciente'),
    Usuario(2, 'Maria Souza', 'maria@examplo.com', '12345',123456789, 'Profissional','AX6789','cirurgião'),
]

consultas_agendadas = []

# Função para autenticar o usuário
def autenticar_usuario(email, senha):
    # Itera sobre a lista de usuários mockados
    for usuario in usuarios_mock:
        if usuario.email == email and usuario.senha == senha:
            return usuario  # Credenciais válidas, retorna o objeto usuário
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
            flash('Credenciais inválidas')
            return redirect(url_for('login'))
    return render_template('login.html')


@app.route('/cadastrar_paciente', methods=['GET', 'POST'])
def cadastrar_paciente():
    if request.method == 'POST':
        nome = request.form['nome']
        sobrenome = request.form['sobrenome']
        email = request.form['email']
        senha = request.form['senha']
        telefone = request.form['telefone']

        novo_id = len(usuarios_mock) + 1  # Simplesmente incrementa o ID
        novo_paciente = Usuario(novo_id, f"{nome} {sobrenome}", email, senha, telefone, 'Paciente')

        usuarios_mock.append(novo_paciente)
        flash('Paciente cadastrado com sucesso!')
        return redirect(url_for('login'))

    return render_template('cadastrar_paciente.html')


@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('login'))

@app.route('/paciente_dashboard')
def paciente_dashboard():
    if 'usuario_id' in session and session['tipo_usuario'] == 'Paciente':
        print(usuario_id)
        return render_template('paciente_dashboard.html', 
                               usuario_nome=session['usuario_nome'], 
                               usuario_id=session['usuario_id'])  # Passando o ID do paciente
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
def get_paciente(id):
    # Busca o paciente pelo ID na lista de usuários
    for usuario in usuarios_mock:
        if usuario.id == id and usuario.tipo_usuario == 'Paciente':
            return jsonify(usuario.to_dict())
    
    return jsonify({'error': 'Paciente não encontrado'}), 404
#rota para obter dados de um profissional

@app.route('/profissional/<int:id>', methods=['GET'])
def get_profissional(id):
    # Busca o paciente pelo ID na lista de usuários
    for usuario in usuarios_mock:
        if usuario.id == id and usuario.tipo_usuario == 'Profissional':
            return jsonify(usuario.to_dict())
    
    return jsonify({'error': 'Paciente não encontrado'}), 404
    

# Função fictícia para obter profissionais (deve ser implementada)
def obter_profissionais():
    lista_profissionais=[]
    for usuario in usuarios_mock:
        if usuario.tipo_usuario == "Profissional":
            lista_profissionais.append(usuario)
    return lista_profissionais  # Credenciais válidas, retorna o objeto usuário


# Outras rotas e lógica de negócio

if __name__ == '__main__':
    app.run(debug=True)
