from Filter import *

#Classe que une filtros para gerar as querrys SQL
class FilterJoiner:

    #Inicializa a classe com uma lista, uma tuple ou somente um filtro
    def __init__(self, filters):

        if isinstance(filters, list):
            self.filters = filters
        elif isinstance(filters, tuple):
            self.filters = []
            self.filters.extend(filters)
        else:
            self.filters = []
            self.filters.append(filters)

        #self.filtersBackup = self.filters

        #Inicializa variaveis para armazenar os filtros e as respectivas colunas
        self.filtros = {}
        self.colunas = []

        #Itera os filtros recebidos para armazenar as colunas e filtros
        for filt in self.filters:
            if not filt.getFiltro():
                continue
            else:
                self.colunas.append(filt.getColuna())
                self.filtros[filt.getColuna()] = filt.getFiltro()

    #Monta a query SQL baseada no conjunto de filtros recebidos
    #Valores contidos no mesmo filtro serão sempre tratados como OR
    #Valores contidos em filtros diferentes serão sempre tratados como AND
    def getSQLQuery(self):
        if not self.colunas:
            query = ';'
        else:
            query = ' WHERE ('
            primeiraColuna = True
            for filtro in self.filters:

                if not filtro.getFiltro():
                    continue

                if not primeiraColuna:
                    query = query + ' AND ('
                else:
                    primeiraColuna = False

                for _ in filtro.getFiltro():
                    query = query+filtro.getColuna()+filtro.getSimbolo()+'%s'+' OR '
                query = query[:-4]
                query = query+')'
        return query

    #Retorna a lista de parametros para ser utilizada na query parametrizada
    def getSQLParameters(self):
        joinedFilter = []
        for col in self.colunas:
            joinedFilter.extend(self.filtros[col])
        return joinedFilter

    def __str__(self):
        return self.getSQLQuery()+str(self.getSQLParameters())

    def contains(self, outroFiltro):
        return set(outroFiltro.getSQLParameters()).issubset(self.getSQLParameters())

    def getFilters(self):
        return self.filters


    def getGenero(self, genero):
        try:
            filtros = self.getFilters()
            for filtro in filtros:
                if filtro.getColuna() == 'sexo':
                    filtros.remove(filtro)
            filtro_genero = Filter('sexo')
            filtro_genero.setFiltro(genero)
            filtros.append(filtro_genero)
        except Exception as e:
            print(e)
        
        return FilterJoiner(filtros)
