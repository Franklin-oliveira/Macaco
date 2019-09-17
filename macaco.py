from dataframe import *
import matplotlib.pyplot as plt


class DataFrame():
    '''
    Macaco.DataFrame
    '''
    
    def __init__(self, dados=None, index=None):
        self.df = dataframe()
        self.columns = {}
        self.shape = [0,0]
        self.colIndex = []
        
        if index != None:
            self.rowIndex = index
        else:
            for col in dados:
                self.index = list(range(len(dados[col])))
        
        if dados != None:
            for col in dados:
                self.addColumn(dados[col], str(col))
                
### ------------------------------------------------------------------------------------------------------- ###    
    def indexColumn(self, col):
        if self.columns[col] == 'int':
            self.df.indexIntCol([], col)
            self.colIndex.append(col)
        elif self.columns[col] == 'double':
            self.df.indexDoubleCol([], col)
            self.colIndex.append(col)
        elif self.columns[col] == 'string':
            self.df.indexStringCol([], col)
            self.colIndex.append(col)
        
### ------------------------------------------------------------------------------------------------------- ###
    def addColumn(self, values, col_name):
        if all(isinstance(x, int) for x in values):
            if self.shape == [0,0]:
                self.df.addIntColumn(values, col_name)
                self.columns[col_name] ='int'
                self.shape[1] += 1
                self.shape[0] = len(values)
                     
            elif self.shape[0] != len(values):
                raise ValueError("Columns with different sizes")
                
            else:
                self.df.addIntColumn(values, col_name)
                self.columns[col_name] ='int'
                self.shape[1] += 1

        elif all(isinstance(x, (float,int)) for x in values):
            if self.shape == [0,0]:
                self.df.addDoubleColumn(values, col_name)
                self.columns[col_name] ='double'
                self.shape[1] += 1
                self.shape[0] = len(values)
                
            elif self.shape[0] != len(values):
                raise ValueError("Columns with different sizes")
                
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
                self.shape[1] += 1
                self.shape[0] = len(values)
                
            elif self.shape[0] != len(values):
                raise ValueError("Columns with different sizes")
                
            else:
                self.df.addStringColumn(values, col_name)
                self.columns[col_name] ='string'
                self.shape[1] += 1
        self.indexColumn(col_name)

### ------------------------------------------------------------------------------------------------------- ###
    def popColumn(self,column_name):
        '''
        Remove coluna do DataFrame.
        '''
        if self.columns[column_name] == 'int':
            self.df.popIntColumn([], column_name)
            self.columns.pop(column_name)
            self.shape[1] -= 1

        elif self.columns[column_name] == 'double':
            self.df.popDoubleColumn([], column_name)
            self.columns.pop(column_name)
            self.shape[1] -= 1

        elif self.columns[column_name] == 'string':
            self.df.popStringColumn([], column_name)
            self.columns.pop(column_name)
            self.shape[1] -= 1

### ------------------------------------------------------------------------------------------------------- ###            
    def getColumn(self,col_name):
        '''
        Retorna a coluna indicada do DataFrame.
        '''
        if self.columns[col_name] == 'int':
            return self.df.getIntColumn(col_name)
        elif self.columns[col_name] == 'double':
            return self.df.getDoubleColumn(col_name)
        elif self.columns[col_name] == 'string':
            return self.df.getStringColumn(col_name)
    
### ------------------------------------------------------------------------------------------------------- ###    
    def addRow(self, values):
        '''
        Adiciona nova linha ao DataFrame.
        '''
        num_linhas = [len(values[i]) for i in values][0]
        if len(set([len(values[i]) for i in values]))>1:
            raise Exception("Columns with different number of elements")
        for col in self.columns:
            if self.columns[col] == 'int':
                self.df.addIntRow(values[col], col)
            elif self.columns[col] == 'double':
                self.df.addDoubleRow(values[col], col)
            elif self.columns[col] == 'string':
                self.df.addStringRow(values[col], col)
        self.shape[0] += num_linhas
        
        
### ------------------------------------------------------------------------------------------------------- ###        
    def loc(self, row, column):
        rows = []
        if type(row) == int:
            rows.append(row)
        else:
            rows = list(row)

        if max(rows) > self.index[-1]:
            raise Exception("Row not in Index")
        
        if type(column) == list:
            cols = []
            for col in column:
                temp = []
                if self.columns[col] == 'int':
                    temp.extend(self.df.getIntRow(rows, col))
                elif self.columns[col] == 'double':
                    temp.extend(self.df.getDoubleRow(rows, col))
                elif self.columns[col] == 'string':
                    temp.extend(self.df.getStringRow(rows, col))
                cols.append(temp)
            return cols
        else:
            if self.columns[column] == 'int':
                return self.df.getIntRow(rows, column)
            elif self.columns[column] == 'double':
                return self.df.getDoubleRow(rows, column)
            elif self.columns[column] == 'string':
                return self.df.getStringRow(rows, column)

