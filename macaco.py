from dataframe import *

class DataFrameMc():
    """docstring for DataFrameMc"""
    def __init__(self,dados=None):
        self.df = dataframe()
        self.colunas = []
        if dados != None:
            for coluna in dados:
                self.InserirColuna(dados[coluna],coluna)


    def addColumn(self,values,col_name):
        # Infere o tipo do dado. Caso encontre multiplos,
        # transforma em string

        if all(isinstance(x, int) for x in values):
            self.df.InsertIntColumn(values, col_name)
            self.colunas.append((col_name,'int'))

        elif all(isinstance(x, (float,int)) for x in values):
            self.df.InsertDoubleColumn(values, col_name)
            self.colunas.append((col_name,'double'))

        elif all(isinstance(x, str) for x in values):
            self.df.InsertStringColumn(values,col_name)
            self.colunas.append((col_name,'string'))
        else:
            string_values = [str(i) for i in list(values)]
            self.df.InsertStringColumn(string_values,col_name)
            self.colunas.append((col_name,'string'))

    def print(self):
        for col in self.colunas[0]:
            print(col)
            print(self.df)
    
    
    #def GetColuna(nome_coluna):
        

    # def GetLinha(linha)
    # def GetColuna(coluna)
    # def GetLoc(linha,coluna)
    # def Query()
