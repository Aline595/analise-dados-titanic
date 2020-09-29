import pandas as pd
from google.colab import files

uploaded = files.upload( )

dados1 = pd.read_excel('Planilhas_texte.xls')# cada tipo muda o read(read_csv)
daos1
# printa uma lista comos dados da planilha

files.dowload('Planilha_texte.xls')
# baixa planilha que ele formou 

print(dados1.shape) #mostra as dimensoes do tamanho da planilha(linha, coluna)
print(dados1.head(), "\n") #mostra as cinco primeiras linhas da planilha
print(dados1.head(10)) #mostra o número de linhas que se pode ver da planilha

print(dados2.describe())

alunos = {'Nome':['Marcelo','Lucas','Cynthia','Helena'],
'Media':[4,7,5.5,9],
'Status':['Reprovado','Aprovado','Reprovado','Aprovado']}

df1 = pd.DataFrame(alunos) # base de dados em tabela
print(df1.shape)
print(df1.head())
print(df1.describe())

df1[['Nome']] # mostra parte do data frame
df1['Nome'] # mostra uma serie do dataframe 

df1.loc[[1,3]] #linhas 1 e 3
df1.loc[1:3] #linhas 1 a 3

df1.loc[df1['Status'] == 'Aprovado']

#Quem sobreviveu por classe social

# Todos sobreviventes 
sobreviventes = dados2[['Survived', 'Pclass']].loc[dados2['Survived'] == 1]
sobreviventes.describe( )

# separar por classe 
sobreviventes1 = sobreviventes.loc[sobreviventes['Pclass'] == 1]
sobreviventes2 = sobreviventes.loc[sobreviventes['Pclass'] == 2]
sobreviventes3 = sobreviventes.loc[sobreviventes['Pclass'] == 3]
print(sobreviventes1.describe())
print(sobreviventes2.describe())
print(sobreviventes3.describe())

# total de pessoas em cada classe
dados2['Pclass'].value_counts()