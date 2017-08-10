import string
import random

class Usuario:
    idd = 0
    def __init__(self,nome=None,curso=None,cpf=None,situacao=True,listalivros=[],listaData=[]):
        self.__nome = nome
        self.__curso = curso
        self.__cpf = cpf
        self.__situacao = situacao
        self.__listaLivros = listalivros
        self.__qttLivros = len(self.__listaLivros)
        self.__listaDatasDeDevolucao = listaData
        Usuario.idd += 1

    def __repr__(self):
        return self.__nome+"#"+self.__curso+"#"+str(self.__cpf)+"#"+str(self.__situacao)+"#"+str(self.__listaLivros)+"#"+str(self.__listaDatasDeDevolucao)

    def getNome(self):
        return self.__nome

    def setNome(self,novo):
        self.__nome = novo

    def getListaDatasDeDevolucao(self):
        return self.__listaDatasDeDevolucao

    def setListaDatasDeDevolucao(self,novaData):
        self.__listaDatasDeDevolucao = novaData

    def getCurso(self):
        return self.__curso

    def setCurso(self,novo):
        self.__curso = novo

    def getCpf(self):
        return self.__cpf

    def setCpf(self,novo):
        self.__cpf = novo

    def getSituacao(self):
        return self.__situacao

    def setSituacao(self,novo):
        self.__situacao = novo

    def getQttLivros(self):
        return self.__qttLivros

    def setIdd(self):
        Usuario.idd -= 1

    def getIdd(self):
        return Usuario.idd

    def getListaLivros(self):
        return self.__listaLivros

    def setEMlistaLivros(self, objLivro):
        self.__listaLivros.append(objLivro)

    def removeLivroListaLivros(self,objLivro):
        self.__listaLivros.pop(objLivro)