### ------------------------------------------------------------------------------------------------------- ###
    def info(self):
        print('< macaco.DataFrame >')
        print('RangeIndex: from {} to {}'.format(min(self.index), max(self.index)))
        print('Total of lines: {}'.format(self.shape[0]))
        print('Data ({} columns):'.format(self.shape[1]))
        
        cols = list(self.columns.keys())
        dtypes = list(self.columns.values())
        sizes = [len(col) for col in cols]
        max_size = max(sizes)
        for i in range(len(cols)):
            if dtypes[i] == 'int':
                vector = self.df.getIntColumn(cols[i])
            elif dtypes[i] == 'double':
                vector = self.df.getDoubleColumn(cols[i])
            elif dtypes[i] == 'string':
                vector = self.df.getStringColumn(cols[i])

            print(cols[i], ' '*int(round(max_size/len(cols[i]),0)), 
                  sum([v != None for v in vector]), 'non-null entries ' ,dtypes[i])
    
    
### ------------------------------------------------------------------------------------------------------- ###
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
        
        print('Colunas:', cols)
        for i in range(min(n_lines, self.shape[0])):
            line = []
            for col in cols:
                line.append(d[col][i])    
            print('Linha {}:'.format(i),line)

### ------------------------------------------------------------------------------------------------------- ###            
    def show(self):
        self.head(self.shape[0])
    
