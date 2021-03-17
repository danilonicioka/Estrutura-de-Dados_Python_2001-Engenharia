# Node - função classe nó -> construtor
class Node:

    def _init_(self, data): #os argumentos serão o dado da lista e o ponteiro
        self.data = data #dado
        self.next = None #referência, mas no primeiro caso coloca vazio. A função None no python representa Vazio

class LinkedList:
    def _init_(self):
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

    def reverse_liskedlist(self): #função para reverter a linked list
        previous_node = None #estamos no primeiro elemento e não há nada antes, logo é vazio
        current_node = self.head

        while current_node != None: #percorrendo a lista
            next = current_node.next #auxiliar para guardar o node.next antigo
            current_node.next = previous_node #como está invertendo, o próximo nó será o anterior na definição antiga
            previous_node = current_node #o anterior será o node que está
            current_node = next #passa para o próximo node anterior para continuar invertendo
        self.head = previous_node

#Test
my_list = LinkedList()
my_list.display()

my_list.append(3)
my_list.append(7)
my_list.append(2)
my_list.append(1)

my_list.display()