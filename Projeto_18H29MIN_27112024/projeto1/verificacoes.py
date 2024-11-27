def obter_profissionais_banco_de_dados(UsuarioDAO,get_db):
    usuario_dao = UsuarioDAO(get_db())
    profissionais = usuario_dao.visualizar(tipo_usuario='profissional')
    return profissionais

def obter_pacientes_banco_de_dados(UsuarioDAO,get_db):
    usuario_dao = UsuarioDAO(get_db())
    pacientes = usuario_dao.visualizar(tipo_usuario='paciente')
    return pacientes

def obter_consultas_banco_de_dados(ConsultasDAO,get_db,id):
    consultas_dao = ConsultasDAO(get_db())
    consulta = consultas_dao.visualizar(id= id)
    return consulta

def obter_prontuario_banco_de_dados(ProntuarioDAO,get_db,id):
    prontuario_dao = ProntuarioDAO(get_db())
    prontuario = prontuario_dao.visualizar(id= id)
    print(prontuario)
    return prontuario

def verificar_email_existente(email,UsuarioDAO,get_db):
    usuario_dao = UsuarioDAO(get_db())
    usuario = usuario_dao.visualizar(email=email)
    return len(usuario) > 0 #retorna true se o email existir

def verificar_crm_existente(crm,UsuarioDAO,get_db):
    usuario_dao = UsuarioDAO(get_db())
    usuario = usuario_dao.visualizar(crm=crm)
    return len(usuario) > 0 #retorna true se o crm existir

# Função para autenticar o usuário
def autenticar_usuario(email, senha,UsuarioDAO,get_db,Visualizar_Usuario,Usuario):
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