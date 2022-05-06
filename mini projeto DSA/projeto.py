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
