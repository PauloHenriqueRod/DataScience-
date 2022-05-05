import sqlite3

# Cria uma conexão com o Banco de Dados
# Se o banco de dados não existir, ele é criado neste momento
con = sqlite3.connect('estudos.db')
print(type(con))

# Criando um cursor
# Um cursor permite percorrer todos os registros em um conjunto de dados
cur = con.cursor()

# Cria uma instrução SQL
sql_create = 'create table cursos ' \
             '(id integer primary key, ' \
             'titulo varchar(100), ' \
             'categoria varchar(140))'

# Executando a instrução SQL no cursor
cur.execute(sql_create)

# Criando outra setença SQL para inserir registros
sql_insert = 'insert into cursos values (?, ?, ?)'

# Dados
recset = [(1000, 'Ciência de dados', 'Data Science'),
         (1001, 'Big Data Fundamentos', 'Big Data'),
         (1002, 'Python Fundamentos', 'Análise de dados')]

# Inserindo os registros
for rec in recset:
    cur.execute(sql_insert, rec)

# Grava a transição
con.commit()

# Criando outra setença sql para selecionar registros
sql_select = 'select * from cursos'

# Seleciona todos os registros e recupera os registros
cur.execute(sql_select)
dados = cur.fetchall()

# Mostra
for linha in dados:
    print('Curso Id: %d, Titulo: %s, Categoria: %s' % linha)

# Gerando outros registros
recset = [(1003, 'Gestão de dados com MongoDB', 'Big Data'),
          (1004, 'R Fundamentos', 'Análise de dados')]

# Inserindo os registros
for rec in recset:
    cur.execute(sql_insert, rec)

# Gravando a transação
con.commit()

# Seleciona todos os registros
cur.execute('select * from cursos')

# Recupera os resultados
recset = cur.fetchall()

# Mostra
for rec in recset:
    print('Curso Id: %d, Titulo: %s, Categoria: %s' % rec)

# Fecha a conexão
con.close()
