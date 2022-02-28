#!/usr/bin/env python
# coding: utf-8

# In[1]:


# importando a biblioteca pandas 
import pandas as pd


# In[2]:


# abrindo o dataset
df = pd.read_csv('datatran2021.csv', sep=';' , encoding='latin-1')
pd.set_option('display.max_columns', None)


# In[3]:


# dimensões do dataset
df.shape


# In[4]:


# filtrandro dados do estado de Minas Gerais
df.loc[(df['uf'] == 'MG')]


# In[5]:


# novo_df recebe dados do estado de Minas Gerais
novo_df = df.loc[(df['uf'] == 'MG')]


# In[6]:


# salvando os dados de Minas Gerais em arquivo csv
novo_df.to_csv('minasgerais2021.csv',index=False)


# In[7]:


# abrindo novo arquivo com os dados de Minas Gerais
df = pd.read_csv('minasgerais2021.csv')


# In[8]:


# dimensões do dataset (linhas,colunas)
df.shape


# In[9]:


# colunas do dataset
df.columns


# In[12]:


# amostras das primeiras linhas 
df.head() 


# In[10]:


# valores ausentes
df.isnull().sum()


# In[11]:


acidentes = df['id'].count()
print(f"Total de acidentes em 2021:",acidentes)


# In[72]:


df['delegacia'].unique()


# In[73]:


df['regional'].unique()


# In[74]:


df['uop'].unique


# In[13]:


# amostras das últimas 10 linhas
df.tail(10)


# In[14]:


# valores estatísticos básicos
df.describe()
#count -> total registros
#mean -> média
#std -> desvio padrão
#min -> valor mínimo encontrado
#25% 
#50% -> pode se dizer a mediana
#75%
#max -> valor máximo encontrado


# In[15]:


# ordenando as datas
df.sort_values('data_inversa')


# In[68]:


# soma do total de feridos no estado
feridos = df['feridos'].sum()
print(f"Total de feridos no estado:",feridos)


# In[16]:


# soma do total de mortos no estado
mortos = df['mortos'].sum()
print(f"Total de mortos no estado:",mortos)


# In[69]:


# maior número de feridos em um acidente
df['feridos'].max()


# In[71]:


# localizando o registro do acidente onde houve o maior número de feridos 
df.loc[df['feridos'] == 49]


# In[70]:


# maior número de óbitos em um acidente
df['mortos'].max()


# In[18]:


# localizando os registros de acidentes onde houve o maior número de óbitos 
df.loc[df['mortos'] == 5]


# In[19]:


# soma de pessoas envolvidas nos acidentes
df['pessoas'].sum()


# In[20]:


# soma de ilesos
df['ilesos'].sum()


# In[21]:


# número máximo de pessoas envolvidas no acidente
df['pessoas'].max()


# In[22]:


# localizando o registro do acidente onde teve o maior número de pessoas envolvidas
df.loc[df['pessoas'] == 53]


# In[23]:


# valores da coluna causa_acidente
df['causa_acidente'].unique()


# In[24]:


# agrupamento acidentes por causa
acidente = df.groupby(['causa_acidente']).size().sort_values(ascending=False)
acidente_mais_20 = acidente[acidente>=20]
acidente_mais_20


# In[25]:


# gráfico principais causas de acidente
import matplotlib.pyplot as plt
acidente_mais_20.plot(kind='bar')
plt.xlabel('Causa do Acidente')
plt.ylabel('Quantidade de Acidentes')
plt.title('Acidentes x Cauda do Acidente')
plt.show()


# In[26]:


# agrupamento de causa acidente x mortos
causa_acidente = df.groupby(by='causa_acidente').sum()['mortos']


# In[27]:


# filtrando registro onde teve óbitos
causa_maior_0 = causa_acidente[causa_acidente>0]


# In[28]:


# ordenando os registros do maior para o menor
causa_maior_0.sort_values(ascending=False)


# In[29]:


# primeiras 20 linhas
causa_acidente20 = causa_maior_0.sort_values(ascending=False).head(20)
causa_acidente20


# In[30]:


# gráfico mortos x causa do acidente
causa_acidente20.plot(kind='bar')
plt.xlabel('Causa do Acidente')
plt.ylabel('Quantidade de Óbitos')
plt.title('Mortos x Causa do Acidente')
plt.show()


# In[31]:


# agrupamento dos registros por br
registros_rodv = df.groupby(['br']).size()
reg_rodovia = registros_rodv.sort_values(ascending=False)
reg_rodovia


# In[32]:


# gráfico acidentes x rodovia
reg_rodovia.plot(kind='bar')
plt.xlabel('BR')
plt.ylabel('Quantidade de Acidentes')
plt.title('Acidentes x Rodovia')
plt.show()


# In[33]:


# filtrando e agrupando os dados referente as rodovias 
qual_rodovia = df.groupby(by='br').sum()
qual_rodovia


# In[34]:


# soma de óbitos por rodovia
m_rodovia = qual_rodovia.groupby(by='br').sum()['mortos']
m_rodovia


# In[35]:


# ordenando os valores do maior para o menor
rodovia = m_rodovia.sort_values(ascending=False)
rodovia


# In[36]:


# gráfico óbitos por rodovia
rodovia.plot(kind='bar')
plt.xlabel('BR')
plt.ylabel('Quantidade de Óbitos')
plt.title('Mortos x Rodovia')
plt.show()


# In[37]:


# agrupamento de registros de acidentes por dia da semana
r_dia = df.groupby(by='dia_semana').count()['id']
r_dia


# In[38]:


