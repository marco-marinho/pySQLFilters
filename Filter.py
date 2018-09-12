
#Classe que contem um filtro
class Filter:

    #Inicializa o filtro com o nome da coluna a ser filtrada, sempre inicalizado como sendo do tipo igual
    def __init__(self, coluna):
        self.coluna = coluna
        self.isequal = True
        self.ismaior = False
        self.ismenor = False

    #Define os valores a serem filtrados na colunas, aceita um primitivo, uma lista ou uma tuple
    def setFiltro(self, filtro):
        if not filtro:
            self.filtro=[]
        elif(isinstance(filtro,int)):
            self.filtro = []
            self.filtro.append(filtro)
        elif(isinstance(filtro, str)):
            self.filtro=[]
            self.filtro.append(filtro)
        elif(isinstance(filtro,list)):
            self.filtro=filtro
        else:
            self.filtro=[]
            self.filtro.extend(list(filtro))

    #Define o limite superior a ser utilizado quando o filtro for do tipo maior
    def setUpperLimit(self, upperLimit):
        self.upperLimit = upperLimit

    #Define o limite inferior a ser utilizado quando o filtro for do tipo menor
    def setLowerLimit(self, lowerLimit):
        self.lowerLimit = lowerLimit

    #Retorna uma lista com os valores que filtram a coluna
    def getFiltro(self):
        return self.filtro

    #Retorna a coluna filtrada
    def getColuna(self):
        return self.coluna

    #Define se o filtro é do tipo maior
    def setMaior(self):
        self.isequal = False
        self.ismaior = True
        self.ismenor = False

    #Define se o filtro é do tipo menor
    def setMenor(self):
        self.isequal = False
        self.ismaior = False
        self.ismenor = True

    #Define se o filtro é do tipo igual
    def setEqual(self):
        self.isequal = True
        self.ismaior = False
        self.ismenor = False
    
    #Retorna o simbolo correspondente ao tipo de filtro a ser utilizado na querry SQL
    def getSimbolo(self):
        if self.isequal:
            return '='
        elif self.ismaior:
            return '>'
        elif self.ismenor:
            return '<'
