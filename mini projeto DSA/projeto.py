# MINI-PROJETO do curso python fundamento para ciência de dados - DATA SCIENCE ACADEMY

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
print('-'*100)

# Criando um gráfico com 3 categorias principais + categoria que abrange todas as outras:
others = {}

# Craição da categoria 'others'
others['COUNT'] = resultado1[resultado1['percentual'] < 5]['COUNT'].sum()

# Gravando percentual:
others['percentual'] = resultado1[resultado1['percentual'] < 5]['percentual'].sum()

# Ajustando o nome:
others['type'] = 'others'
# print(others)
# Filtrando o dataframe de resultados:
resultado1 = resultado1[resultado1['percentual']>5]

# Adicionando a categoria 'others'
resultado1 = resultado1.append(others, ignore_index=True)

# Ordenando resultado:
resultado1 = resultado1.sort_values(by='COUNT', ascending=False)
print(resultado1)

# Ajuste das labels:
labels=[str(resultado1['type'][i])+' '+'['+str(round(resultado1['percentual'][i], 2))+'%'+']' for i in resultado1.index]


# Criando figura:
f = plt.figure()

# PiePlot:
plt.pie(resultado1['COUNT'], labeldistance=1, radius=1.5, wedgeprops=dict(width=0.4))
plt.legend(labels=labels, loc = 'center', prop={'size': 8})
plt.title("Distribuição de Títulos", loc='Center', fontdict={'fontsize': 10, 'fontweight': 10})
plt.show()