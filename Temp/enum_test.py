from enum import Enum

class DiasSemana(Enum):
    SEGUNDA=1
    TERÇA=2
    QUARTA=3
    QUINTA=4
    SEXTA=5
    SABADO=6
    DOMINGO=7
print(DiasSemana.DOMINGO.value)
print(DiasSemana.DOMINGO.name)
for i in DiasSemana:
    print(i)