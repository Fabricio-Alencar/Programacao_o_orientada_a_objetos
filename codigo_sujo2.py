# Constantes que serão substituídas por Enum
STATUS_PENDENTE = 1
STATUS_EM_PROGRESSO = 2
STATUS_CONCLUIDO = 3

# Variável global desnecessária
historico_global = []

class Tarefa:
    def __init__(self, descricao, prazo, status=STATUS_PENDENTE):
        self.descricao = descricao
        self.prazo = prazo
        self.status = status
        # Uso de variável global desnecessária para armazenar o histórico
        global historico_global
        historico_global.append(f"Tarefa '{self.descricao}' criada com status {status}")
        self.historico = []

    # Método longo com várias responsabilidades
    def atualizar_status(self, novo_status):
        # Gambiarra: Coloquei aqui esse código para evitar erros, mas sei que deveria estar separado
        if novo_status not in [STATUS_PENDENTE, STATUS_EM_PROGRESSO, STATUS_CONCLUIDO]:
            return "Status inválido"
        
        if self.status == novo_status:
            return "Status já está como " + str(novo_status)
        
        self.status = novo_status
        # Adiciona ao histórico global e local
        global historico_global
        historico_global.append(f"Status da tarefa '{self.descricao}' alterado para {novo_status}")
        self.historico.append(f"Status alterado para {novo_status}")

    # Método com código duplicado
    def adicionar_observacao(self, observacao):
        if len(observacao) > 100:
            return "Observação muito longa"  # Código duplicado
        self.historico.append(f"Observação: {observacao}")

    # Método com lógica complexa, difícil de ler
    def exibir_tarefa(self):
        print(f"Tarefa: {self.descricao}")
        print(f"Prazo: {self.prazo}")
        print(f"Status: {self.status}")
        print("Histórico Local:")
        for evento in self.historico:
            print(f"  - {evento}")
        
        # Exibe o histórico global desnecessário
        print("Histórico Global:")
        for evento in historico_global:
            print(f"  - {evento}")

# Simulação de uso do código com problemas
tarefa = Tarefa("Entregar relatório", "2024-10-30")
tarefa.atualizar_status(STATUS_EM_PROGRESSO)
tarefa.adicionar_observacao("Relatório precisa ser revisado")
tarefa.exibir_tarefa()
