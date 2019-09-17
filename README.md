# Macaco - DataFrame para Python compilado em C++

Repositório do trabalho final da disciplina de Estruturas de Dados e Algoritmos da EMAp-FGV.

## Equipe:

> - Franklin Oliveira
> - Felipe Costa 

## O que aprendemos?

> - Como compilar um código em C++ e utilizá-lo em Python (usando a biblioteca boost)    <br>
> - Como estruturar um código em C++ (diferentes extensões de arquivos)                  <br>
> - Como criar um pacote instalável com o *pip*                                          <br>



## Arquivos

> - **compile_pyboost.sh** - arquivo em bash para compilar o código em c++
> - **dataframe.cpp** - Implementa a classe DataFrame em C++. Nesse arquivo são definidas as funções para acrescentar colunas, deletar e acessar as informações em cada coluna. Isso é feito para três tipos de variáveis: `int`, `double` e `string`. O *boost* é uma biblioteca de C++ integrada a esse código para que haja a comunicação com o Python.
> - **dataframe.h** - Arquivo de header (define a classe DataFrame e instancia seus métodos)
> - **macaco.py** - Definição do pacote macaco - envelopa o código em C++ para o usuário em Python.
> - **dataframe.o**, **dataframe.so** - dataframe compilado (arquivos binários), pronto para ser acessado pelo Python (funcionará em um sistema operacional Linux, com os caminhos de pasta definidos conforme o arquivo `compile_pyboost.sh`).
> - **demo.ipynb** - Demonstração das funcionalidades do pacote macaco

-----

## Sobre o Projeto

O objetivo desse projeto foi criar uma biblioteca para o Python, compilada em C++, com funcionalidades semelhantes à da biblioteca [Pandas](https://pandas.pydata.org/). O nome macaco, sugerido pelo professor, tem a intenção de remeter à biblioteca original, mas deixando claro que não se trata de uma cópia (apesar de ambas terem funcionalidades semelhantes).

As funcionalidades que deveríamos implementar na biblioteca estão todas listadas no arquivo `Project Specification.pdf`.

### Descrição

O *dataframe* é uma estrutura utilizada para otimizar a análise e a manipulação de dados numéricos (ou minimamente estruturados) em tabelas. A idéia é ter uma estrutura bidimensional, onde uma das dimensões é representada pelas colunas e a outra é representada pelas linhas. Em tese, os dados que estão contidos nas colunas tem o mesmo tipo, enquanto que as linhas podem ser de diferentes tipos. 

O Macaco possui as seguintes funcionalidades:
* Adicionar e remover colunas dos tipos inteiro, double e string.
* Representar os dados das colunas em quatro tipos de gráficos: linha, histograma, barra e barra horizontal. É possível escolher a quantidade de colunas que são traçadas simultaneamente, tornando a visualização de dados mais fácil e intuitiva.

Para uma descrição mais detalhada de suas funcionalidades, vide a seção **Funcionalidades** ao fim desta página.


### Requisitos

A biblioteca foi desenvolvida e testada integralmente em uma distribuição `Linux` (s.o. Ubuntu 19), e pode não funcionar devidamente em outros sistemas operacionais. Caso esteja utilizando um sistema operacional diferente, você poderá compilar novamente os arquivos binários em C++. Em linux, isso é feito com o seguinte comando (dentro da pasta raiz do projeto): 

```bash
bash compile_pyboost.sh
```

Caso não funcione, você pode ajustar os argumentos dentro do arquivo `compile_pyboost.sh`. Atente-se para os caminhos de pasta do pacote `boost` e do interpretador `Python`. Verifique se a versão e os caminhos apontados correspondem aos do seu sistema operacional e das versões destas ferramentas instaladas em seu computador. 

Alternativamente, em `Linux`, os arquivos podem ser compilados com os seguintes comandos em um terminal:

```bash
g++ -std=c++17 -I /usr/include/python3.X -fpic -c -o dataframe.o dataframe.cpp
g++ -o dataframe.so -shared dataframe.o -lboost_python3
``` 

Se o seu sistema operacional não é `Linux`, você pode pesquisar as respectivas versões desses comandos de acordo com seu sistema.

**OBS:** O macaco foi desenvolvido com a versão 17 do `C++` pode não funcionar em versões prévias. A versão utilizada do `Python` foi a 3.7, mas tudo deve funcionar apropriadamente em versões prévias do `Python 3`. 

#### Dependencias em Python 3:
```
matplotlib
```

#### Dependencias em C++17:
```
iostream - vector - string - map - tuple - boost
```


### Instalação
**OBS:** Para garantir que a ferramenta funcionará corretamente, é fundamental que os arquivos binários em C++ sejam compilados novamente, da maneira mais adequada para o seu sistema operacional e versões do interpretador Python e da biblioteca *boost*. Para isso, siga as instruções na seção de **Requisitos**.

Para fazer a instalação, execute os seguintes comandos em uma instância do terminal:  

```bash
git clone https://github.com/Franklin-oliveira/Macaco

cd Macaco

pip install -e .  
```

-----

## Funcionalidades

Para guia de uso e exemplo das funcionalidades da biblioteca, vide o arquivo `demo.ipynb`.

### macaco.DataFrame
**class macaco.DataFrame(Dados=None,index=None)**
Estrutura de dados bidimensional.

|Parameters  | Description|
|------------|:-----------------------------------------------------------------------------------:|
|Dados       |  dicionario{coluna:[valores]}|
|Index       |  lista[valores]|

   
    Exemplo:
    import macaco as mc
    
    df = mc.DataFrame({'Col1': ['a','b','c','d'], 'Col2': [1,2,3,4], 'Col3':[3,3,4,1]})
    

|Methods|Description|
|------------|:-----------------------------------------------------------------------------------:|
|addColumn(seld,values,col_name)|Adiciona uma nova coluna|
|popColumn(self,column_name)|Remove a coluna indicada|
|getColumn(self,col_name)|Mostra os valores da coluna indicada|
|addRow(self, values)|Insere uma nova linha ao dataframe|
|loc(self,row,column)|Retorna o(s) elemento(s) na(s) linha(s) e coluna(s) indicadas| 
|info(self)|Exibe uma breve descrição do dataframe|
|head(self,n_lines=5)|Exibe as primeiras linhas do DataFrame|
|tail(self,n_lines=5)|Exibe as últimas linhas do DataFrame|
|show(self)|Exibe todo o DataFrame (não recomendável para DataFrames muito grandes)|
|plot(self,y,x,kind,remove_frames,kwargs)|Traça um gráfico com as colunas x e y|

      Exemplo:
      import macaco as mc
    
      df = mc.DataFrame({'Col1': ['a','b','c'], 'Col2': [1,2,3], 'Col3':[3,3,4]})
      df.addColumn([85,86,87],'Decada Perdida')
      df.show()
      
      ['Col1','Col2','Col3','Decada Perdida']
      ['a',1,3,85]
      ['b',2,3,86]
      ['c',3,4,87]

|Attributes|Description|
|------------|:-----------------------------------------------------------------------------------:|
|info(self)|Retorna um sumário conciso do DataFrame(colunas,tipos,quantidade de linhas)|
|show(self)|Imprime na tela o DataFrame|

    
 
    

