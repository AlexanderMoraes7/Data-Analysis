class No():
    #proximo = str # Aponta para o próximo nó da lista
    #elemento : object = str # Armazena o elemento de cada nó
    def __init__(self, elemento : object, proximo): # Construtor da classe
        self.elemento = elemento
        self.proximo = proximo
    def SetProximo(self, proximo): # Método que altera próximo nó da lista
        self.proximo = proximo
    def getProximo(self): # Método que recebe o próximo No da Lista
        return self.proximo
    def setElemento(self, elemento : object): # Método para alterar o elemento
        self.elemento = elemento
    def getElemento(self): # Método para receber o objeto contido no nó
        return self.elemento
    
class Lista():
    def __init__(self): # Construtor da classe Lista inicializada vazia
        self.inicio = None
    def insereInicio(self, elemento):
        novoNo : No = (elemento) # Passo 1 da figura 3
        novoNo = No(elemento, None)
        No.SetProximo(self.inicio) # Passo 2 da figura 3
        self.inicio = novoNo # Passo 3 da figura 3
    def removeInicio(self):
        auxiliar = self.inicio
        self.inicio = auxiliar.getProximo()
        return auxiliar.getElemento
    def imprimeLista(self): # Método para imprimir todo o conteúdo da Lista
        self.auxiliar = self.inicio # Auxiliar percorre a lista do início ao fim
        print("Início da Lista Ligada\n")
        while self.auxiliar != None: # Testa se ainda não chegou no final da Lista
            print(self.auxiliar.getElemento + "\n") # Imprime com o método String
            self.auxiliar = self.auxiliar.getProximo() # Passa para o próximo Nó da lista
        print("Final da Lista Ligada\n")
    def buscaElemento(self, posicao = int): # Busca o elemento na posição da lista
        self.auxiliar = self.inicio
        while ((posicao > 0) and (self.auxiliar != None)):
            if (posicao == 1):
                return self.auxiliar.getElemento()
            posicao - 1
            self.auxiliar = self.auxiliar.getProximo() # Passa para o próximo Nó da lista
        return None # A lista não possui elemento na posição indicada
    def liberaLista(self): # Libera todos os nós a lista
        while self.inicio != None:
            self.inicio = self.inicio.getProximo()
            # O Garbage collector do Java liberaria automaticamente o nó eliminado

class Cliente():
    def __init__(self, c = int, r = str, e = str, p = float): # Construtor da Classe Cliente
        self.codigo = c
        self.razaoSocial = r
        self.endereco = e
        self.previsaoVendas = p
    def __str__(self):
        return "Codigo: " + self.codigo + " Razão Social: " + self.razaoSocial
    def atualizaRazaoSocial(self, r = str):
        self.razaoSocial = r
    def atualizaPrevisao(self, p = float):
        self.previsaoVendas = p
    def mudaEndereco(self, e = str):
        self.endereco = e

listaClientes : Lista = Lista() # Cria a lista de clientes
c = Cliente(221, "Produtos excelentes LTDA", "Rua sem fim, 200", 5000.0)
# Inserindo elementos na Lista Ligada
listaClientes.insereInicio(c) # Usando uma variável cliente
listaClientes.imprimeLista()
listaClientes.insereInicio(Cliente(185, "Negócios Importantes SA", "Avenida Principal, 10", 12000.0))
listaClientes.insereInicio(Cliente(443, "Parceiros Críticos LTDA", "Rua dos negócios, 2000", 7000.0))
# Busca do elemento na posição 2 da lista
c : Cliente = listaClientes.buscaElemento(2)
if (c != None):
    print("Elemento da posição 2 da Lista Ligada\n")
    print(c)
# Removendo um elemento da Lista Ligada
# Necessário type casting para classe Cliente
clienteRemovido : Cliente = Cliente
clienteRemovido : Cliente = listaClientes.removeInicio()
print("Elemento removido da Lista Ligada")
print(c)
listaClientes.imprimeLista()
# Liberando toda a lista
print("Liberando toda a lista")
listaClientes.liberaLista()
listaClientes.imprimeLista()
