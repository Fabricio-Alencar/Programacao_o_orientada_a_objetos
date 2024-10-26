from datetime import datetime
from enum import Enum
# Enum para substituit as constantes
class StatusTarefa(Enum):
    PENDENTE = 1
    EM_PROGRESSO = 2
    CONCLUIDO = 3
# função de validação de texto(evita código duplicado)
def validar_texto(texto,max_len,nome_campo):
    if len(texto)> max_len:
        raise ValueError(f"{nome_campo} não pode ter mais de {max_len} caracteres.")
        
def atualizar_status(status,descricao,novo_status):
        if novo_status not in [StatusTarefa.PENDENTE, StatusTarefa.EM_PROGRESSO, StatusTarefa.CONCLUIDO]:
            return "Status inválido!"
        
        if status == novo_status:
            return "Status já está como " + str(novo_status)
        
        return novo_status
class Tarefa:
    def __init__(self, descricao, prazo, status=StatusTarefa.PENDENTE):
        validar_texto(descricao,100,"descrição")
        self.descricao = descricao
        self.prazo = self._validar_prazo(prazo)
        self.status =status
        self.historico =[]
        self._adicionar_historico(f"Tarefa '{self.descricao}' criada com status {self.status.name}")
        
    def _validar_prazo(self,prazo):
        try:
            return datetime.strptime(prazo, "%Y-%m-%d")
        except ValueError:
            raise ValueError("Formato de prazo inválido!")
    def _adicionar_historico(self,mensagem):
        self.historico.append(mensagem)
    def iniciar(self):
        self.status = atualizar_status(self.status, self.descricao, StatusTarefa.EM_PROGRESSO)
        self._adicionar_historico(f"Tarefa '{self.descricao}' iniciada com sucesso!")
    def concluir(self):
        self.status = atualizar_status(self.status,self.descricao, StatusTarefa.CONCLUIDO)
        self._adicionar_historico(f"Tarefa '{self.descricao}' concluida com sucesso!")
    def exibir_historico(self):
        print("Histórico:")
        for evento in self.historico:
            print(f"  - {evento}")
    def modificar_status(self, novo_status):
        resultado = atualizar_status(self.status, self.descricao, novo_status)
        if isinstance(resultado, StatusTarefa):
            self.status = resultado
            self._adicionar_historico(f"Status alterado para {self.status.name}")
        else:
            print(resultado)

        atualizar_status(self.status,self.descricao,novo_status)

class ListaTarefas:
    def __init__(self):
        self.tarefas = []

    def adicionar_tarefas(self,descricao,prazo):
        nova_tarefa=Tarefa(descricao,prazo)
        self.tarefas.append(nova_tarefa)
        print(f"Tarefa '{descricao}' adicionada com sucesso!")

    def remover_tarefa(self,descricao):
        for tarefa in self.tarefas:
            if tarefa.descricao==descricao:
               self.tarefas.remove(tarefa) 
               return f"Tarefa '{descricao}' removida com sucesso!"
    
        return f"Tarefa '{descricao}' não encontrada!"
                
    def listar_tarefas(self):
        if not self.tarefas:
            print(f"Não existem tarefas para exibir!")
        else:
            print("Lista de Tarefas: ")
            for tarefa in self.tarefas:
                print(f" - {tarefa.descricao} | Prazo: {tarefa.prazo.strftime('%Y-%m-%d')} | Status: {tarefa.status.name}")

if __name__ == "__main__":
    lista = ListaTarefas()

    # Testando a adição de tarefas 

    lista.adicionar_tarefas("Estudar Python", "2023-12-31")
    lista.adicionar_tarefas("Fazer compras", "2023-11-15")
    lista.listar_tarefas()

    # Iniciar e concluir tarefa
    tarefa1 = lista.tarefas[0]
    tarefa1.iniciar()

    tarefa1.concluir()
  
    tarefa1.exibir_historico() 
 
    #  modificação de status
    tarefa1.modificar_status(StatusTarefa.PENDENTE)
    tarefa1.exibir_historico()

    # Testar a remoção de tarefa
    print(lista.remover_tarefa("Fazer compras"))
    lista.listar_tarefas()
    # Testar remoção de tarefa que não existe
    print(lista.remover_tarefa("Ir ao cinema"))
        
