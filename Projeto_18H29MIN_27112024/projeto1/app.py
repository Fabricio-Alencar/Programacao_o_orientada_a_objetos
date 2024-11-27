from flask import Flask, flash, render_template, request, redirect, url_for, session, jsonify, g
from DAO_BD import ConexaoBD, UsuarioDAO, ConsultasDAO, ProntuarioDAO
import classes 
import verificacoes

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

@app.route('/')
def index():
    return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        senha = request.form['senha']
        usuario = verificacoes.autenticar_usuario(email, senha, UsuarioDAO, get_db, classes.Visualizar_Usuario, classes.Usuario)
        if usuario:
            session['usuario_id'] = usuario.id
            session['usuario_nome'] = usuario.nome
            session['tipo_usuario'] = usuario.tipo_usuario
            if usuario.tipo_usuario == 'paciente':
                return render_template('paciente_dashboard.html', usuario_nome=session['usuario_nome'], usuario_id=session['usuario_id'])
            else:  # Caso seja profissional
                return render_template('profissional_dashboard.html', usuario_nome=session['usuario_nome'], usuario_id=session['usuario_id'])
        else:
            flash('Credenciais inválidas')  # Mensagem de erro
            return render_template('login.html')
    return render_template('login.html')

@app.route('/cadastrar_paciente', methods=['GET', 'POST'])
def cadastrar_paciente():
    if request.method == 'POST':
        nome = request.form['nome']
        sobrenome = request.form['sobrenome']
        email = request.form['email']
        senha = request.form['senha']
        ddd = request.form['ddd']
        telefone = request.form['telefone']

        # Verifica se o email já existe
        if verificacoes.verificar_email_existente(email, UsuarioDAO, get_db):
            flash('Email já está cadastrado.')  # Mensagem de erro
            return render_template('cadastrar_paciente.html')  # Renderiza a mesma página

        try:
            usuario_dao = UsuarioDAO(get_db())
            usuario_dao.cadastrar(
                nome=nome + " " + sobrenome,
                email=email,
                senha=senha,
                telefone="+"+ddd+" "+ telefone,
                tipo_usuario="paciente"
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
        ddd = request.form['ddd']
        telefone = request.form['telefone']
        especialidade = request.form['especialidade']
        crm = request.form['crm']
        estado = request.form['estado']
        # Verifica se o email já existe
        if verificacoes.verificar_email_existente(email, UsuarioDAO, get_db):
            flash('Email já está cadastrado.')  # Mensagem de erro
            return render_template('cadastrar_profissional.html')  # Renderiza a mesma página  
        crm = crm+"/"+estado
        if verificacoes.verificar_crm_existente(crm, UsuarioDAO, get_db):
            flash("CRM já está cadastrado.")  # Mensagem de erro
            return render_template('cadastrar_profissional.html')  # Renderiza a mesma página
        try:
            usuario_dao = UsuarioDAO(get_db())
            usuario_dao.cadastrar(
                nome=nome + " " + sobrenome,
                email=email,
                senha=senha,
                telefone="+"+ddd+" "+ telefone,
                tipo_usuario="profissional",
                especialidade=especialidade ,
                crm=crm)
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

@app.route('/paciente_dashboard', methods=['GET'])
def paciente_dashboard():
    if 'usuario_id' in session and session['tipo_usuario'] == 'paciente':
        usuario_nome = request.args.get('nome', session['usuario_nome'])  # Obtém o nome da URL ou da sessão
        usuario_id = request.args.get('id', session['usuario_id'])  # Obtém o ID da URL ou da sessão
        return render_template('paciente_dashboard.html', usuario_nome=usuario_nome, usuario_id=usuario_id)
    return redirect(url_for('login'))

@app.route('/profissional_dashboard')
def profissional_dashboard():
    if 'usuario_id' in session and session['tipo_usuario'] == 'profissional':
        usuario_nome = request.args.get('nome', session['usuario_nome'])  # Obtém o nome da URL ou da sessão
        usuario_id = request.args.get('id', session['usuario_id'])  # Obtém o ID da URL ou da sessão
        return render_template('profissional_dashboard.html', usuario_nome=usuario_nome, usuario_id=usuario_id)
    return redirect(url_for('login'))

@app.route('/agendar_consulta', methods=['GET', 'POST'])
def agendar_consulta():
    if 'usuario_id' in session and session['tipo_usuario'] == 'paciente':
        if request.method == 'POST':
            data_hora = request.form['data_hora']
            id_profissional = request.form['profissional_id']
            status = "AGENDADO"
            observacoes = request.form.get('observacoes')  # Captura as observações do formulário
            id_paciente = session['usuario_id']
            try:
                consultas_dao = ConsultasDAO(get_db())
                data, hora = data_hora.split("T")
                consultas_dao.cadastrar(
                    data=data,
                    hora=hora,
                    status=status,
                    observacoes=observacoes,  # Armazena as observações
                    id_paciente_FK=id_paciente,
                    id_profissional_FK=id_profissional)
                flash('Consulta agendada com sucesso!')
                return redirect(url_for('paciente_dashboard'))
            except Exception as e:
                flash("Erro ao cadastrar consulta: " + str(e))
                print(f"Erro: {e}")  # Loga o erro no console
                return render_template('agendar_consulta.html', profissionais=verificacoes.obter_profissionais_banco_de_dados(UsuarioDAO, get_db))
    return render_template('agendar_consulta.html', profissionais=verificacoes.obter_profissionais_banco_de_dados(UsuarioDAO, get_db))

@app.route('/paciente/<int:id>', methods=['GET'])
def get_paciente(id):
    try:
        usuario_dao = UsuarioDAO(get_db())  # Obtém o DAO
        paciente = classes.Visualizar_Usuario(usuario_dao, id=id)
        if paciente:  # Verifica se o paciente foi encontrado
            if isinstance(paciente, list) and len(paciente) > 0:
                paciente_obj = paciente[0]  # Pega o primeiro item (se for uma lista)
                return jsonify(paciente_obj)  # Converte para JSON
            return jsonify(paciente.to_dict())  # Caso seja um único objeto
        return jsonify({"error": "Paciente não encontrado"}), 404
    except Exception as e:
        print(f"Erro ao buscar paciente: {e}")  # Loga o erro no console
        return jsonify({"error": "Erro no servidor"}), 500

@app.route('/profissional/<int:id>', methods=['GET'])
def get_profissional(id):
    try:
        usuario_dao = UsuarioDAO(get_db())  # Obtém o DAO
        profissional = usuario_dao.visualizar(id=id)  # Busca o profissional pelo ID
        if profissional:  # Verifica se o profissional foi encontrado
            return jsonify(profissional[0])  # Retorna o primeiro resultado como JSON
        return jsonify({"error": "Profissional não encontrado"}), 404  # Retorna erro 404 se o profissional não foi encontrado
    except Exception as e:
        print(f"Erro ao buscar profissional: {e}")  # Loga o erro no console
        return jsonify({"error": "Erro no servidor"}), 500

@app.route('/prontuarios', methods=['GET', 'POST'])
def gerenciar_prontuarios():
    if 'usuario_id' in session and session['tipo_usuario'] == 'profissional':
        id = session['usuario_id']
        if request.method == 'GET':
            # Retorna todos os prontuários do paciente logado
            prontuario_dao = ProntuarioDAO(get_db())
            prontuarios = prontuario_dao.visualizar(id_profissional_FK=session['usuario_id'])  # Supondo que você tenha essa 
            
            print(prontuarios,'gerenciar_prontuarios')
            prontuarios=jsonify(prontuarios) 
            return render_template('prontuarios.html', prontuarios=verificacoes.obter_prontuario_banco_de_dados(ProntuarioDAO, get_db, id))  # Retorna os prontuários em formato JSON
        elif request.method == 'POST':
            # Cria um novo prontuário
            data = request.json.get('data')
            anotacoes = request.json.get('anotacoes')
            prescricao = request.json.get('prescricao')
            id_paciente = session['usuario_id']  # Obtém o ID do paciente logado

            try:
                prontuario_dao = ProntuarioDAO(get_db())
                prontuario_dao.cadastrar(data=data, anotacoes=anotacoes, prescricao=prescricao, id_paciente_FK=id_paciente)
                return jsonify({"message": "Prontuário criado com sucesso!"}), 201
            except Exception as e:
                return jsonify({"error": str(e)}), 500

@app.route('/prontuarios/<int:id>', methods=['PUT', 'DELETE'])
def modificar_prontuario(id):
    prontuario_dao = ProntuarioDAO(get_db())

    if request.method == 'PUT':
        # Atualiza um prontuário existente
        data = request.json.get('data')
        anotacoes = request.json.get('anotacoes')
        prescricao = request.json.get('prescricao')

        try:
            prontuario_dao.atualizar(id, data=data, anotacoes=anotacoes, prescricao=prescricao)
            return jsonify({"message": "Prontuário atualizado com sucesso!"})
        except Exception as e:
            return jsonify({"error": str(e)}), 500

    elif request.method == 'DELETE':
        # Remove um prontuário existente
        try:
            prontuario_dao.remover(id)
            return jsonify({"message": "Prontuário removido com sucesso!"})
        except Exception as e:
            return jsonify({"error": str(e)}), 500

@app.route('/excluir_conta', methods=['POST'])
def excluir_conta():
    if 'usuario_id' in session:  # Verifica se o usuário está logado
        try:
            usuario_dao = UsuarioDAO(get_db())
            usuario_id = session['usuario_id']  # Obtém o ID do usuário da sessão
            classes.Excluir_Usuario(usuario_dao, 'id', usuario_id)  # Chama o método para excluir o usuário
            session.clear()  # Limpa a sessão
            flash('Conta excluída com sucesso!')  # Mensagem de sucesso
            return redirect(url_for('login'))  # Redireciona para a página de login
        except Exception as e:
            flash('Ocorreu um erro ao excluir sua conta. Tente novamente.')  # Mensagem de erro
            return redirect(url_for('login'))  # Redireciona para a tela de login
    return redirect(url_for('login'))  # Redireciona para o login se não estiver autenticado

@app.route('/minhas_consultas', methods=['GET', 'POST'])
def minhas_consultas():
    if 'usuario_id' not in session:
        return redirect(url_for('login'))  # Redireciona se não estiver autenticado
    id = session['usuario_id']
    tipo_usuario = session['tipo_usuario']  # Obtém o tipo de usuário
    consultas = []
    nomes = {}  # Muda para um dicionário
    if tipo_usuario == 'paciente':
        consultas = classes.Visualizar_Consulta(ConsultasDAO(get_db()), id_paciente_FK=id)
        # Obtém os nomes dos profissionais para todas as consultas
        for consulta in consultas:
            if 'id_profissional_FK' in consulta:
                profissional_id = consulta["id_profissional_FK"]
                nome = classes.Visualizar_Usuario(UsuarioDAO(get_db()), id=profissional_id)
                if nome:  # Verifica se o nome foi encontrado
                    nomes[profissional_id] = nome[0]["nome"]  # Armazena no dicionário
    elif tipo_usuario == 'profissional':
        consultas = classes.Visualizar_Consulta(ConsultasDAO(get_db()), id_profissional_FK=id)
        # Obtém os nomes dos pacientes para todas as consultas
        for consulta in consultas:
            if 'id_paciente_FK' in consulta:
                paciente_id = consulta["id_paciente_FK"]
                nome = classes.Visualizar_Usuario(UsuarioDAO(get_db()), id=paciente_id)
                if nome:  # Verifica se o nome foi encontrado
                    nomes[paciente_id] = nome[0]["nome"]  # Armazena no dicionário
    else:
        return redirect(url_for('login'))  # Redireciona se o tipo de usuário não for válido
    print(nomes)  # Para depuração
    return render_template('minhas_consultas.html', consultas=consultas, nomes=nomes, usuario_nome=session['usuario_nome'], usuario_id=session['usuario_id'], tipo_usuario=tipo_usuario)

@app.route('/dashboard')
def dashboard():
    if 'usuario_id' in session:
        if session['tipo_usuario'] == 'paciente':
            return redirect(url_for('paciente_dashboard'))
        elif session['tipo_usuario'] == 'profissional':
            return redirect(url_for('profissional_dashboard'))
    return redirect(url_for('login'))

@app.route('/atualizar_paciente/<int:id>', methods=['POST'])
def atualizar_paciente(id):
    if 'usuario_id' not in session:
        return redirect(url_for('login'))  # Redireciona se não estiver autenticado
    dados_atualizados = request.json
    try:
        usuario_dao = UsuarioDAO(get_db())
        for chave, valor in dados_atualizados.items():
            classes.Alterar_Usuario(usuario_dao, "id", id, chave, valor)
    except Exception as e:
        print(f"Erro ao atualizar paciente: {e}")  # Loga o erro no console
        return jsonify({"error": "Erro ao atualizar paciente."}), 500
    return jsonify({"message": "Paciente atualizado com sucesso!"}), 200

@app.route('/atualizar_profissional/<int:id>', methods=['POST'])
def atualizar_profissional(id):
    if 'usuario_id' not in session:
        return redirect(url_for('login'))  # Redireciona se não estiver autenticado
    dados_atualizados = request.json
    try:
        usuario_dao = UsuarioDAO(get_db())
        for chave, valor in dados_atualizados.items():
            classes.Alterar_Usuario(usuario_dao, "id", id, chave, valor)
    except Exception as e:
        print(f"Erro ao atualizar profissional: {e}")  # Loga o erro no console
        return jsonify({"error": "Erro ao atualizar profissional."}), 500
    return jsonify({"message": "Profissional atualizado com sucesso!"}), 200

@app.route('/consultas/<int:id>', methods=['DELETE'])
def excluir_consulta(id):
    if 'usuario_id' not in session:
        return jsonify({"error": "Usuário não autenticado"}), 401  # Retorna erro se não estiver autenticado
    try:
        consultas_dao = ConsultasDAO(get_db())
        if consultas_dao.excluir('id', id):  # Exclui a consulta com o ID fornecido
            return jsonify({"message": "Consulta excluída com sucesso!"}), 200
        else:
            return jsonify({"error": "Consulta não encontrada."}), 404
    except Exception as e:
        print(f"Erro ao excluir consulta: {e}")  # Loga o erro no console
        return jsonify({"error": "Erro ao excluir consulta."}), 500
    
@app.route('/consultas/<int:id>', methods=['PUT'])
def modificar_consulta(id):
    dados_atualizados = request.json
    try:
        consultas_dao = ConsultasDAO(get_db())
        for chave, valor in dados_atualizados.items():
            classes.Alterar_Usuario(consultas_dao, "id", id, chave, valor)
    except Exception as e:
        print(f"Erro ao atualizar consulta: {e}")  # Loga o erro no cons
        ole
        return jsonify({"error": "Erro ao atualizar consulta."}), 500
    return jsonify({"message": "Consulta atualizado com sucesso!"}), 200

if __name__ == '__main__':
    app.run(debug=True)