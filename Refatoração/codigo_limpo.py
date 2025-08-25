# Algumas constantes (serão substituídas por Enum)
# Essas constantes são usadas em vários lugares
from abc import ABC, abstractmethod
from enum import Enum
class SituacaoEstudante(Enum):
    APROVADO = 1
    REPROVADO = 2
    RECUPERACAO = 3
class NotaInvalidaError(Exception):
    pass
class FrequanciaInvalidaErro(Exception):
    pass

def validar_valor(valor,minimo,maximo,nome_campo):
    if valor<minimo or valor>maximo:
        raise ValueError(f"{nome_campo} deve estar entre {minimo} e {maximo}")

def calcular_situacao_final(nota, frequencia):
    if nota >= 7 and frequencia >= 75:
        return SituacaoEstudante.APROVADO
    elif nota >= 5 and frequencia >= 50:
        return SituacaoEstudante.RECUPERACAO
    else:
        return SituacaoEstudante.REPROVADO

class RegistrarNotas:
    def __init__(self):
        self.notas=[]

    def adicionar_notas(self,nota):
        validar_valor(nota,0,10,'Nota')
        self.notas.append(nota)

    def calcular_media(self):
        if not self.notas:
            return 0.0
        else:
            return sum(self.notas)/len(self.notas)

class Estudante:
    def __init__(self, nome, idade, matricula):
        self.nome = nome
        self.idade = idade
        self.matricula = matricula
        self.registro_notas=RegistrarNotas()

    def definir_frequencia(self,frequencia):
        validar_valor(frequencia,0,100,"Frequência")
        self.frequencia=frequencia

    def avaliar_situacao(self):
        media=self.registro_notas.calcular_media()
        return media

    def formatar_mensagem_situacao(self):
        situacao= self.avaliar_situacao()
        if situacao ==SituacaoEstudante.APROVADO:
            return f'{self.nome} esta aprovado!'
        elif situacao ==SituacaoEstudante.RECUPERACAO:
            return f'{self.nome} esta de recuperação!'
        else:
            return f'{self.nome} foi reprovado!'

class Notificacao(ABC):
    @abstractmethod
    def enviar_notificacao(self,mensagem):
        pass

class NotificacaoEmail(Notificacao):
    def enviar_notificacao(self,mensagem):
        print(f'enviando email...{mensagem}')

class NotificacaoSMS(Notificacao):
    def enviar_notificacao(self,mensagem):
        print(f'enviando SMS...{mensagem}')

class ServicoNotificacao:
    def __init__(self, notificadores):
        self.notificadores = notificadores
    def notificar(self,mensagem):
        for notificador in self.notificadores:
            notificador.enviar_notificacao(mensagem)

if __name__=="__main__":
    estudante = Estudante('Carlos',20,'12345')
    estudante.registro_notas.adicionar_notas(8)
    estudante.registro_notas.adicionar_notas(5)
    estudante.definir_frequencia(80)

    mensagem = estudante.formatar_mensagem_situacao()
    print(mensagem)
    #enviar notificações
    notificacao_email = NotificacaoEmail()
    notificacao_sms= NotificacaoSMS()
    servico_notificacao = ServicoNotificacao([notificacao_email,notificacao_sms])
    servico_notificacao.notificar(mensagem)


