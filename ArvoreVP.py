from Livro import *
from Usuario import *

class NoArvoreVp() :
    def __init__(self,chave,valor,cor):
        self._chave=chave
        self._valor=valor
        self._pai=None
        self._cor=cor
        self._esquerda=None
        self._direita=None
    def setPai(self,pai):
        self._pai=pai
    def getPai(self):
        return self._pai
    def setChave(self,chave):
        self._chave=chave
    def getChave(self):
        return self._chave
    def setDireito(self,direita):
        self._direita=direita
    def getDireito(self):
        return self._direita
    def getValor(self):
        return self._valor
    def setValor(self,valor):
        self._valor=valor
    def setEsquerdo(self,esquerda):
        self._esquerda=esquerda
    def getEsquerdo(self):
        return self._esquerda
    def getCor(self):
        return self._cor
    def setCor(self,cor):
        self._cor=cor

class ArvoreVP:
    def __init__(self):
        self._noneTree=NoArvoreVp(None,None,'preto')
        self._raiz=self._noneTree
        self._len=0

    def getRaiz(self):
        return self._raiz

    def getLen(self):
        return self._len

    def pesquisar(self,Chave):
        no=self._raiz
        while no!=self._noneTree and Chave!=no.getChave():
            if Chave < no.getChave():
                no=no.getEsquerdo()
            else:
                no=no.getDireito()
        return no

    def busca(self,chave):
        no = self._raiz
        resultado = None
        while no != None:
            if no.getChave() == chave:
                resultado = no
            if chave < no.getChave():
                no=no.getEsquerdo()
            else:
                no=no.getDireito()
        return resultado

    def minimoChave(self,no):
        if no==self._noneTree:
            return self._noneTree
        else:
            while no.getEsquerdo()!=self._noneTree:
                no=no.getEsquerdo()
        return no

    def maximoChave(self,no):
        if no==self._noneTree:
            return self._noneTree
        else:
            while no.getDireito()!=self._noneTree:
                no=no.getDireito()
            return no
    def sucessor(self,no):
        if no.getDireito()!=self._noneTree:
            no=no.getDireito()
            return self.minimoChave(no)
        else:        
            pai=no.getPai()
            while pai!=self._noneTree and no==pai.getDireito():
                no=pai
                pai=pai.getPai()
            return pai
    
    def predecessor(self,no):
        if no.getEsquerdo()!=self._noneTree:
            no=no.getEsquerdo()
            return self.maximoChave(no)
        pai=no.getPai()
        while pai!=self._noneTree and no==pai.getEsquerdo():
            no=pai
            pai=pai.getPai()
        return pai

    def rotEsquerda(self,no):
        aux=no.getDireito()
        no.setDireito(aux.getEsquerdo())
        if aux.getEsquerdo()!= self._noneTree:
            aux.getEsquerdo().setPai(no)
        aux.setPai(no.getPai())
        if no.getPai()==self._noneTree:
            self._raiz=aux
        elif no==no.getPai().getEsquerdo():
            no.getPai().setEsquerdo(aux)
        else:
            no.getPai().setDireito(aux)
        aux.setEsquerdo(no)
        no.setPai(aux)

    def rotDireita(self,no):
        aux=no.getEsquerdo()
        no.setEsquerdo(aux.getDireito)
        if aux.getDireito()!= self._noneTree:
            aux.getDireito().setPai(no)
        aux.setPai(no.getPai())
        if no.getPai()==self._noneTree:
            self._raiz=aux
        elif no==no.getPai().getDireito():
            no.getPai().setDireito(aux)
        else:
            no.getPai().setEsquerdo(aux)
        aux.setDireito(no)
        no.setPai(aux)
            
            

    def adicionar(self,chave,valor):
        if self._len < 2**20:
            self._len+=1
            no=NoArvoreVp(chave,valor,'vermelho')
            pivo=self._raiz
            aux=self._noneTree
            while pivo!=self._noneTree:
                aux=pivo
                if no.getChave()<pivo.getChave():
                    pivo=pivo.getEsquerdo()
                else:
                    pivo=pivo.getDireito()
            no.setPai(aux)
            if aux==self._noneTree:
                self._raiz=no
            elif chave<aux.getChave():
                aux.setEsquerdo(no)
            else:
                aux.setDireito(no)
            no.setEsquerdo(self._noneTree)
            no.setDireito(self._noneTree)
            self.balanceamentoApp(no)

    def balanceamentoApp(self,no):
        while no.getPai().getCor()=='vermelho':
            if no.getPai()==no.getPai().getPai().getEsquerdo():
                aux=no.getPai().getPai().getDireito()
                if aux.getCor()=='vermelho':
                    no.getPai().setCor('preto')
                    aux.setCor('preto')
                    no.getPai().getPai().setCor('vermelho')
                    no=no.getPai().getPai()
                else:
                    if no==no.getPai().getDireito():
                        no=no.getPai()
                        self.rotEsquerda(no)
                    no.getPai().setCor('preto')
                    no.getPai().getPai().setCor('vermelho')
                    self.rotDireita(no.getPai().getPai())
            else:
                aux=no.getPai().getPai().getEsquerdo()
                if aux.getCor()=='vermelho':
                    no.getPai().setCor('preto')
                    aux.setCor('preto')
                    no.getPai().getPai().setCor('vermelho')
                    no=no.getPai().getPai()
                else:
                    if no==no.getPai().getEsquerdo():
                        no=no.getPai()
                        self.rotDireita(no)
                    no.getPai().setCor('preto')
                    no.getPai().getPai().setCor('vermelho')
                    self.rotEsquerda(no.getPai().getPai())
        self._raiz.setCor('preta')
    
    def trocar(self,noX,noY):
        if noX.getPai()==self._noneTree:
            self._raiz=noY          
        elif noX==noX.getPai().getEsquerdo():
            noX.getPai().setEsquerdo(noY)        
        else:
            noX.getPai().setDireito(noY)            
        noY.setPai(noX.getPai())

    def deletar(self,chave):
        no=self.pesquisar(chave)
        if no==self._noneTree:
            return self._noneTree
        self._len-=1
        aux=no
        corOriginalAux=aux.getCor()
        if no.getEsquerdo()==self._noneTree:
            aux1=no.getDireito()
            self.trocar(no,no.getDireito())
        elif no.getDireito()==self._noneTree:
            aux1=no.getEsquerdo()
            self.trocar(no,no.getEsquerdo())
        else:
            aux = self.minimoChave(no.getDireito())
            corOriginalAux=aux.getCor()
            aux1=aux.getDireito()
            if aux.getPai()==no:
                aux1.setPai(aux)                
            else:
                self.trocar(aux,aux.getDireito())
                aux.setDireito(no.getDireito())
                aux.getDireito().setPai(aux)
            self.trocar(no,aux)
            aux.setEsquerdo(no.getEsquerdo())
            aux.getEsquerdo().setPai(aux)
            aux.setCor(no.getCor())
        if corOriginalAux == 'preto':
            self.balanceamentoDel(aux1)
            return no

    def balanceamentoDel(self,no):
        while no!=self._raiz and no.getCor()=='preto':
            if no== no.getPai().getEsquerdo():
                aux=no.getPai().getDireito()
                if aux.getCor()=='vermelho':
                    aux.setCor('preto')
                    no.getPai().setCor('vermelho')
                    self.rotEsquerda(no.getPai())
                    aux=no.getPai().getDireito()
                if aux.getEsquerdo().getCor()=='preto' and aux.getDireito().getCor()=='preto':
                    aux.setCor('vermelho')
                    no=no.getPai()
                else:
                    if aux.getDireito().getCor()=='preto':
                        aux.getEsquerdo().setCor('preto')
                        aux.setCor('vermelho')
                        self.rotDireita(aux)
                        aux=no.getPai().getDireito()
                    aux.setCor(no.getPai().getCor())
                    no.getPai().setCor('preto')
                    aux.getDireito().setCor('preto')
                    self.rotEsquerda(no.getPai())
                    no=self._raiz
            else:
                aux=no.getPai().getEsquerdo()
                if aux.getCor()=='vermelho':
                    aux.setCor('preto')
                    no.getPai().setCor('vermelho')
                    self.rotDireito(no.getPai())
                    aux=no.getPai().getEsquerdo()
                if aux.getDireito().getCor()=='preto' and aux.getEsquerdo().getCor()=='preto':
                    aux.setCor('vermelho')
                    no=no.getPai()
                else:
                    if aux.getEsquerdo().getCor()=='preto':
                        aux.getDireito().setCor('preto')
                        aux.setCor('vermelho')
                        self.rotEsquerda(aux)
                        aux=no.getPai().getEsquerdo()
                    aux.setCor(no.getPai().getCor())
                    no.getPai().setCor('preto')
                    aux.getEsquerdo().setCor('preto')
                    self.rotDireita(no.getPai())
                    no=self._raiz
        no.setCor('preto')

    def strPercorrer(self,no):
        string=''
        if no.getChave()!=None and no!=None :
            string+=self.strPercorrer(no.getEsquerdo())
            string+=str(no.getChave())+':'+str(no.getValor())+', '
            string+=self.strPercorrer(no.getDireito())
            return string
        return string

    def __repr__(self):
        string=self.strPercorrer(self._raiz)
        return '['+string[:-2]+']'
