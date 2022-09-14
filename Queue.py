import Node

class Queue:
    def __init__(self, max_size):
        self.head = None
        self.tail = None
        self.size = 0
        self.max_size = max_size        

    def peek(self):
        if self.size > 0:
            return self.head_node.get_value()
        else:
            print("The queue is empty!")

    def get_size(self):
        return self.size

    def has_space(self):
        if self.max_size == None:
            return True
        else:
            return self.max_size > self.get_size()

    def is_empty(self):
        if self.get_size() == 0:
            return True
        else:
            return False

    def enqeue(self, value):
        if self.has_space():
            new_node = Node(value)
            if self.is_empty():
                self.head = new_node
                self.tail = new_node
            else:
                self.tail.set_next_node(new_node)
                self.tail = new_node
                self.size += 1
        else:
            print("Sorry, no more room!")
                
    def dequeue(self):
        if not self.is_empty():
            node_to_remove = self.head
            if self.get_size() == 1:
                self.head = None
                self.tail = None
            else:
                self.head = node_to_remove.get_next_node()
                return self.node_to_remove.get_value()
            self.size -= 1
        else:
            print('Queue is empty.')



