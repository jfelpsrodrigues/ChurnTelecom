import pandas as pd
import plotly.express as px

# Importação e Visualização dos Dados
tabela = pd.read_csv("telecom_users.csv").drop("Unnamed: 0", axis=1)
print(tabela)
print('='*100)

# Tratamento da Base de Dados
tabela['TotalGasto'] = pd.to_numeric(tabela['TotalGasto'], errors='coerce')
tabela = tabela.dropna(how='all', axis=1)
tabela = tabela.dropna(how='any', axis=0)
print(tabela.info())

# Analisando os dados
print(tabela['Churn'].value_counts())
print('='*100)
print(tabela['Churn'].value_counts(normalize=True))
print('='*100)



for coluna in tabela.columns:
    if coluna == 'IDCliente':
        pass
    elif coluna == 'Churn':
        pass
    else:
        graf = px.histogram(tabela, x=coluna, color='Churn')
        graf.show()
        print(tabela.pivot_table(index='Churn', columns=coluna, aggfunc='count')['IDCliente'])