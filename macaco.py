from dataframe import *
import matplotlib.pyplot as plt

class DataFrame():
    """docstring for DataFrame"""
    def __init__(self,dados=None):
        self.df = dataframe()
        self.columns = {}
        self.shape = [0,0]
        if dados != None:
            for coluna in dados:
                self.addColumn(dados[coluna], str(coluna))

    def addColumn(self, values, col_name):
        # Infere o tipo do dado. Caso encontre multiplos,
        # transforma em string
    
        if all(isinstance(x, int) for x in values):
            if self.shape == [0,0]:
                self.df.addIntColumn(values, col_name)
                self.columns[col_name] ='int'
                self.shape[0] = len(values)
                self.shape[1] += 1
            elif self.shape[0] != len(values):
                raise Exception("Coluna com tamanhos diferentes.")
            else:
                self.df.addIntColumn(values, col_name)
                self.columns[col_name] ='int'
                self.shape[1] += 1

        elif all(isinstance(x, (float,int)) for x in values):
            if self.shape == [0,0]:
                self.df.addDoubleColumn(values, col_name)
                self.columns[col_name] ='double'
                self.shape[0] = len(values)
                self.shape[1] += 1
            elif self.shape[0] != len(values):
                raise Exception("Coluna com tamanhos diferentes.")
            else:
                self.df.addDoubleColumn(values, col_name)
                self.columns[col_name] ='double'
                self.shape[1] += 1

        else:
            if not all(isinstance(x, str) for x in values):
                values = [str(i) for i in list(values)]
            if self.shape == [0,0]:
                self.df.addStringColumn(values,col_name)
                self.columns[col_name] ='string'
                self.shape[0] = len(values)
                self.shape[1] += 1
            elif self.shape[0] != len(values):
                raise Exception("Coluna com tamanhos diferentes.")
            else:
                self.df.addStringColumn(values,col_name)
                self.columns[col_name] ='string'
                self.shape[1] += 1
                

    def popColumn(self,column_name):
        '''
        Remove coluna do dataframe.
        '''
        if self.columns[column_name] == 'int':
            self.df.popIntColumn([], column_name)
            self.columns.pop(column_name)

        elif self.columns[column_name] == 'double':
            self.df.popDoubleColumn([], column_name)
            self.columns.pop(column_name)

        elif self.columns[column_name] == 'string':
            self.df.popStringColumn([], column_name)
            self.columns.pop(column_name)

            
    def getColumn(self,col_name):
        if self.columns[col_name] == 'int':
            return self.df.getIntColumn(col_name)
        elif self.columns[col_name] == 'double':
            return self.df.getDoubleColumn(col_name)
        elif self.columns[col_name] == 'string':
            return self.df.getStringColumn(col_name)
        

    def info(self):
        print('< macaco.DataFrame >')
        print('RangeIndex: ') ### fazer!!!
        print('Total of lines: {}'.format(self.shape[0]))
        print('Data ({} columns):'.format(self.shape[1]))
        
        cols = list(self.columns.keys())
        dtypes = list(self.columns.values())
        for i in range(len(cols)):
            if dtypes[i] == 'int':
                vector = self.df.getIntColumn(cols[i])
            elif dtypes[i] == 'double':
                vector = self.df.getDoubleColumn(cols[i])
            elif dtypes[i] == 'string':
                vector = self.df.getStringColumn(cols[i])

            print(cols[i], ' ', sum([v != None for v in vector]), 'non-null entries ' ,dtypes[i])
    
    
    def head(self, n_lines=5):
        '''
        Exibe as primeiras linhas do dataframe. 
        
        A primeira lista são as colunas. 
        Depois, cada lista corresponde a uma linha.
        '''
        cols = list(self.columns.keys())
        dtypes = list(self.columns.values())
        
        d = {}
        for i in range(len(cols)):
            if dtypes[i] == 'int':
                vector = self.df.getIntColumn(cols[i])[:n_lines]
                d[cols[i]] = vector
            elif dtypes[i] == 'double':
                vector = self.df.getDoubleColumn(cols[i])[:n_lines]
                d[cols[i]] = vector
            elif dtypes[i] == 'string':
                vector = self.df.getStringColumn(cols[i])[:n_lines]
                d[cols[i]] = vector
        
        print(cols)
        for i in range(n_lines):
            line = []
            for col in cols:
                line.append(d[col][i])    
            print(line)
    
    
    def tail(self, n_lines=5):
        '''
        Exibe as primeiras linhas do dataframe. 
        
        A primeira lista são as colunas. 
        Depois, cada lista corresponde a uma linha.
        '''
        cols = list(self.columns.keys())
        dtypes = list(self.columns.values())
        
        d = {}
        for i in range(len(cols)):
            if dtypes[i] == 'int':
                vector = self.df.getIntColumn(cols[i])[-n_lines:]
                d[cols[i]] = vector
            elif dtypes[i] == 'double':
                vector = self.df.getDoubleColumn(cols[i])[-n_lines:]
                d[cols[i]] = vector
            elif dtypes[i] == 'string':
                vector = self.df.getStringColumn(cols[i])[-n_lines:]
                d[cols[i]] = vector
        
        print(cols)
        for i in range(n_lines):
            line = []
            for col in cols:
                line.append(d[col][i])    
            print(line)  
            
            
    def plot(self, y = None, x = None, kind='line', remove_frames='No', **kwargs):
            '''
            Faz um plot com as colunas x e y.

            Argumentos: 
                - y: nome da coluna para o eixo y
                - x: nome da coluna para o eixo x
                - kind: tipo de gráfico 
                    'line': linha (default)
                    'bar': barras verticais
                    'barh': barras horizontais
                    'hist': histograma
                    'kde': Kernel Density Estimation plot
                    'density': mesmo que o kde
                    'scatter': dispersão
                    'area': área
                    'pie': pizza

            Para mais configurações, visite a documentação do matplotlib.pyplot
            '''

            # preparando os dados
            if x == None:
                x = list(range(self.shape[0]))

            if self.columns[y] == 'int':
                y_data = self.df.getIntColumn(y)
            elif self.columns[y] == 'double':
                y_data = self.df.getDoubleColumn(y)

            # se é string, levanta um erro
            elif self.columns[y] == 'string':
                raise ValueError('Cannot plot string vector')

            # permite passar um eixo para o plot
            if kwargs.get('ax') == None:
                fig, ax = plt.subplots(figsize=kwargs.get('figsize'))
            else:
                ax = ax

            #plt.figure(figsize=kwargs.get('figsize'), num=kwargs.get('num'),  dpi=kwargs.get('dpi'),
            #           facecolor=kwargs.get('facecolor'), edgecolor=kwargs.get('edgecolor'))

            # gráfico de linha (padrão)
            if kind == 'line':
                # ajustando argumentos padrão
                if kwargs.get('scalex') == None:
                    scalex = True
                else:
                    scalex = kwargs.get('scalex')

                if kwargs.get('scaley') == None:
                    scaley = True
                else:
                    scaley = kwargs.get('scaley')

                ax.plot(y_data, scalex= scalex, scaley = scaley, 
                         color=kwargs.get('color'))

            # histograma
            if kind == 'hist':
                # tratando argumentos padrão
                if kwargs.get('histtype') == None:
                    histtype = 'bar'
                else:
                    histtype = kwargs.get('histtype')

                if kwargs.get('align') == None:
                    align = 'mid'
                else:
                    align = kwargs.get('align')

                if kwargs.get('orientation') == None:
                    orientation = 'vertical'
                else:
                    orientation = kwargs.get('orientation')

                ax.hist(y_data, bins = kwargs.get('bins'), color=kwargs.get('color'), 
                         range=kwargs.get('range'), density=kwargs.get('density'),
                         weights=kwargs.get('weights'), cumulative=kwargs.get('cumulative'),
                         bottom=kwargs.get('bottom'), rwidth=kwargs.get('rwidth'), 
                         log=kwargs.get('log'), label=kwargs.get('label'),
                         stacked=kwargs.get('stacked'), normed=kwargs.get('normed'),
                         histtype=histtype, align=align, orientation=orientation)



            ### OBS: implementar os demais tipos de gráficos AQUI!!!

            # ajustando elementos gráficos
            ax.set_xlabel(kwargs.get('xlabel'))
            ax.set_ylabel(kwargs.get('ylabel'))
            plt.title(kwargs.get('title'))

            if kwargs.get('ylim') != None:
                ax.set_ylim(kwargs.get('ylim'))
            if kwargs.get('xlim') != None:
                ax.set_xlim(kwargs.get('xlim'))

            if remove_frames == 'all':
                ax.spines['top'].set_visible(False)
                ax.spines['right'].set_visible(False)
                ax.spines['bottom'].set_visible(False)
                ax.spines['left'].set_visible(False)
            if remove_frames == 'left':
                ax.spines['left'].set_visible(False)
            if remove_frames == 'right':
                ax.spines['right'].set_visible(False)
            if remove_frames == 'bottom':
                ax.spines['bottom'].set_visible(False)
            if remove_frames == 'top':
                ax.spines['top'].set_visible(False)


        # def GetLinha(linha)
        # def GetColuna(coluna)
        # def GetLoc(linha,coluna)
        # def Query()
