class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self):
        return self.data

class LinkedList:
    def __init__(self):
        self.head = None
        
    def __iter__(self):
        node = self.head
        
        while node is not None:
            yield node
            node = node.next
            
    def add_first(self, node):
        node.next = self.head
        self.head = node
        
    def append(self, node):
        if self.head is None:
            self.head = node
            return
        
        last = self.head
        while last.next:
            last = last.next
            
        last.next = node
        
    def insert(self, prev_node, new_data):
        if prev_node is None:
            print("The node given must be in the linked list.")
            return
        
        new_node = Node(new_data)
        
        new_node.next = prev_node.next
        
        prev_node.next = new_node
        
    def delete(self, node):
        if node is None or node.next is None:
            print("Cannot delete the last node or a None node.")
        
        node.data = node.next.data
        node.next = node.next.next
            
    def __repr__(self):
        node = self.head
        nodes = []
        while node is not None:
            nodes.append(node.data)
            node = node.next
        nodes.append("None")
        return " -> ".join(nodes)
    
llist = LinkedList()

first_node = Node("a")

llist.head = first_node

second_node = Node("b")

third_node = Node("c")

first_node.next = second_node

second_node.next = third_node

llist.append(Node("d"))

llist.insert(second_node, "j")

llist.delete(first_node)

print(llist)
    