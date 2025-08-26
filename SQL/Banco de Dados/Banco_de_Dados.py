import sqlite3
conn = sqlite3.connect("teste.db")  #Cria ou abre novamente a conexão
cursor = conn.cursor()

#criar tabela
cursor.execute('''CREATE TABLE IF NOT EXISTS users(
                nome TEXT NOT NULL, cpf TEXT NOT NULL)
                ''')

#insert
nome1 = "Samuel Maracas"
cpf1 = "123456789"
nome2 = "Nicoli Barros"
cpf2 = "123456780"
nome3 = "Chou Beatriz"
cpf3 = "123456788"
cursor.execute('''INSERT INTO users (nome,cpf) VALUES
                (?,?)''', (nome1,cpf1))
cursor.execute('''INSERT INTO users (nome,cpf) VALUES
                (?,?)''', (nome2,cpf2))
cursor.execute('''INSERT INTO users (nome,cpf) VALUES
                (?,?)''', (nome3,cpf3))

#Atualização de Dados (Transforma todos os dados existentes em um definido)
#cursor.execute('''UPDATE users SET nome = "Matheus Diniz", cpf = "123456784"''')

#Deleta o dados definido
#cursor.execute('''DELETE FROM users WHERE nome="Matheus Diniz"''')

#SELECT
cursor.execute('''SELECT * FROM users''')
linha = cursor.fetchone() #Pegar apenas um
print(linha)
linha = cursor.fetchone() #Se executar dnv pega a segunda, pq ao terminar de executar a primeira ele aponta pra proxima linha
print(linha)

for linha in cursor.fetchmany(4): #imprime n linhas
    print(linha)

for linha in cursor.fetchall(): #imprime todas as linhas
    print(linha)
 
conn.commit() #serve para atualizar as mudanças feitas
conn.close() #fecha a conexão com o banco de dados

