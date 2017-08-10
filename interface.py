# coding=utf-8
from ArvoreVP import *
from datetime import date
import time
class Interface:
    def __init__(self, arvoreUser,arvoreLivro):
        self.__Arvoreusuario = arvoreUser
        self.__Arvorelivro = arvoreLivro

    def emprestimoCheck(self,userKey,livroKey):
        usuario = self.__Arvoreusuario.pesquisar(userKey)
        livro = self.__Arvorelivro.pesquisar(int(livroKey))
        usuario = usuario.getValor()
        livro = livro.getValor()
        if usuario != None and livro != None:
            if usuario.getSituacao():
                if livro.getSituacao():
                    if len(usuario.getListaLivros())<5:
                       return True
                    else:
                        print("usuario já atingiu a quantidade máxima de empréstimos")
                        return False
                else:
                    print("O Livro Solicitado pelo usuário não possui exemplares disponíveis para emprestimo")
                    return False
            else:
                print("Usuario está com pendência na biblioteca")
                return False
        else:
            if usuario == None:
                print("Usuário não encontrado...Tente novamente")
            elif livro == None:
                print("Livro não encontrado... Tente novamente")
            return False

    def emprestimo(self,userKey, livroKey):
        livroKey = geradorCodigo(livroKey)
        usuario = self.__Arvoreusuario.pesquisar(int(userKey))
        livro = self.__Arvorelivro.pesquisar(int(livroKey))
        usuario = usuario.getValor()
        livro = livro.getValor()

        if self.emprestimoCheck(userKey,livroKey):
            hoje = date.today()###
            futuro = date.fromordinal(hoje.toordinal()+15)
            if len(usuario.getListaLivros()) <= 5:
                usuario.setEMlistaLivros(livro)
                livro.setSituacao()
                livro.setDataDeDevolucao(futuro)##
                usuario.setListaDatasDeDevolucao(futuro)
                usuario.setSituacao(True)
                aux = ''
                aux += "O emprestimo do livro:  foi realizado com sucesso.\n" 
                aux += "Empréstimo feito no dia: "+str(hoje)+"\nData de devolução: "+str(futuro)+"\n"
                print (aux)
                return
            else:
                aux =''
                aux += "O emprestimo do livro não foi realizado com sucesso.\n" 
                aux += "Para realizar mais emprestimos, devolva algum livro."
                print (aux)
                return

    def devolucao(self, userKey, livroKey):
        livroKey = geradorCodigo(livroKey)
        usuario = self.__Arvoreusuario.pesquisar(int(userKey))
        livro = self.__Arvorelivro.pesquisar(int(livroKey))
        nomeLivro = self.__Arvorelivro.pesquisar(int(livroKey)).getValor()
        if usuario!= None and livro!=None:
            if nomeLivro in usuario.getValor().getListaLivros():
                indice = usuario.getValor().getListaLivros().index(nomeLivro)
                usuario.getValor().removeLivroListaLivros(indice)
                livro.getValor().setSituacao(True)
                hj = livro.getValor().strHoje()
                ft = livro.getValor().strFuturo()
                if hj < ft:
                    printar = "Você devolveu na data prevista e não gerou multas"
                else:
                    multa = hj - ft
                    printar = "Você não entregou na data prevista, entao sua multa é de"+str(multa)
                print (printar)
                return
            else:
                print("O usuário não pode devolver um livro que não possui")
                return
        else:
            if usuario==None:
                print("Usuário não cadastrado")
            elif livro==None:
                print("Livro não cadastrado")

    def cadastrarUsuario(self, nome, curso, cpf):
        novouser = Usuario(nome, curso, cpf)
        self.__Arvoreusuario.adicionar(int(cpf), novouser)
        print("O usuario: " + nome + " foi cadastrado com sucesso")

    def descadastrarUsuario(self, cpf):
        try:
            nouser = self.__Arvoreusuario.pesquisar(int(cpf))
            nome = nouser.getValor().getNome()
            #    nome = nouser.getNome()
            #AttributeError: 'NoArvoreVp' object has no attribute 'getNome'
            self.__Arvoreusuario.deletar(int(cpf))
            print("O usuario: " + nome + " foi descadastrado com sucesso")
        except:
            print("Usuario não esta cadastrado no sistema")

    def cadastrarLivro(self, titulo, autor,genero):
        codigo = geradorCodigo(titulo)
        novolivro = Livro(titulo, autor, codigo, genero)
        self.__Arvorelivro.adicionar(int(codigo), novolivro)
        print("O livro: " + titulo + " foi cadastrado com sucesso")

    def descadastrarLivro(self, codigo):
        try:
            codigo = geradorCodigo(codigo)
            nolivro = self.__Arvorelivro.pesquisar(int(codigo))
            titulo = nolivro.getValor().getTitulo()
            self.__Arvorelivro.deletar(int(codigo))
            print("O Livro: " + titulo + " foi descadastrado com sucesso")
        except:
            print("Livro não encontrado no sistema.")
            ValueError: 'NoneType object has no attribute getTitulo'

    def imprimirMenuPrincipal(self):
        print("{:^100}".format(" ------------------------------------ "))
        print("{:^100}".format("|         BIBLIOTECA UFRPE           |"))
        print("{:^100}".format("| - Escolha uma opção                |"))
        print("{:^100}".format("|  (1)Usuário                        |"))
        print("{:^100}".format("|  (2)Livro                          |"))
        print("{:^100}".format("|  (3)Imprimir Acervo                |"))
        print("{:^100}".format("|  (4)Sair                           |"))
        print("{:^100}".format(" ------------------------------------ "))

    def imprimirMenuUsuario(self):
        print("{:^100}".format(" ------------------------------------"))
        print("{:^100}".format("|         BIBLIOTECA UFRPE           |"))
        print("{:^100}".format("| - Escolha uma opção                |"))
        print("{:^100}".format("|                                    |"))
        print("{:^100}".format("|  (1)Cadastrar usuário              |"))
        print("{:^100}".format("|  (2)Remover usuário                |"))
        print("{:^100}".format("|  (3)Relatório usuário              |"))
        print("{:^100}".format("|  (4)Emprestimo                     |"))
        print("{:^100}".format("|  (5)Devolução                      |"))
        print("{:^100}".format("|  (6)Voltar                         |"))
        print("{:^100}".format(" ------------------------------------"))

    def imprimirMenuLivro(self):
        print("{:^100}".format(" ------------------------------------"))
        print("{:^100}".format("|         BIBLIOTECA UFRPE           |"))
        print("{:^100}".format("| - Escolha uma opção                |"))
        print("{:^100}".format("|  (1)Cadastrar livro                |"))
        print("{:^100}".format("|  (2)Remover livro                  |"))
        print("{:^100}".format("|  (3)Relatório livro                |"))
        print("{:^100}".format("|  (4)Voltar                         |"))
        print("{:^100}".format(" ------------------------------------"))

    def relatorioLivro(self,chave):
        try:
            chave = geradorCodigo(chave)
            livro = self.__Arvorelivro.pesquisar(chave)
            lista = str(livro.getValor())
            if "*" in lista:
                lista = lista.split("*")
                if lista[3] == "True":
                    lista[3] = "Disponivel"
                else:
                    lista[3] = "NÃO Disponivel"
                self.imprimeRelatorioLivro(lista)
            else:
                print("Livro não cadastrado")
        except:
            print("         Livro não encontrado, por favor tente novamente!")
            ValueError: ""

    def imprimeRelatorioLivro(self, lista):

        print("{:^100}".format(" ------------------------------------------------------ "))
        print("{:^100}".format("         BIBLIOTECA UFRPE                             "))
        print("{:^100}".format("- Relatorio livro: %s                                "%lista[0]))
        print("{:^100}".format("  Código do livro: %s                                 "%geradorCodigo(lista[0])))
        print("{:^100}".format("  Autor: %s                                           "%lista[1]))
        print("{:^100}".format("  Gênero Literário %s                                 "%lista[2]))
        if lista[3] == "Disponivel":
            print("{:^100}".format("  O livro se encontra          %s                     "%lista[3]))
        else:
            print("{:^100}".format(" A data de devolução para esse livro é: %s           "%lista[4]))
        print("{:^100}".format(" ------------------------------------------------------ "))
        time.sleep(3)

    def relatorioUsuario(self,keyUser):
        try:
            usuario = self.__Arvoreusuario.pesquisar(keyUser)
            lista = str(usuario.getValor())
            lista = lista.split("#")
            if lista[3] == "True":
                lista[3] = "HABILITADO"
            else:
                lista[3] = "NÃO HABILITADO"

            if lista[4] != "[]":
                string = str(lista[4])
                string2 = str(lista[5])
                string = string.replace("[","")
                string = string.replace("]","")
                string = string.replace(",","\n")
                lista[4] = str(string)
                string2 = string2.replace("[","")
                string2 = string2.replace("]","")
                string2 = string2.replace(",","\n")
                lista[5] = str(string2)

            self.imprimeRelatorioUsuario(lista)
        except:
            print("Usuário não escontrado")
            ValueError: ""

    def imprimeRelatorioUsuario(self,lista):
            print("{:^100}".format(" ------------------------------------------------------ "))
            print("{:^100}".format("         BIBLIOTECA UFRPE                             "))
            print("{:^100}".format("- Relatorio Usuario: %s                              "%lista[0].title()))
            print("{:^100}".format(" CPF: %s                                             "%lista[2]))
            print("{:^100}".format(" Curso: %s                                           "%lista[1]))
            print("{:^100}".format(" Usuário %s para fazer empréstimos na Biblioteca     "%lista[3]))
            if len(lista[4]) > 2:
                print("{:^100}".format(" %s possui os seguintes livros:                      "%lista[0]))
                print("{:^100}".format(" %s "%lista[4]))
                print("{:^100}".format(" Com as respectivas datas de devolução:              "))
                print("{:^100}".format(" %s "%lista[5]))
            else:
                print("{:^100}".format(" Usuario sem livros no momento"))
            print("{:^100}".format(" ------------------------------------------------------ "))
            time.sleep(3)

    def imprimirAcervo(self):
        print("{:^100}".format(" ------------------------------------------------------ "))
        print("{:^100}".format("         ACERVO BIBLIOTECA UFRPE                        "))
        print("{:^100}".format(" ------------------------------------------------------ "))
        listaAcervo = str(self.__Arvorelivro)
        listaAcervo = listaAcervo.replace("[","")
        listaAcervo = listaAcervo.replace("]","")
        listaAcervo = listaAcervo.split(",")
        for livroObject in listaAcervo:
            livroObject = livroObject.split(":")
            livroInfo = livroObject[1]
            livroInfo = livroInfo.split("*")
            if livroInfo[3] == "True":
                disponibilidade = "DISPONÍVEL"
            else:
                disponibilidade = "NÃO DISPONÍVEL"
            print("{:^100}".format(" %s        %s      %s"%(livroInfo[0],livroInfo[1],disponibilidade)))
        print("{:^100}".format(" ------------------------------------------------------ "))
        time.sleep(3)
    def loadDataLivros(self,leituraLivros):
        if "[" in leituraLivros:
            nodesLivro = leituraLivros.split(",")
            for noh in nodesLivro:
                noh = noh.replace("[", "")
                noh = noh.replace("]", "")
                noh = noh.split(":")
                objeLivro = noh[1]
                objeLivro = objeLivro.split("*")
                self.__Arvorelivro.adicionar(int(noh[0]),Livro(objeLivro[0], objeLivro[1], int(noh[0]), objeLivro[2], bool(objeLivro[3]),objeLivro[4]))
        else:
            print("vazio")

    def loadDataUser(self, leituraUser):
        if "[" in leituraUser and len(leituraUser)>2:
            nodesLivro = leituraUser.split(",")
            for noh in nodesLivro:
                noh = noh.split(":")
                if "[" in noh[0]:
                    noh[0] = noh[0].replace("[","")
                objeUser = noh[1]
                objeUser = objeUser.split("#")
                listalivros = objeUser[4]
                listalivros = listalivros.replace("[","")
                listalivros = listalivros.replace("]","")
                if len(listalivros) > 0:
                    listalivros = listalivros.split(",")
                    for i in range(len(listalivros)):
                        objetoLivro = listalivros[i].split()
                        objLivro = self.__Arvorelivro.pesquisar(objetoLivro[0]).getValor()
                        listalivros[i] = objLivro
                    listadata = objeUser[5]
                    listadata.replace("[", "")
                    listadata.replace("]", "")
                    listadata = listadata.split()
                    print(len(listadata))
                else:
                    listalivros = []
                    listadata = []
                self.__Arvoreusuario.adicionar(int(noh[0]),Usuario(objeUser[0],objeUser[1],int(objeUser[2]),bool(objeUser[3]),listalivros,listadata))

