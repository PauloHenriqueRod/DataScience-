import sqlite3
import datetime
import random
import time

# Criando uma conexão
con = sqlite3.connect('treino.db')

# Criando um cursor
c = con.cursor()


# Função de criar tabela
def create_table():
    c.execute('CREATE TABLE IF NOT EXISTS produtos(id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, date TEXT,'
              'prod_name TEXT, valor REAL)')


# Função para inserir uma linha
def data_insert():
    c.execute("INSERT INTO produtos VALUES (10, '2022-05-04 10:33:25', 'Teclado', 90)")
    con.commit()
    c.close()
    con.close()


# Criar tabela
# create_table()
# Inserir linha
# data_insert()

# Usando variáveis para inserir dados
def data_insert_var():
    new_date = datetime.datetime.now()
    new_produte = 'Notebook'
    new_valor = random.randrange(3000, 10000)
    c.execute("INSERT INTO produtos (date, prod_name, valor) VALUES (?, ?, ?)", (new_date, new_produte, new_valor))
    con.commit()


# for i in range(10):
#    data_insert_var()
#    time.sleep(1)

# Leitura de dados:
def todos_dados():
    c.execute("SELECT * FROM PRODUTOS")
    for linha in c.fetchall():
        print(linha)


# Leitura de dados específicos:
def leitura_especifica():
    c.execute("SELECT * FROM PRODUTOS WHERE valor > 5000")
    for linha in c.fetchall():
        print(linha)


# Leitura de colunas específicas:
def leitura_coluna():
    c.execute("SELECT * FROM PRODUTOS")
    for linha in c.fetchall():
        print(linha[3])


todos_dados()
print('-='*30)
leitura_especifica()
print('-='*30)
leitura_coluna()

c.close()
con.close()
