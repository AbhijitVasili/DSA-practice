class Node:
    def __init__(self,value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self,value):
        #Create a new node
        #Initialize the head of the linked list to point to the new node
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    # def append(selfr,value):
    #     #Create a new node
    #     #Add the new node to the end of the linked list
    # def prepend(self,value):
    #     #Create a new node
    #     #Add the new node to the beginning of the linked list
    # def insert(self,index,value):
    #     #Create a new node
    #     #Add the new node at the specified index in the linked list
my_linked_list = LinkedList(4)
print(my_linked_list.head.value)