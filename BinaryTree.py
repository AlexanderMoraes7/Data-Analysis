class No():
    def __init__(self, id, elemento : object, no_esq, no_dir): # Construtor da Classe
        self.id = id
        self.elemento = elemento
        self.no_esq = no_esq
        self.no_dir = no_dir
    def setId(self, id): # Alterar o identificador do Nó
        self.id = id
    def getId(self): # Receber o identificador do Nó
        return self.id
    def setElemento(self, elemento): # Alterar elemento
        self.elemento = elemento
    def getElemento(self): # Recebe o objeto contido no nóooo
        return self.elemento
    def setEsq(self, esq): # Altera o filho esquerdo
        self.no_esq = esq
    def getEsq(self): # Recebe o filho esquerdo do nó
        return self.no_esq
    def setDir(self, dir): # Altera o filho direito
        self.no_dir = dir
    def getDir(self):
        return self.no_dir
    
class ArvoreBinaria():
    def __init__(self): # Construtor da Classe
        self.raiz = None # Inicia a árvore vazia
    def insere(self, id, elemento : object): # Inserção do Elemento
        novoNo = No(id, elemento, None, None)
        if (self.raiz == None):
            self.raiz = novoNo
        else:
            atual = self.raiz
            self.pai : No
            while(True):
                self.pai = atual
                if id < atual.getId(): # Vai inserir a esquerda
                    atual = atual.getEsq()
                    if atual == None: # pode inserir a esrqueda
                        self.pai.setEsq(novoNo)
                        return
                else: # Vai inserir a direita
                    atual = atual.getDir()
                    if atual == None: # Pode inserir a direita
                        self.pai.setId(novoNo)
                        return
                    
a = ArvoreBinaria()
a.insere(10,"A")
a.insere(5,"B")
a.insere(15,"C")
a.insere(2,"D")
a.insere(7,"E")
a.insere(12,"F")
a.insere(6,"G")
a.insere(8,"H")
