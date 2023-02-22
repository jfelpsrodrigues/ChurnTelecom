# Importação e Visualização dos Dados
import pandas as pd
import plotly.express as px

tabela = pd.read_csv("telecom_users.csv").drop("Unnamed: 0", axis=1)
print("Tabela de Dados:")
print("-"*100)
print(tabela)
print("-"*100)

# Tratamento da Base de Dados
tabela['TotalGasto'] = pd.to_numeric(tabela['TotalGasto'], errors='coerce')
tabela = tabela.dropna(how='all', axis=1)
tabela = tabela.dropna(how='any', axis=0)
print("-"*100)
print(tabela.info())
print("-"*100)

# Analisando os dados
print(tabela['Churn'].value_counts())
print(tabela['Churn'].value_counts(normalize=True))

# Criando gráficos para a análise
for coluna in tabela.columns:
    if coluna == 'IDCliente':
        pass
    elif coluna == 'Churn':
        pass
    else:
        graf = px.histogram(tabela, x=coluna, color='Churn')
        graf.show()
        print(tabela.pivot_table(index='Churn', columns=coluna, aggfunc='count')['IDCliente'])
