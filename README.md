# Macaco

Repositório do trabalho final da disciplina de Estruturas de Dados e Algoritmos da EMAp-FGV.

## Equipe:

- Franklin Oliveira

- Felipe Costa 

## O que aprendemos?

## Arquivos

compile_pyboost.sh - para compilar
dataframe.cpp - Implementa a classe DataFrame em C++. Nesse arquivo são definidas as funções para acrescentar colunas, deletar e acessar
as informações em cada coluna. Isso é feito para três tipos de variáveis: int, double e string. O boost é integrado nesse código, para que
haja a comunicação com o Python.
dataframe.o, dataframe.so - dataframe compilado, pronto para ser acessado pelo Python.
demo.ipynb - implementação das funções gráficas

## Projeto: MACACO

### Descrição

O dataframe é uma forma utilizada para otimizar a análise e a manipulação de dados numéricos (ou minimamente estruturados)  em tabelas. A idéia é ter uma estrutura bidimensional, onde uma das dimensões é representada pelas colunas e a outra é representada pelas linhas. Em tese, os dados que estão contidos nas colunas tem o mesmo tipo, enquanto que as linhas podem ser de diferentes tipos. 

O Macaco possui as seguintes funcionalidades:
* Adicionar e remover colunas dos tipos inteiro, double e string.
* Representar os dados das colunas em quatro tipos de gráficos: linha, histograma, barra e barra horizontal. É possível escolher a quantidade de colunas que são traçadas simultaneamente, tornando a visualização de dados mais fácil e intuitiva.

### Requisitos

Para instalar:
pip install macaco

Dependencias:
* Matplotlib

## Funcionalidades

### macaco.DataFrame
**class macaco.DataFrame(Dados=None)**
Estrutura de dados bidimensional.

|Parameters  | Description|
|------------|:-----------------------------------------------------------------------------------:|
|Dados       |  dicionario: a key contém o nome da coluna e a lista associada aos valores da coluna|

|Methods|Description|
|------------|:-----------------------------------------------------------------------------------:|
|addColumn(seld,values,col_name)|Adiciona uma nova coluna|
|popColumn(self,column_name)|Remove a coluna indicada|
|getColumn(self,col_name)|Mostra os valores da coluna indicada|
|head(self,n_lines=5)|Exibe as primeiras linhas do DataFrame|
|tail(self,n_lines=5)|Exibe as últimas linhas do DataFrame|
|plot(self,y,x,kind,remove_frames,kwargs)|Traça um gráfico com as colunas x e y|

|Attributes|Description|
|------------|:-----------------------------------------------------------------------------------:|
|info(self)|Retorna um sumário conciso do DataFrame(colunas,tipos,quantidade de linhas)|

    
    
    Exemplo:
    from dataframe import *
    
    df=DataFrame({'Col1': ['a','b','c','d'], 'Col2': [1,2,3,4], 'Col3':[3,3,4,1]})
    

