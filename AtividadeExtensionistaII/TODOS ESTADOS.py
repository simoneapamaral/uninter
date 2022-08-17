#!/usr/bin/env python
# coding: utf-8

# In[1]:


# importando a biblioteca pandas 
import pandas as pd


# In[2]:


# abrindo o dataset
df = pd.read_csv('acidentes2021_todas_causas_tipos.csv', sep=';' , encoding='latin-1')
pd.set_option('display.max_columns', None)


# In[3]:


# dimensões do dataset
df.shape


# In[4]:


# colunas do dataset
df.columns


# In[5]:


# amostras das primeiras linhas 
df.head() 


# In[6]:


# amostras das últimas linhas
df.tail()


# In[7]:


# ordenando as datas
df.sort_values('data_inversa')


# In[8]:


# valores ausentes
ausentes = df.isnull().sum()


# In[9]:


ausentes.sort_values(ascending=False)


# In[10]:


# total de acidentes
acidentes = df['id'].count()
print(f"Total de acidentes em 2021:",acidentes)


# In[11]:


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


# In[12]:


# soma do total de ilesos
ilesos = df['ilesos'].sum()
print(f"Total de ilesos:",ilesos)


# In[13]:


# soma do total de feridos leves 
feridosleves = df['feridos_leves'].sum()
print(f"Total de feridos leves:",feridosleves)


# In[14]:


# soma do total de feridos graves 
feridosgraves = df['feridos_graves'].sum()
print(f"Total de feridos graves:",feridosgraves)


# In[15]:


# soma do total de mortos 
mortos = df['mortos'].sum()
print(f"Total de mortos:",mortos)


# In[16]:


# agrupando acidentes por causa
acidente = df.groupby(['causa_acidente']).size().sort_values(ascending=False)
principais_causas = acidente.head(10) # 10 primeiras
principais_causas


# In[17]:


# gráfico principais causas de acidente
import matplotlib.pyplot as plt
principais_causas.plot(kind='bar', color='red')
plt.xlabel('Causa do Acidente')
plt.ylabel('Quantidade de Acidentes')
plt.title('Acidentes x Principais Causas de Acidentes (Ranking 1ª a 10ª)')
plt.show()


# In[18]:


# filtrando registros por estado
estado = df['uf'].value_counts()
estado


# In[19]:


# gráfico acidentes por estado
import matplotlib.pyplot as plt
estado.plot(kind='bar', color='red')
plt.xlabel('Estado')
plt.ylabel('Quantidade de Acidentes')
plt.title('Acidentes x Estado')
plt.show()


# In[20]:


# agrupando os dados referente as rodovias
qual_rodovia = df.groupby(by='br').sum()
qual_rodovia


# In[57]:


# soma de acidentes por rodovia (Ranking)
br = df['br'].value_counts()
br_dez_mais = br.head(10)
br_dez_mais


# In[58]:


# gráfico acidentes por rodovia 
import matplotlib.pyplot as plt
br_dez_mais.plot(kind='bar', color='red')
plt.xlabel('Rodovia')
plt.ylabel('Quantidade de Acidentes')
plt.title('Acidentes x Rodovia (Ranking 1ª a 10ª)')
plt.show()


# In[21]:


# soma de óbitos por rodovia (Ranking)
obitos_rodovia = qual_rodovia.groupby(by='br').sum()['mortos']
ordem_obitos = obitos_rodovia.sort_values(ascending=False)
dezmais = ordem_obitos.head(10)
dezmais


# In[53]:


# gráfico mortos por rodovia 
import matplotlib.pyplot as plt
dezmais.plot(kind='bar', color='red')
plt.xlabel('Rodovia')
plt.ylabel('Quantidade de Mortos')
plt.title('Mortos x Rodovia (Ranking 1ª a 10ª)')
plt.show()


# In[23]:


# agrupando os dados referente aos estados
qual_estado = df.groupby(by='uf').sum()
qual_estado


# In[24]:


# soma de óbitos por estado
obitos = qual_estado.groupby(by='uf').sum()['mortos']
obitos


# In[25]:


# ordenando do maior para o menor mortos por estado
mortos_ordem = obitos.sort_values(ascending=False)
mortos_ordem


# In[54]:


# gráfico mortos por estado
import matplotlib.pyplot as plt
mortos_ordem.plot(kind='bar', color='red')
plt.xlabel('Estado')
plt.ylabel('Quantidade de Mortos')
plt.title('Mortos x Estado')
plt.show()


# In[27]:


sexo = df['sexo'].value_counts()
sexo


# In[28]:


# gráfico do percentual de acidentes por sexo
plt.figure(figsize=(7, 5))
sexo.plot.pie(fontsize=14, autopct='%0.1f%%', labeldistance=None, radius=1)
plt.title('Percentual de Acidentes por Sexo', pad=10, fontsize=15)
plt.legend(['Masculino','Feminino','Não Informado','Ignorado'],loc='upper right', bbox_to_anchor=(1.3,1) )
plt.ylabel('')
plt.show()


# In[29]:


# agrupando óbitos por sexo
mortos_por_sexo = df.groupby(by='sexo').sum()['mortos']
mortos_por_sexo
sexo_mortos = mortos_por_sexo.sort_values(ascending=False)
sexo_mortos


# In[30]:


# gráfico do percentual de mortos por sexo
plt.figure(figsize=(7, 5))
sexo_mortos.plot.pie(fontsize=14, autopct='%0.0f%%', labeldistance=None, radius=1)
plt.title('Percentual de Mortos por Sexo', pad=10, fontsize=15)
plt.legend(['Masculino','Feminino'],loc='upper right', bbox_to_anchor=(1.1,1) )
plt.ylabel('')
plt.show()


# In[31]:


# filtrando acidentes por classificação
class_acidente = df['classificacao_acidente'].value_counts()
class_acidente


# In[32]:


# gráfico do percentual de acidentes por classificação
plt.figure(figsize=(7, 5))
class_acidente.plot.pie(fontsize=14, autopct='%0.0f%%', labeldistance=None, radius=1)
plt.title('Percentual de Acidentes por Classificação do Acidente', pad=10, fontsize=15)
plt.legend(['Com Vítimas Feridas','Com Vítimas Fatais','Sem Vítimas'],loc='upper right', bbox_to_anchor=(1.3,1) )
plt.ylabel('')
plt.show()


# In[33]:


# agrupando os registros de acidentes por condições meteorológicas
tmp = df.groupby(by='condicao_metereologica').count()['id']


# In[34]:


# ordenando os resgistros do maior para o menor
tempo = tmp.sort_values(ascending=False)
tempo


# In[35]:


# gráfico de acidentes por condição meteorológica
tempo.plot(kind='barh',color='red')
plt.xlabel('Quantidade de Acidentes')
plt.ylabel('Condição Meteorológica')
plt.title('Acidentes x Condição Meteorológica')
plt.show()


# In[36]:


# filtrando registros por tipo de pista
tipo_pista = df['tipo_pista'].value_counts()
tipo_pista


# In[37]:


# gráfico do percentual de acidentes por tipo de pista
plt.figure(figsize=(7, 5))
tipo_pista.plot.pie(fontsize=14, autopct='%0.0f%%', labeldistance=None, radius=1)
plt.title('Percentual de Acidentes por Tipo de Pista', pad=10, fontsize=15)
plt.legend(['Simples','Dupla','Múltipla',],loc='upper right', bbox_to_anchor=(1.1,1) )
plt.ylabel('')
plt.show()


# In[38]:


tipo_ac = df['tipo_acidente'].value_counts()
tipo_ac


# In[39]:


# gráfico acidentes por tipo acidente
tipo_ac.plot(kind='bar',color='red')
plt.xlabel('Tipo Acidente')
plt.ylabel('Quantidade de Mortos')
plt.title('Acidentes x Tipo Acidente')
plt.show()


# In[40]:


# agrupando óbitos por tipo de acidente
tipo = df.groupby(by='tipo_acidente').sum()['mortos']


# In[41]:


# ordenando número de óbitos por tipo de acidente do maior para o menor
tipo_ordem = tipo.sort_values(ascending=False)
tipo_ordem


# In[42]:


# gráfico mortos por tipo acidente
tipo_ordem.plot(kind='bar',color='red')
plt.xlabel('Tipo Acidente')
plt.ylabel('Quantidade de Mortos')
plt.title('Mortos x Tipo Acidente')
plt.show()


# In[43]:


# filtrando resgistro por dia da semana
dia_semana = df['dia_semana'].value_counts()
dia_semana


# In[44]:


# gráfico registro de acidentes por dia da semana
dia_semana.plot(kind='bar',color='red')
plt.xlabel('Dia da Semana')
plt.ylabel('Quantidade de Acidentes')
plt.title('Acidentes x Dia da Semana')
plt.show()


# In[45]:


# agrupando óbitos por dia da semana
dia = df.groupby(by='dia_semana').sum()['mortos']
dia


# In[46]:


# ordenando os registros do maior para o menor
dia_semana = dia.sort_values(ascending=False)
dia_semana


# In[47]:


# gráfico mortos por dia da semana
dia_semana.plot(kind='bar',color='red')
plt.xlabel('Dia da Semana')
plt.ylabel('Quantidade de Óbitos')
plt.title('Mortos x Dia da Semana')
plt.show()


# In[48]:


veiculos = df['tipo_veiculo'].value_counts()
veiculos


# In[49]:


# gráfico acidentes por tipo de veículo
veiculos.plot(kind='bar',color='red')
plt.xlabel('Tipo de Veículo')
plt.ylabel('Quantidade de Acidentes')
plt.title('Acidentes x Tipo de Veículo')
plt.show()


# In[50]:


# agrupando óbitos por tipo de veículo
tipo = df.groupby(by='tipo_veiculo').sum()['mortos']
tipo_v = tipo.sort_values(ascending=False)
tipo_v


# In[51]:


# gráfico mortos por tipo de veículo
tipo_v.plot(kind='bar',color='red')
plt.xlabel('Tipo de Veículo')
plt.ylabel('Quantidade de Óbitos')
plt.title('Mortos x Tipo de Veículo')
plt.show()