### ------------------------------------------------------------------------------------------------------- ###   
    def tail(self, n_lines=5):
        '''
        Exibe as últimas linhas do dataframe. 
        
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
        
        print('Colunas:', cols)
        n = self.shape[0] - min(n_lines, self.shape[0])
        for i in range(min(n_lines, self.shape[0])):
            line = []
            for col in cols:
                line.append(d[col][i])    
            print('Linha {}:'.format(n), line)
            n += 1
    

### ------------------------------------------------------------------------------------------------------- ###     
    def plot(self, y = None, x = None, kind='line', remove_frames='no',style='seaborn-white',
             axe = None, **kwargs):
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
                'scatter': dispersão
            - axe: eixo para fazer o plot (plt.axes)
                
        Para mais configurações, visite a documentação do matplotlib.pyplot
        '''
        plt.style.use(style)
        
        # preparando os dados
        if x == None:
            x = list(range(self.shape[0]))
        else:
            x = self.getColumn(x)
        
        if y == None:
            y = []
            for col in list(self.columns.keys()):
                if self.columns[col] != 'string':
                    y.append(col)
        
        d = {}
        if type(y) == list:
            for col in y:
                if self.columns[col] == 'int':
                    d[col] = self.df.getIntColumn(col)
                elif self.columns[col] == 'double':
                    d[col] = self.df.getDoubleColumn(col)
                # se é string, levanta um erro
                elif self.columns[y] == 'string':
                    raise ValueError('Cannot plot string vector')
        else:
            if self.columns[y] == 'int':
                d[y] = self.df.getIntColumn(y)
            elif self.columns[y] == 'double':
                d[y] = self.df.getDoubleColumn(y)
            # se é string, levanta um erro
            elif self.columns[y] == 'string':
                raise ValueError('Cannot plot string vector')

        # permite passar um eixo para o plot
        ax = kwargs.get('axe')
        if ax == None:
            fig, ax = plt.subplots(figsize=kwargs.get('figsize'))
        
        #plt.figure(figsize=kwargs.get('figsize'), num=kwargs.get('num'),  dpi=kwargs.get('dpi'),
        #           facecolor=kwargs.get('facecolor'), edgecolor=kwargs.get('edgecolor'))
        
        # gráfico de linha (padrão)
        if kind.lower() == 'line':
            # ajustando argumentos padrão
            if kwargs.get('scalex') == None:
                scalex = True
            else:
                scalex = kwargs.get('scalex')
            
            if kwargs.get('scaley') == None:
                scaley = True
            else:
                scaley = kwargs.get('scaley')
            
            if type(y) == list:
                for col in y:
                    ax.plot(x,d[col], scalex= scalex, scaley = scaley, 
                         color=kwargs.get('color'), label=col)
                    ax.legend()
            else:
                ax.plot(x,d[y], scalex= scalex, scaley = scaley, 
                         color=kwargs.get('color'))
        # histograma
        elif kind == 'hist':
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
            
            if type(y)==list:
                
                for col in y:
                    
                    ax.hist(d[col], bins = kwargs.get('bins'), color=kwargs.get('color'), range=kwargs.get('range'),\
                            density=kwargs.get('density'),weights=kwargs.get('weights'),\
                            cumulative=kwargs.get('cumulative'),bottom=kwargs.get('bottom'), rwidth=kwargs.get('rwidth'),\
                            log=kwargs.get('log'), label=col,stacked=kwargs.get('stacked'),\
                            normed=kwargs.get('normed'),histtype=histtype, align=align, orientation=orientation,\
                            alpha=kwargs.get('alpha'))
                    ax.legend(y)
                
            else:
                
                ax.hist(d[y], bins = kwargs.get('bins'), color=kwargs.get('color'), 
                     range=kwargs.get('range'), density=kwargs.get('density'),
                     weights=kwargs.get('weights'), cumulative=kwargs.get('cumulative'),
                     bottom=kwargs.get('bottom'), rwidth=kwargs.get('rwidth'), 
                     log=kwargs.get('log'), label=kwargs.get('label'),
                     stacked=kwargs.get('stacked'), normed=kwargs.get('normed'),
                     histtype=histtype, align=align, orientation=orientation, alpha=kwargs.get('alpha'))
                
                
        # Scatter
        elif kind == 'scatter':
            if type(y)==list:
                for col in y:
                    
                    ax.scatter(x = x, y = d[col], s=kwargs.get('s'), c=kwargs.get('c'), 
                               marker= kwargs.get('marker'), cmap= kwargs.get('cmap'),
                               norm= kwargs.get('norm'), vmin=kwargs.get('vmin'),
                               vmax= kwargs.get('vmax'), alpha=kwargs.get('alpha'), 
                               linewidths= kwargs.get('linewidths'), verts= kwargs.get('verts'),
                               edgecolors= kwargs.get('edgecolors'), data=kwargs.get('data'))
                    ax.legend(y)
            else:
                
                ax.scatter(x = x, y = d[y], s=kwargs.get('s'), c=kwargs.get('c'), 
                           marker= kwargs.get('marker'), cmap= kwargs.get('cmap'),
                           norm= kwargs.get('norm'), vmin=kwargs.get('vmin'),
                           vmax= kwargs.get('vmax'), alpha=kwargs.get('alpha'), 
                           linewidths= kwargs.get('linewidths'), verts= kwargs.get('verts'),
                           edgecolors= kwargs.get('edgecolors'), data=kwargs.get('data'))

        # Bar
        elif kind == 'bar':
            if kwargs.get('width') == None:
                width = 0.8
            else:
                width = kwargs.get('width')
            if kwargs.get('align') == None:
                align = 'center'
            else:
                align = kwargs.get('align')
            
            if type(y)==list:
                for col in y:
                    ax.bar(x = x, height= d[col], width= width, bottom=kwargs.get('bottom'), align= align,
                       data=kwargs.get('data'), alpha=kwargs.get('alpha'), label=col)
                    ax.legend(y)
                    
            else:
                ax.bar(x = x, height= d[y], width= width, bottom=kwargs.get('bottom'), align= align,
                       data=kwargs.get('data'), alpha=kwargs.get('alpha'))
        
        # Barh    
        elif kind == 'barh':
            if kwargs.get('height') == None:
                height = 0.8
            else:
                height = kwargs.get('height')
            if kwargs.get('align') == None:
                align = 'center'
            else:
                align = kwargs.get('align')
            
            if type(y)==list:
                for col in y:
                    ax.barh(y = x, width= d[col], height= height, align= align,
                       data=kwargs.get('data'), alpha=kwargs.get('alpha'))
                    ax.legend(y)
                    
            else:
                
                ax.barh(y = x, width= d[y], height= height, align= align,
                       data=kwargs.get('data'), alpha=kwargs.get('alpha'))
        
        # ajustando elementos gráficos
        ax.set_xlabel(kwargs.get('xlabel'))
        ax.set_ylabel(kwargs.get('ylabel'))
        plt.title(kwargs.get('title'))
        
        if kwargs.get('ylim') != None:
            ax.set_ylim(kwargs.get('ylim'))
        if kwargs.get('xlim') != None:
            ax.set_xlim(kwargs.get('xlim'))
        
        if remove_frames.lower() == 'all':
            ax.spines['top'].set_visible(False)
            ax.spines['right'].set_visible(False)
            ax.spines['bottom'].set_visible(False)
            ax.spines['left'].set_visible(False)
        if remove_frames.lower() == 'left':
            ax.spines['left'].set_visible(False)
        if remove_frames.lower() == 'right':
            ax.spines['right'].set_visible(False)
        if remove_frames.lower() == 'bottom':
            ax.spines['bottom'].set_visible(False)
        if remove_frames.lower() == 'top':
            ax.spines['top'].set_visible(False)
            
### ------------------------------------------------------------------------------------------------------- ###