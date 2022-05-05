import sqlite3

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
create_table()

# Inserir linha
data_insert()