#OPEN CONSOLE
arquivoLoadLivros = open("arvoreLivrosEscreve.txt","r")
leituraLivros = arquivoLoadLivros.read()
arquivoLoadLivros.close()
arquivoLoadUsuarios = open("arvoreUsuariosEscreve.txt","r")
leituraUsuarios = arquivoLoadUsuarios.read()
arquivoLoadUsuarios.close()
erro = "Opcao invalida, tente novamente"
arvoreUser = ArvoreVP()
arvoreLivro = ArvoreVP()
biblioteca = Interface(arvoreUser,arvoreLivro)
biblioteca.loadDataLivros(leituraLivros)
biblioteca.loadDataUser(leituraUsuarios)

#CONSOLE
while True:
    biblioteca.imprimirMenuPrincipal()
    opcao = input()
    if opcao == '1': #USUARIO
        biblioteca.imprimirMenuUsuario()
        opcao = input()
        if opcao == '1': #cadastro
            biblioteca.cadastrarUsuario(nome = input("Informe o nome: "),curso = input("Informe o curso: "),cpf = int(input("Informe o cpf: ")))
        elif opcao == '2':#remover
            biblioteca.descadastrarUsuario(cpf = int(input('Informe o cpf: ')))
        elif opcao == '3':#Relatorio
            biblioteca.relatorioUsuario(keyUser = int(input("Informe o cpf: ")))
        elif opcao == '4':#pedir emprestimo
            biblioteca.emprestimo(userKey = int(input("Informe o cpf do usuário: ")), livroKey = input("Informe o nome do livro: "))
        elif opcao == '5': #devolucao
            biblioteca.devolucao(userKey = int(input("Informe o cpf do usuário: ")), livroKey = input("Informe o nome do livro: "))
        elif opcao == '6':
            pass
        else:
            print(erro)
    elif opcao == '2': #LIVRO
        biblioteca.imprimirMenuLivro()
        opcao = input()
        if opcao == '1': #cadastrar
            biblioteca.cadastrarLivro(titulo = input("Informe o titulo: "),autor = input("Informe o autor: "),genero = input("Informe o genero do livro: "))
           #TypeError: cadastrarLivro() got an unexpected keyword argument 'codigo' 
        elif opcao == '2':#remover
            biblioteca.descadastrarLivro(codigo = input("Informe o nome do livro: "))
        elif opcao == '3': #relatorio livro
            biblioteca.relatorioLivro(chave = input("Informe o nome do livro: "))
        elif opcao == '4':
            pass
        else:
            print(erro)
    elif opcao == '3':#Acervo
        biblioteca.imprimirAcervo()

    elif opcao == "4":#SAIR
        time.sleep(1)
        break
    else:
        print(erro)
arquiUsuarios = open("arvoreUsuariosEscreve.txt","w")
arquiUsuarios.write(str(arvoreUser))
arquivoLivros = open("arvoreLivrosEscreve.txt","w")
arquivoLivros.write(str(arvoreLivro))
arquivoLivros.close()
arquiUsuarios.close()
