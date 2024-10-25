from Classes import Menu
class Validacao:
    def validar_nome(self):
        if " " in self.nome:
            print("Nome válido!")
            return True
        print("Nome inválido!")
        return False 

    def validar_cpf(self):
        if len(self.cpf) == 14 and self.cpf[3] == "." and self.cpf[7] == "." and self.cpf[11] == "-":
            print("Formato de CPF válido!")
            return True
        print("Formato de CPF inválido!")
        return 
        
    def validar_telefone(self):
        if (self.telefone[0] == "(" and self.telefone[3] == ")" and
            (self.telefone[8] == "-" or self.telefone[9] == "-") and
            len(self.telefone) in [13, 14]):
            print("Formato de Telefone válido!")
            return True
        print("Formato de Telefone inválido!")
        return False

    def validar_senha(self):
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
        padrao_email = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.(com|org|net|edu|gov)$'
    
        if not re.match(padrao_email, email):
            print('Email invalido!')
            return False
        else:
            print('Email válido!')
            return True