import tkinter as tk  # Importa a biblioteca tkinter e a renomeia como tk para facilitar o uso.
from tkinter import messagebox  # Importa o módulo messagebox para mostrar mensagens ao usuário.
from tkinter import ttk  # Importa o módulo ttk para usar widgets com um estilo mais moderno.

# Classe base para todos os funcionários
class Funcionario:
    def __init__(self, nome, preco_por_hora):  # Método construtor que inicializa o funcionário com nome e preço por hora.
        self.nome = nome  # Atribui o nome do funcionário ao atributo nome.
        self.preco_por_hora = preco_por_hora  # Atribui o preço por hora ao atributo preco_por_hora.

    def calcular_salario(self, horas_trabalhadas):  # Método para calcular o salário com base nas horas trabalhadas.
        return horas_trabalhadas * self.preco_por_hora  # Retorna o salário calculado.

# Classe para funcionários administrativos
class FuncionarioAdministrativo(Funcionario):
    def __init__(self, nome, preco_por_hora, cargo):  # Método construtor que também recebe o cargo.
        super().__init__(nome, preco_por_hora)  # Chama o construtor da classe pai (Funcionario).
        self.cargo = cargo  # Atribui o cargo ao atributo cargo.

# Classe para professores
class Professor(Funcionario):
    def __init__(self, nome, preco_por_hora, disciplina):  # Método construtor que também recebe a disciplina.
        super().__init__(nome, preco_por_hora)  # Chama o construtor da classe pai (Funcionario).
        self.disciplina = disciplina  # Atribui a disciplina ao atributo disciplina.

# Classe para técnicos
class Tecnico(Funcionario):
    def __init__(self, nome, preco_por_hora, especialidade):  # Método construtor que também recebe a especialidade.
        super().__init__(nome, preco_por_hora)  # Chama o construtor da classe pai (Funcionario).
        self.especialidade = especialidade  # Atribui a especialidade ao atributo especialidade.

