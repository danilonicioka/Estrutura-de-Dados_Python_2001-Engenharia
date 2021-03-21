# Node - função classe nó -> construtor
class Node:

    def __init__(self, data): #os argumentos serão o dado da lista e o ponteiro
        self.data = data #dado
        self.next = None #referência, mas no primeiro caso coloca vazio. A função None no python representa Vazio

class LinkedList:
    def __init__(self):
        self.head = None #cabeça da lista

    def append(self, data): #função para adicionar elementos na lista
        new_node = Node(data) #nova variável para o nó atual
        if self.head == None: #if para verificar se lista está vazia ou possui algum elemento
            self.head = new_node #se estiver vazia o novo nó será adicionado na cabeça da lista
            return

        current_node = self.head

        while current_node.next: #percorrer toda a estrutura, a condição só se tornará falsa quando chegar no final da lista
            current_node = current_node.next #passa cada nó atual para o próximo

        current_node.next = new_node #ao chegar no final(saiu do while), define-se o nó atual como o novo
        return

    def length(self): #para achar o tamanho da lista
        if self.head == None:
            return 0 #se o head estiver vazio significa que não há elementos na lista

        current_node = self.head #vai para o head
        total = 0 #contador
        while current_node: #só retornará falso quando chegar no final da lista
            total += 1 #se não está no final, aumenta o contador
            current_node = current_node.next #passa para o próximo nó

        return total #ao sair do while, terá a quantidade de elementos em total

    def to_list(self): #função para transformar a linked list em uma array normal no Python
        node_data = [] #define-se um vetor vazio
        current_node = self.head

        while current_node:
            node_data.append(current_node.data) #percorre a lista e coloca os dados do nó atual no vetor
            current_node = current_node.next
        return node_data #retorna o vetor com os dados da lista

    def display(self): #função para exibir os dados da lista
        contents = self.head

        if contents is None: #verifica se há algum dado na cabeça da lista
            print("List has no elements")

        while contents:
            print(contents.data)
            contents = contents.next #passa para o próximo nó
        print("------------") #print apenas para separar

    #Retorna o valor do nó do índice que for informado
    def get(self, index):
        if index >= self.length() or index < 0:
            print("Error: Index out of range")
            return None
        current_idx = 0 #começa a busca pelo índice 0 no head
        current_node = self.head
        while current_node != None: #percorre a lista procurando o índice
            if current_idx == index:
                return current_node.data
            current_node = current_node.next #anda na lista
            current_idx += 1

    def reverse_liskedlist(self): #função para reverter a linked list
        previous_node = None #estamos no primeiro elemento e não há nada antes, logo é vazio
        current_node = self.head

        while current_node != None: #percorrendo a lista
            next = current_node.next #auxiliar para guardar o node.next antigo
            current_node.next = previous_node #como está invertendo, o próximo nó será o anterior na definição antiga
            previous_node = current_node #o anterior será o node que está
            current_node = next #passa para o próximo node anterior para continuar invertendo
        self.head = previous_node

    #Implementar função que busca um item e retorna se existe ou não
    #def search_item(data):

    #Implementar função que remove o primeiro item da lista
    #def remove_at_start()

    #Implementar função que remove o último item da lista
    #def remove_at_end()

    #Implementar função que insere um item no começo
    #def insert_at_start()

    #Implementar função que insere um item no começo
    #def insert_at_end()

    #Implementar função que remove o elemento pelo valor
    #def remove_element_by_value(value)

    #Implementar função que insere um item no index especificado
    #def insert_at_index(index, data)

#Test
my_list = LinkedList()
my_list.display()

my_list.append(3)
my_list.append(2)
my_list.append(7)
my_list.append(1)

my_list.display()

print("The total number of elements are: "+str(my_list.length())) #str transforma em string
print(my_list.to_list())

my_list.reverse_liskedlist()
my_list.display()

#my_list.search_item(7)
#my_list.search_item(77)

#my_list.remove_at_start()
my_list.display()

#my_list.remove_at_end()
my_list.display()

#my_list.insert_at_start(1)
my_list.display()

#my_list.insert_at_end(3)
my_list.display()

#my_list.remove_element_by_value(3)
my_list.display()

#my_list.insert_at_index(2, 88)
my_list.display()