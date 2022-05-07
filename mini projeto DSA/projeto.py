import re
import time
import sqlite3

import pandas.core.frame
import pycountry
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib as cm
from sklearn.feature_extraction.text import CountVectorizer
import warnings
warnings.filterwarnings('ignore')
sns.set_theme(style='whitegrid')

# Conecta ao banco de dados:
con = sqlite3.connect('imdb.db')

# Extrai a lista de tabela:
tabelas = pd.read_sql_query("SELECT NAME AS 'Table_name' FROM sqlite_master WHERE type = 'table'", con)

# Tipo do objeto:
print(type(tabelas))

# Vizualiza o resultado:
print(tabelas.head())

# Convertendo dataframe em lista:
tableas = tabelas["Table_name"].values.tolist()

# Percorrendo a lista de tabelas no banco de dados e extraindo o esquema de cada um:
for tabela in tableas:
    consulta = f'PRAGMA TABLE_INFO({tabela})'
    resultado = pd.read_sql_query(consulta, con)
    print(f'Esquema de tabela:\n{tabela}')
    print(resultado)
    print('-'*100)
    print('\n')

# QUAIS SÃO AS CATEGORIAS DE FILME MAIS ASSISTIDAS:
print('-'*100)
print('MOSTRANDO QUAIS SÃO AS CATEGORIAS DE FILMES MAIS ASSISTIDAS')
print('-'*100)
# Criando consulta SQL:
consulta1 = 'SELECT type, COUNT(*) AS COUNT FROM titles GROUP BY type'
# Extraindo resultado:
resultado1 = pd.read_sql_query(consulta1, con)
# print(resultado1)

# Calculando percentual:
resultado1['percentual'] = (resultado1['COUNT']/resultado1['COUNT'].sum())*100
print(resultado1)
