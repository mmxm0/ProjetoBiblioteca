# coding=utf-8
import random
import string
from datetime import date

class Livro:
    idd = 0 # VARIAVEL ESTATICA QUE FUNCIONA COMO CONTADORA DE OBJETOS DA CLASSE
            # SE FOREM CRIADOS OBJETOS DA CLASSE LIVRO, ESSA VARIAVEL VAI SER > 0
    def __init__(self,titulo=None,autor=None,cod_de_barras=None,genero=None,situacao=True,datadevolucao=None):
        self.__titulo = titulo
        self.__autor = autor
        Livro.idd +=1
        self.__generoLiterario = genero
        self.__codLivro = cod_de_barras
        self.__situacao = situacao
        self.__dataDeDevolucao = datadevolucao
    def __repr__(self):
        return str(self.__titulo)+ "*" +str(self.__autor)+ "*" + str(self.__generoLiterario)+ "*"+str(self.__situacao)+"*"+str(self.__dataDeDevolucao)

    def getTitulo(self):
        return self.__titulo
    def getSituacao(self):
        return self.__situacao
    def getAutor(self):
        return self.__autor

    def getQtddObjLivro(self):
        return Livro.idd

    def getCodBarras(self):
        return self.__codLivro

    def getGeneroLiterario(self):
        return self.__generoLiterario

    def getDataDeDevolucao(self):
        return self.__dataDeDevolucao

    def setDataDeDevolucao(self,novaData):
        self.__dataDeDevolucao =novaData

    def setTitulo(self,titulo):
        self.__titulo = titulo

    def setAutor(self, autor):
        self.__autor = autor

    def setCodLivro(self,cod):
        self.__codLivro = cod

    def setGeneroLiterario(self,genero):
        self.__generoLiterario = genero

    def setSituacao(self,situacao=False):
        self.__situacao = situacao

    def strHoje(self):
        hoje = date.today()
        auxHoje = str(hoje)
        hj = ''
        for i in auxHoje:
            if i != "-":
                hj += i
        return int(hj)
    def strFuturo(self):
        hoje = date.today()
        futuro = self.getDataDeDevolucao()
        auxFuturo = str(futuro)
        ft = ''
        for k in auxFuturo:
            if k != "-":
                ft += k
        return int(ft)


def geradorCodigo(nome):
    cod = 0
    for i in nome:
        cod += ord(i)
    return cod
