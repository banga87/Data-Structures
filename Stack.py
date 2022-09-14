import Node

class Stack:
    # We can adjust the default limit if needed.
    def __init__(self, limit=None):
        self.top_item = None
        self.limit = limit
        self.size = 0
        
    def push(self, value):
        if self.has_space():
            new_item = Node(value)
            new_item.set_next_node(self.top_item)
            self.top_item = new_item
            self.size += 1
        else:
            print("The stack is full.")

    def pop(self):
        if not self.is_empty():
            item_to_remove = self.top_item
            self.top_item = item_to_remove.get_next_node()
            self.size -= 1
            return item_to_remove.get_value()
        else:
            print("Stack is empty!")

    def peek(self):
        if not self.is_empty:
            return self.top_item.get_value()

    def has_space(self):
        return self.limit > self.size

    def is_empty(self):
        return self.size == 0