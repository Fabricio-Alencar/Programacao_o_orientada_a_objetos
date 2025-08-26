import tkinter as tk
from tkinter import ttk
from sist_gestao_funcionario import Funcionario_Administrativo, Professor, Tecnico, ADM_Cadastro, Professor_Cadastro, Tecnico_Cadastro
from tkinter import messagebox  # Importa o módulo messagebox para mostrar mensagens ao usuário.

# Classe que gerencia o sistema de gestão de funcionários
class SistemaGestaoFuncionarios:
    def __init__(self, master):  # Método construtor que inicializa a interface gráfica.
        self.root = master  # Armazena a referência da janela principal.
        self.root.title("Sistema de Gestão de Funcionários")  # Define o título da janela principal.
        self.root.geometry('600x600') # Horizontal x Vertical

        self.pagina0 = tk.Frame(self.root)
        self.pagina1 = None  # Variável global para armazenar a página ativa
        self.pagina2 = None  # Variável global para armazenar a página ativa

        # Cria um dicionário para armazenar os funcionários cadastrados.
        self.funcionarios= {} 

        
        # Criação da primeira página
        self.pagina0.pack(fill="both", expand=True)  # Exibe a primeira página

        etiqueta = tk.Label(self.pagina0, text="Qual função você deseja realizar?", font=("Arial", 16)) 
        etiqueta.pack(pady=20)  # Adiciona a etiqueta e um espaçamento vertical de 20 pixels

        # Botão para cadastrar funcionários
        button = tk.Button(self.pagina0, text='Cadastrar Funcionário', width=20, command=self.pagina_de_cadastro)
        button.pack(pady=20)

        # Botão para listar funcionários
        button = tk.Button(self.pagina0, text="Listar Funcionários", command=self.listar_funcionarios)  
        button.pack(pady=20)  # Adiciona o botão à janela.

        # Botão para calcular salário
        button = tk.Button(self.pagina0, text="Calcular Salário", command=self.abrir_calculo_salario)  
        button.pack(pady=20)  # Adiciona o botão à janela.

        # Botão para fechar programa
        button = tk.Button(self.pagina0, text='Sair', width=20, command=self.root.destroy)
        button.pack(pady=20)

    def pagina_de_cadastro(self):
        self.pagina0.pack_forget()  # Esconde a página 0 
        if self.pagina1:  # Se já existir uma página 1, destrói para evitar sobreposição
            self.pagina1.destroy()
        self.pagina1 = tk.Frame(self.root)  # Cria a página 1
        self.pagina1.pack(fill="both", expand=True)  # Exibe a página 1

        etiqueta = tk.Label(self.pagina1, text="Selecione qual tipo de funcionário\n você deseja cadastrar:", font=("Arial", 16)) 
        etiqueta.pack(pady=20)  
        button = tk.Button(self.pagina1, text='Administrativo', width=20, command=lambda: self.cadastrar(1))  # Cadastrar Administrativos
        button.pack(pady=20)
        button = tk.Button(self.pagina1, text='Professor', width=20, command=lambda: self.cadastrar(2))  # Cadastrar Professores
        button.pack(pady=20)
        button = tk.Button(self.pagina1, text='Técnico', width=20, command=lambda: self.cadastrar(3))  # Cadastrar Técnicos
        button.pack(pady=20)
        button = tk.Button(self.pagina1, text='Voltar', width=20, command=self.voltar_pagina0_1)  # Sair da aplicação
        button.pack(pady=20)

    def cadastrar(self, tipo):
        self.pagina1.pack_forget()  # Esconde a página 1 
        self.cadastrar2(tipo)

    def cadastrar2(self, tipo):
        if self.pagina2:  # Se já existir uma página 2, destrói para evitar sobreposição
            self.pagina2.destroy()
        self.pagina2 = tk.Frame(self.root)  # Cria a página 2
        self.pagina2.pack(fill="both", expand=True)  # Exibe a página 2

        # Label para o título da página
        tk.Label(self.pagina2, text="Funcionário Administrativo" if tipo == 1 else "Professor" if tipo == 2 else "Técnico", font=("Arial", 16)).pack(pady=20)

        # Campos de entrada
        tk.Label(self.pagina2, text='Nome').pack()  # Label para "Nome"
        nome = tk.Entry(self.pagina2)  # Campo de entrada
        nome.pack(pady=5)  # Entrada com espaçamento

        tk.Label(self.pagina2, text='Telefone').pack() 
        telefone = tk.Entry(self.pagina2)  # Campo de entrada
        telefone.pack(pady=5) 

        tk.Label(self.pagina2, text='Horário').pack()  # Caixa de seleção para Horário
        horarios = ["Manhã", "Tarde", "Noturno"]
        horario = ttk.Combobox(self.pagina2, values=horarios, state="readonly")  # Impede a digitação personalizada
        horario.pack(pady=5)
        horario.current(0)  # Define "Manhã" como padrão

        if tipo == 1:  # Funcionário Administrativo
            tk.Label(self.pagina2, text='Setor').pack()  # Caixa de seleção para Setor
            setores = ["Financeiro", "Recursos Humanos", "TI", "Marketing"]
            setor = ttk.Combobox(self.pagina2, values=setores, state="readonly") 
            setor.pack(pady=20)
            setor.current(0) 

            tk.Label(self.pagina2, text='Nível de Acesso').pack()  # Caixa de seleção para Nível de Acesso
            niveis = ["Básico", "Intermediário", "Avançado"]
            nivel = ttk.Combobox(self.pagina2, values=niveis, state="readonly")
            nivel.pack(pady=5)
            nivel.current(0) 

            button_cadastrar = tk.Button(self.pagina2, text="Cadastrar", command=lambda: self.Cadastrar_Administrativo(nome.get(), telefone.get(), horario.get(), setor.get(), nivel.get()))
            button_cadastrar.pack(pady=20)

        elif tipo == 2:  # Professor
            tk.Label(self.pagina2, text='Carga horária (Quantidade de horas/aula semanais)').pack() 
            carga = tk.Entry(self.pagina2)  
            carga.pack(pady=5)

            tk.Label(self.pagina2, text='Salário por hora').pack() 
            salario = tk.Entry(self.pagina2)  
            salario.pack(pady=5)

            button_cadastrar = tk.Button(self.pagina2, text="Cadastrar", command=lambda: self.Cadastrar_Professor(nome.get(), telefone.get(), horario.get(), carga.get(), salario.get()))
            button_cadastrar.pack(pady=20)

        else:  # Técnico
            tk.Label(self.pagina2, text='Especialização').pack() 
            especializacoes = ["Informática", "Mecânica", "Automação Industrial", "Farmácia", "Enfermagem", "Química"]
            especializacao = ttk.Combobox(self.pagina2, values=especializacoes, state="readonly") 
            especializacao.pack(pady=20)
            especializacao.current(0)

            button_cadastrar = tk.Button(self.pagina2, text="Cadastrar", command=lambda: self.Cadastrar_Tecnico(nome.get(),telefone.get(), horario.get(), especializacao.get()))
            button_cadastrar.pack(pady=20)

        # Botão de voltar
        button2 = tk.Button(self.pagina2, text="Voltar", command=self.voltar_pagina_de_cadastro, width=20)
        button2.pack(pady=20)


    def listar_funcionarios(self):  # Método para listar todos os funcionários cadastrados.
        self.janela_funcionarios = tk.Toplevel(self.root)  # Cria uma nova janela para listar funcionários.
        self.janela_funcionarios.title("Funcionários Cadastrados")  # Define o título da nova janela.

        # Criar a tabela
        self.tree = ttk.Treeview(self.janela_funcionarios, columns=("Nome", "Tipo", "Horário", "Telefone", "Carga Horária", "Preço por Hora", "Setor", "Nível de Acesso", "Especialização"), show='headings')  # Cria uma tabela para exibir os funcionários.
        self.tree.heading("Nome", text="Nome")  # Define o cabeçalho da coluna "Nome".
        self.tree.heading("Tipo", text="Tipo")  # Define o cabeçalho da coluna "Tipo".       
        self.tree.heading("Horário", text="Horário")  # Define o cabeçalho da coluna "Horário".
        self.tree.heading("Telefone", text="Telefone")  # Define o cabeçalho da coluna "Telefone".
        self.tree.heading("Carga Horária", text="Carga Horária")  # Define o cabeçalho da coluna "Carga Horária".
        self.tree.heading("Preço por Hora", text="Preço por Hora")  # Define o cabeçalho da coluna "Preço por Hora".
        self.tree.heading("Setor", text="Setor")  # Define o cabeçalho da coluna "Setor".
        self.tree.heading("Nível de Acesso", text="Nível de Acesso")  # Define o cabeçalho da coluna "Nível de Acesso".
        self.tree.heading("Especialização", text="Especialização")  # Define o cabeçalho da coluna "Especialização".
        self.tree.pack()  # Adiciona a tabela à janela.

        for nome, funcionario in self.funcionarios.items():  # Itera sobre os funcionários cadastrados.
            tipo = funcionario.tipo
            horario = funcionario.horario 
            telefone = funcionario.telefone 
            carga_horaria = funcionario.carga if hasattr(funcionario, 'carga') else "X"
            preco_por_hora = funcionario.preco_por_hora if hasattr(funcionario, 'preco_por_hora') else "X"
            setor = funcionario.setor if hasattr(funcionario, 'setor') else "X"
            nivel = funcionario.nivel if hasattr(funcionario, "nivel") else "X"
            especializacao = funcionario.especializacao if hasattr(funcionario, 'especializacao') else "X"

            # Preenche a tabela com os dados do funcionário
            self.tree.insert("", "end", values=(nome, tipo, horario, telefone, carga_horaria, preco_por_hora, setor, nivel, especializacao))






    def abrir_calculo_salario(self):  # Método para abrir a janela de cálculo de salário.
        self.janela_calculo = tk.Toplevel(self.root)  # Cria uma nova janela para calcular o salário.
        self.janela_calculo.title("Calcular Salário")  # Define o título da nova janela.
        self.janela_calculo.geometry('300x100') # Horizontal x Vertical


        # Seleção do funcionário;
        self.label_funcionario = tk.Label(self.janela_calculo, text="Selecione o Funcionário:")  # Rótulo para selecionar o funcionário.
        self.label_funcionario.pack()  # Adiciona o rótulo à nova janela.
        self.combo_funcionario = ttk.Combobox(self.janela_calculo, values=list(self.funcionarios.keys()))  # Cria um combo box com os nomes dos funcionários cadastrados.
        self.combo_funcionario.pack()  # Adiciona o combo box à nova janela.

        # Botão para calcular
        self.button_calcular = tk.Button(self.janela_calculo, text="Calcular", command=self.calcular_salario)  # Botão para calcular o salário.
        self.button_calcular.pack()  # Adiciona o botão à nova janela.

    def calcular_salario(self):  # Método para calcular o salário do funcionário selecionado.
        nome_funcionario = self.combo_funcionario.get()  # Obtém o nome do funcionário selecionado no combo box.

        if nome_funcionario in self.funcionarios:  # Verifica se o funcionário está cadastrado.
            funcionario = self.funcionarios[nome_funcionario]  # Obtém o objeto do funcionário.
            salario = funcionario.calcular_salario()  # Calcula o salário usando o método da classe Funcionario.
            messagebox.showinfo("Salário Calculado", f"O salário de {nome_funcionario} é: R$ {salario:.2f}")  # Mostra o salário calculado em uma mensagem.
        else:
            messagebox.showerror("Erro", "Funcionário não encontrado.")  # Mostra uma mensagem de erro se o funcionário não for encontrado.







    def voltar_pagina_de_cadastro(self):
        self.pagina2.pack_forget()  # Esconde a página de cadastro (página 2)
        self.pagina1.pack(fill="both", expand=True)  # Exibe a página 1 novamente

    def voltar_pagina0_1(self):
        self.pagina1.pack_forget()
        self.pagina0.pack(fill="both", expand=True)  # Exibe a primeira página novamente

    def voltar_pagina0_2(self):
        self.pagina2.pack_forget()
        self.pagina0.pack(fill="both", expand=True)  # Exibe a primeira página novamente

    def Cadastrar_Administrativo(self, nome, telefone, horario, setor, nivel):
        if not nome:  # Se o campo 'Nome' estiver vazio
            messagebox.showerror("Erro", "O campo 'Nome' é obrigatório!")  
            return
        ADM = Funcionario_Administrativo(nome,  horario, telefone, "Funcionário Administrativo", setor, nivel)
        ADM_Cadastro.append(ADM)  # Adiciona o funcionário à lista de dados
        print(f"Cadastro realizado: {nome}, {telefone}, {horario}, {setor}, {nivel}")
        self.funcionarios[nome] = ADM  # Adiciona o funcionário ao dicionário usando o nome como chave.
        messagebox.showinfo("Sucesso", f"Funcionário {nome} cadastrado com sucesso!")  # Mostra uma mensagem de sucesso.
        self.voltar_pagina0_2()  # Função para voltar para a página 1 após o cadastro

    def Cadastrar_Professor(self, nome, telefone, horario, carga, salario):
        try: #Verifica se o usuário colocou números nas entradas de carga horária e preço por hora (salario)
            if not nome:  # Se o campo 'Nome' estiver vazio
                messagebox.showerror("Erro", "O campo 'Nome' é obrigatório!")  
                return
            carga = float(carga.replace(",", ".")) #Tranforma a string em float e virgulas em pontos
            salario = float(salario.replace(",", ".")) #Transforma a string em float
            Prof = Professor(nome, horario, telefone, "Professor", carga, salario)
            Professor_Cadastro.append(Prof) 
            print(f"Cadastro realizado: {nome}, {telefone}, {horario}, {carga}, {salario} ")
            self.funcionarios[nome] = Prof # Adiciona o funcionário ao dicionário usando o nome como chave.
            messagebox.showinfo("Sucesso", f"Funcionário {nome} cadastrado com sucesso!") 
            self.voltar_pagina0_2()  
        except ValueError:  # Se ocorrer um erro de conversão, não é um número válido
            messagebox.showerror("Erro", "Por favor, coloque números nas entradas de [Carga Horária] e [Preço por Hora].")  # Exibe mensagem de erro

    def Cadastrar_Tecnico(self, nome, telefone, horario, especializacao):
        if not nome:  # Se o campo 'Nome' estiver vazio
            messagebox.showerror("Erro", "O campo 'Nome' é obrigatório!")  
            return
        Tecn = Tecnico(nome, horario, telefone, "Técnico", especializacao)
        Tecnico_Cadastro.append(Tecn) 
        print(f"Cadastro realizado: {nome}, {telefone}, {horario}, {especializacao} ")
        self.funcionarios[nome] = Tecn  # Adiciona o funcionário ao dicionário usando o nome como chave.
        messagebox.showinfo("Sucesso", f"Funcionário {nome} cadastrado com sucesso!") 
        self.voltar_pagina0_2() 

# Inicialização da aplicação
if __name__ == "__main__":  # Verifica se o script está sendo executado diretamente.
    i = 1
    root = tk.Tk()  # Cria a janela principal da aplicação.
    sistema = SistemaGestaoFuncionarios(root)  # Cria uma instância do sistema de gestão de funcionários.
    root.mainloop()  # Inicia o loop principal da interface gráfica.