# Classe que gerencia o sistema de gestão de funcionários
class SistemaGestaoFuncionarios:
    def __init__(self, master):  # Método construtor que inicializa a interface gráfica.
        self.master = master  # Armazena a referência da janela principal.
        self.master.title("Sistema de Gestão de Funcionários")  # Define o título da janela principal.
        
        self.funcionarios = {}  # Cria um dicionário vazio para armazenar os funcionários cadastrados.

        # Campo para nome
        self.label_nome = tk.Label(master, text="Nome:")  # Cria um rótulo para o campo de nome.
        self.label_nome.pack()  # Adiciona o rótulo à janela.
        self.entry_nome = tk.Entry(master)  # Cria um campo de entrada para o nome do funcionário.
        self.entry_nome.pack()  # Adiciona o campo de entrada à janela.

        # Campo para preço por hora
        self.label_preco_por_hora = tk.Label(master, text="Preço por Hora:")  # Cria um rótulo para o campo de preço por hora.
        self.label_preco_por_hora.pack()  # Adiciona o rótulo à janela.
        self.entry_preco_por_hora = tk.Entry(master)  # Cria um campo de entrada para o preço por hora.
        self.entry_preco_por_hora.pack()  # Adiciona o campo de entrada à janela.

        # Seleção do tipo de funcionário
        self.label_tipo = tk.Label(master, text="Tipo de Funcionário:")  # Cria um rótulo para a seleção do tipo de funcionário.
        self.label_tipo.pack()  # Adiciona o rótulo à janela.
        self.tipo_var = tk.StringVar(value="Administrativo")  # Cria uma variável para armazenar o tipo de funcionário selecionado.
        self.radio_admin = tk.Radiobutton(master, text="Administrativo", variable=self.tipo_var, value="Administrativo")  # Botão de opção para "Administrativo".
        self.radio_admin.pack()  # Adiciona o botão de opção à janela.
        self.radio_professor = tk.Radiobutton(master, text="Professor", variable=self.tipo_var, value="Professor")  # Botão de opção para "Professor".
        self.radio_professor.pack()  # Adiciona o botão de opção à janela.
        self.radio_tecnico = tk.Radiobutton(master, text="Técnico", variable=self.tipo_var, value="Técnico")  # Botão de opção para "Técnico".
        self.radio_tecnico.pack()  # Adiciona o botão de opção à janela.

        # Campo para informações adicionais
        self.label_info_adicional = tk.Label(master, text="Info Adicional (Cargo/Disciplina/Especialidade):")  # Rótulo para informações adicionais.
        self.label_info_adicional.pack()  # Adiciona o rótulo à janela.
        self.entry_info_adicional = tk.Entry(master)  # Campo de entrada para informações adicionais.
        self.entry_info_adicional.pack()  # Adiciona o campo de entrada à janela.

        # Botão para cadastrar funcionário
        self.button_cadastrar = tk.Button(master, text="Cadastrar Funcionário", command=self.cadastrar_funcionario)  # Botão para cadastrar funcionário.
        self.button_cadastrar.pack()  # Adiciona o botão à janela.

        # Botão para listar funcionários
        self.button_listar = tk.Button(master, text="Listar Funcionários", command=self.listar_funcionarios)  # Botão para listar funcionários cadastrados.
        self.button_listar.pack()  # Adiciona o botão à janela.

        # Botão para calcular salário
        self.button_calcular_salario = tk.Button(master, text="Calcular Salário", command=self.abrir_calculo_salario)  # Botão para calcular o salário de um funcionário.
        self.button_calcular_salario.pack()  # Adiciona o botão à janela.

    def cadastrar_funcionario(self):  # Método para cadastrar um novo funcionário.
        nome = self.entry_nome.get()  # Obtém o nome do campo de entrada.
        preco_por_hora = float(self.entry_preco_por_hora.get())  # Obtém o preço por hora e converte para float.
        tipo = self.tipo_var.get()  # Obtém o tipo de funcionário selecionado.
        info_adicional = self.entry_info_adicional.get()  # Obtém informações adicionais do campo de entrada.

        # Criação do objeto de acordo com o tipo de funcionário
        if tipo == "Administrativo":  # Se o tipo for "Administrativo".
            funcionario = FuncionarioAdministrativo(nome, preco_por_hora, info_adicional)  # Cria um objeto FuncionarioAdministrativo.
        elif tipo == "Professor":  # Se o tipo for "Professor".
            funcionario = Professor(nome, preco_por_hora, info_adicional)  # Cria um objeto Professor.
        elif tipo == "Técnico":  # Se o tipo for "Técnico".
            funcionario = Tecnico(nome, preco_por_hora, info_adicional)  # Cria um objeto Tecnico.

        # Armazenar o funcionário no dicionário
        self.funcionarios[nome] = funcionario  # Adiciona o funcionário ao dicionário usando o nome como chave.
        messagebox.showinfo("Sucesso", f"Funcionário {nome} cadastrado com sucesso!")  # Mostra uma mensagem de sucesso.

        self.limpar_campos()  # Limpa os campos de entrada após o cadastro.

    def listar_funcionarios(self):  # Método para listar todos os funcionários cadastrados.
        self.janela_funcionarios = tk.Toplevel(self.master)  # Cria uma nova janela para listar funcionários.
        self.janela_funcionarios.title("Funcionários Cadastrados")  # Define o título da nova janela.

        # Criar a tabela
        self.tree = ttk.Treeview(self.janela_funcionarios, columns=("Nome", "Tipo", "Preço por Hora"), show='headings')  # Cria uma tabela para exibir os funcionários.
        self.tree.heading("Nome", text="Nome")  # Define o cabeçalho da coluna "Nome".
        self.tree.heading("Tipo", text="Tipo")  # Define o cabeçalho da coluna "Tipo".
        self.tree.heading("Preço por Hora", text="Preço por Hora")  # Define o cabeçalho da coluna "Preço por Hora".
        self.tree.pack()  # Adiciona a tabela à janela.

        for nome, funcionario in self.funcionarios.items():  # Itera sobre os funcionários cadastrados.
            tipo = type(funcionario).__name__  # Obtém o tipo do funcionário.
            preco_por_hora = funcionario.preco_por_hora  # Obtém o preço por hora do funcionário.
            self.tree.insert("", "end", values=(nome, tipo, preco_por_hora))  # Insere os dados do funcionário na tabela.

    def abrir_calculo_salario(self):  # Método para abrir a janela de cálculo de salário.
        self.janela_calculo = tk.Toplevel(self.master)  # Cria uma nova janela para calcular o salário.
        self.janela_calculo.title("Calcular Salário")  # Define o título da nova janela.

        # Seleção do funcionário
        self.label_funcionario = tk.Label(self.janela_calculo, text="Selecione o Funcionário:")  # Rótulo para selecionar o funcionário.
        self.label_funcionario.pack()  # Adiciona o rótulo à nova janela.
        self.combo_funcionario = ttk.Combobox(self.janela_calculo, values=list(self.funcionarios.keys()))  # Cria um combo box com os nomes dos funcionários cadastrados.
        self.combo_funcionario.pack()  # Adiciona o combo box à nova janela.

        # Campo para horas trabalhadas
        self.label_horas = tk.Label(self.janela_calculo, text="Horas Trabalhadas:")  # Rótulo para o campo de horas trabalhadas.
        self.label_horas.pack()  # Adiciona o rótulo à nova janela.
        self.entry_horas = tk.Entry(self.janela_calculo)  # Campo de entrada para as horas trabalhadas.
        self.entry_horas.pack()  # Adiciona o campo de entrada à nova janela.

        # Botão para calcular
        self.button_calcular = tk.Button(self.janela_calculo, text="Calcular", command=self.calcular_salario)  # Botão para calcular o salário.
        self.button_calcular.pack()  # Adiciona o botão à nova janela.

    def calcular_salario(self):  # Método para calcular o salário do funcionário selecionado.
        nome_funcionario = self.combo_funcionario.get()  # Obtém o nome do funcionário selecionado no combo box.
        horas_trabalhadas = float(self.entry_horas.get())  # Obtém as horas trabalhadas e converte para float.

        if nome_funcionario in self.funcionarios:  # Verifica se o funcionário está cadastrado.
            funcionario = self.funcionarios[nome_funcionario]  # Obtém o objeto do funcionário.
            salario = funcionario.calcular_salario(horas_trabalhadas)  # Calcula o salário usando o método da classe Funcionario.
            messagebox.showinfo("Salário Calculado", f"O salário de {nome_funcionario} é: R$ {salario:.2f}")  # Mostra o salário calculado em uma mensagem.
        else:
            messagebox.showerror("Erro", "Funcionário não encontrado.")  # Mostra uma mensagem de erro se o funcionário não for encontrado.

    def limpar_campos(self):  # Método para limpar os campos de entrada.
        self.entry_nome.delete(0, tk.END)  # Limpa o campo de nome.
        self.entry_preco_por_hora.delete(0, tk.END)  # Limpa o campo de preço por hora.
        self.entry_info_adicional.delete(0, tk.END)  # Limpa o campo de informações adicionais.
        self.tipo_var.set("Administrativo")  # Reseta o tipo de funcionário para "Administrativo".

# Inicialização da aplicação
if __name__ == "__main__":  # Verifica se o script está sendo executado diretamente.
    root = tk.Tk()  # Cria a janela principal da aplicação.
    sistema = SistemaGestaoFuncionarios(root)  # Cria uma instância do sistema de gestão de funcionários.
    root.mainloop()  # Inicia o loop principal da interface gráfica.