# ordenando os registros do maior para o menor
dia_semana_acidente = r_dia.sort_values(ascending=False)
dia_semana_acidente


# In[39]:


# gráfico registro de acidentes por dia da semana
dia_semana_acidente.plot(kind='bar')
plt.xlabel('Dia da Semana')
plt.ylabel('Quantidade de Acidentes')
plt.title('Acidentes x Dia da Semana')
plt.show()


# In[40]:


# agrupamento de óbitos por dia da semana
dia = df.groupby(by='dia_semana').sum()['mortos']
dia


# In[41]:


# ordenando os registros do maior para o menor
dia_semana = dia.sort_values(ascending=False)
dia_semana


# In[42]:


# gráfico mortos por dia da semana
dia_semana.plot(kind='bar')
plt.xlabel('Dia da Semana')
plt.ylabel('Quantidade de Óbitos')
plt.title('Mortos x Dia da Semana')
plt.show()


# In[43]:


# valores da coluna tipo_acidente
df['tipo_acidente'].unique()


# In[44]:


# agrupamento de óbitos por tipo acidente
tipo = df.groupby(by='tipo_acidente').sum()['mortos']


# In[45]:


# ordenando número de óbitos por tipo acidente do maior para o menor, onde houve óbitos
tipo_ac = tipo.sort_values(ascending=False)
tipo_acidente = tipo_ac[tipo>0]
tipo_acidente


# In[46]:


# gráfico mortos por tipo acidente
tipo_acidente.plot(kind='bar')
plt.xlabel('Tipo Acidente')
plt.ylabel('Quantidade de Óbitos')
plt.title('Mortos x Tipo Acidente')
plt.show()


# In[47]:


# agrupamento de óbitos por município onde houve 10 ou mais registros
municipio = df.groupby(by='municipio').sum()['mortos']
muni_mortos = municipio[municipio>=10]
muni_mortos


# In[48]:


# ordenando os registros do maior para o menor
municipio_mortos_ord = muni_mortos.sort_values(ascending=False)
municipio_mortos_ord


# In[49]:


# gráfico mortos por municipio onde houve 10 ou mais registros
municipio_mortos_ord.plot(kind='bar')
plt.xlabel('Município')
plt.ylabel('Quantidade de Óbitos')
plt.title('Mortos x Município (mais de 10 registros)')
plt.show()


# In[50]:


# valores da coluna tipo_pista
df['tipo_pista'].unique()


# In[51]:


# agrupamento dos registros de acidentes por tipo de pista
tipo_pista = df.groupby(by='tipo_pista').count()['id']
tipo_pista


# In[52]:


# ordenando os registros do maior para o menor
t_pista = tipo_pista.sort_values(ascending=False)
t_pista


# In[53]:


# gráfico do percentual de acidentes por tipo de pista
plt.figure(figsize=(7, 5))
t_pista.plot.pie(fontsize=14, autopct='%0.0f%%', labeldistance=None, radius=1)
plt.title('Percentual de Acidentes por Tipo de Pista', pad=10, fontsize=15)
plt.legend(['Simples','Dupla','Múltipla',],loc='upper right', bbox_to_anchor=(1.1,1) )
plt.ylabel('')
plt.show()


# In[54]:


# valores da coluna fase_dia
df['fase_dia'].unique()


# In[55]:


# agrupamento dos registros de acidentes por fase do dia
f_dia = df.groupby(by='fase_dia').count()['id']


# In[56]:


# ordenando os registros do maior para o menor
fase_dia = f_dia.sort_values(ascending=False)
fase_dia


# In[57]:


# gráfico do percentual de acidentes por fase do dia 
plt.figure(figsize=(7, 5))
fase_dia.plot.pie(fontsize=14, autopct='%0.0f%%', labeldistance=None, radius=1)
plt.title('Percentual de Acidentes por Fase do Dia', pad=10, fontsize=15)
plt.legend(['Pleno dia','Plena Noite','Amanhecer','Anoitecer'],loc='upper right', bbox_to_anchor=(1.2,1))
plt.ylabel('')
plt.show()


# In[58]:


# valores da coluna condicao_metereologica
df['condicao_metereologica'].unique()


# In[59]:


# agrupamento dos registros de acidentes por condição metereologica
tmp = df.groupby(by='condicao_metereologica').count()['id']


# In[60]:


# ordenando os resgistros do maior para o menor
tempo = tmp.sort_values(ascending=False)
tempo


# In[61]:


# gráfico de acidentes por condição meteorológica
tempo.plot(kind='bar')
plt.xlabel('Condição Meteorológica')
plt.ylabel('Quantidade de Acidentes')
plt.title('Acidentes x Condição Meteorológica')
plt.show()


# In[62]:


# valores da coluna classificacao_acidente
df['classificacao_acidente'].unique()


# In[63]:


# agrupamento dos registros de acidentes por classifição do acidente
cl_acidente = df.groupby(by='classificacao_acidente').count()['id']


# In[64]:


# ordenando os resgistros do maior para o menor
classif_acidente = cl_acidente.sort_values(ascending=False)
classif_acidente


# In[65]:


# gráfico do percentual de acidentes por classificação do acidente
plt.figure(figsize=(7, 5))
classif_acidente.plot.pie(fontsize=14, autopct='%0.0f%%', labeldistance=None, radius=1)
plt.title('Percentual de Acidentes por Classificação do Acidente', pad=10, fontsize=15)
plt.legend(['Com Vítimas Feridas','Sem Vítimas','Com Vítimas Fatais'],loc='upper right', bbox_to_anchor=(1.32,1))
plt.ylabel('')
plt.show()


# In[ ]:




