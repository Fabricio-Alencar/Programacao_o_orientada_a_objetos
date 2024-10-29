
class Validacoes:
    def validar_nome(nome):
        # Verifica se o nome contém espaços
        if " " in self.nome:
            # Verifica se o nome não contém números
            if any(char.isdigit() for char in self.nome):
                print("Nome inválido! O nome não pode conter números.")
                return False
            
            print("Nome válido!")
            return True
        
        print("Nome inválido! O nome deve conter pelo menos um espaço.")
        return False

    def validar_cpf(cpf):
        if len(self.cpf) == 14 and self.cpf[3] == "." and self.cpf[7] == "." and self.cpf[11] == "-":
            print("Formato de CPF válido!")
            return True
        print("Formato de CPF inválido!")
        return 
        
    def validar_telefone(telefone):
        if (self.telefone[0] == "(" and self.telefone[3] == ")" and
            (self.telefone[8] == "-" or self.telefone[9] == "-") and
            len(self.telefone) in [13, 14]):
            print("Formato de Telefone válido!")
            return True
        print("Formato de Telefone inválido!")
        return False

    def validar_senha(senha):
        if len(self.Pessoa.__senha) < 8:
            print("A senha deve ter pelo menos 8 caracteres.")
            return False  # senha menor q 8 digitos
    
        if not re.search(r'[A-Z]', self.Pessoa.__senha):
            print("A senha deve conter pelo menos uma letra maiúscula.")
            return False # senha não possui letra maiúscula
    
        if not re.search(r'[a-z]', self.Pessoa.__senha):
            print("A senha deve conter pelo menos uma letra minúscula.")
            return False # senha não possui letra minúscula
    
        if not re.search(r'\d', self.Pessoa.__senha):
            print("A senha deve conter pelo menos um número.")
            return False # senha não possui números
        if not re.search(r'[!@#$%^&*()_+{}\[\]:;"\'<>,.?/~`-]', self.Pessoa.__senha):
            print("A senha deve conter pelo menos um caractere especial.")
            return 5 # senha não possui caractere especial
        
        print("Senha válida!")
        return True


    def validar_email(email):
        padrao_email = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.(com|org|net|edu|gov)$' #formato de um email
    
        if not re.match(padrao_email, self.Pessoa.email):
            print('Email invalido!')
            return False
        else:
            print('Email válido!')
            return True
    def validar_tipo(tipo):
        if self.Pessoa.tipo == paciente or self.Pessoa.tipo == profissional:
            return True
        else:
            return False
    def validar_crm(crm):
        # Padrão de regex para validar o CRM
        padrao_crm = r'^CRM-[A-Z]{2}-\d{5}$'
        
        # Verifica se o CRM corresponde ao padrão
        if re.match(padrao_crm, self.crm):
            print("CRM válido!")
            return True
        else:
            print("CRM inválido! O formato deve ser 'CRM-XX-12345', onde 'XX' é a sigla do estado e '12345' é um número.")
            return False
    