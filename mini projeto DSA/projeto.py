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
print('#'*50)
print()
# --------------------------QUAIS SÃO AS CATEGORIAS DE FILME MAIS ASSISTIDAS:-------------------------------------------
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
print('#'*50)
print()
# --------------------------------QUAIS AS CATEGORIAS COM MAIS FILMES--------------------------------------------------

# Cria a consulta SQL:
consulta2 = "SELECT genres, COUNT(*) FROM titles WHERE type = 'movie' GROUP BY genres"

# RESULTADO 2:
resultado2 = pd.read_sql_query(consulta2, con)

# Vizualiza o resultado:
print(resultado2)

# Convertendo as strings para minúsculo, para facilitar a leitura:
resultado2['genres'] = resultado2['genres'].str.lower().values

# Removendo valroes ausentes:
temp = resultado2['genres'].dropna()

# Criando um vetor usando expressão regular para filtrar as strings:
padrao = r'(?u)\b\w\w+\b'
vetor = CountVectorizer(token_pattern=padrao, analyzer='word').fit(temp)

# Aplicando vetorização ao dataset sem valroes 'na':
bag_generos = vetor.transform(temp)

# Retornando gêneros únicos:
generos_unicos = vetor.get_feature_names()

# Criando o dataframe de gêneros:
generos = pd.DataFrame(bag_generos.todense(), columns=generos_unicos, index=temp.index)

# Vizualizando:
generos.info()

# Calculando o percentual:
generos_percentual = 100 * pd.Series(generos.sum()).sort_values(ascending=False)/generos.shape[0]

# Plot:
plt.figure(figsize=(9, 5))
sns.barplot(x=generos_percentual.values, y=generos_percentual.index, orient='h', palette='terrain')
plt.ylabel('\nGênero')
plt.xlabel('\nPercentual de filmes (%)')
plt.title('\nNúmero (Percentual) de títulos por gênero')
plt.show()
print('#'*100)

# ------------------------------------MEDIANA DE AVALIAÇÃO DOS FILMES POR GÊNEROS-------------------------------------
print('#'*100)
# Consulta sql:
consulta3 = '''
SELECT rating, genres FROM
ratings JOIN titles ON ratings.title_id=titles.title_id
WHERE premiered<=2022 AND type = 'movie'
'''

# Resultado:
resultado3 = pd.read_sql_query(consulta3, con)


# Retornando os gêneros:
def retorna_generos(df):
    df['genres'] = df['genres'].str.lower().values
    temp = df['genres'].dropna()
    vetor = CountVectorizer(token_pattern=padrao, analyzer='word').fit(temp)
    genero_unico = vetor.get_feature_names()
    genero_unico = [genre for genre in genero_unico if len(genre)>1]
    return genero_unico

# Aplicando a função:
gen_unic = retorna_generos(resultado3)

# Criando listas vazias:
genero_count = []
generos_rating = []

# Loop
for itens in generos_unicos:
    # Retorna a contagem de filmes por gênero:
    consulta = f'SELECT COUNT(rating) FROM ratings JOIN titles ON ratings.title_id=titles.title_id ' \
               f'WHERE genres LIKE {itens} AND type=\'movie\''
    resultado = pd.read_sql_query(consulta, con)
    genero_count.append(resultado.values[0][0])

    # Retorna a avaliaçãoe filmes por gênero:
    consulta = 'SELECT rating FROM ratings JOIN titles ON ratings.title_id=titles.title_id ' \
               f'WHERE genres LIKE {itens} and type = \'movie\''
    resultado = pd.read_sql_query(consulta, con)
    generos_rating.append(np.median(resultado['rating']))

# Preparando o dataframe inicial:
df_generos_ratings = pd.DataFrame()
df_generos_ratings['genres'] = generos_unicos
df_generos_ratings['count'] = genero_count
df_generos_ratings['rating'] = df_generos_ratings
