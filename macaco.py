from dataframe import *


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
            
            