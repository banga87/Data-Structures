from email.errors import NonPrintableDefect
from multiprocessing import current_process
from platform import node
from types import NoneType
import Node

class DoubleLinkedList:
    def __init__(self) -> None:
        self.head_node = None
        self.tail_node = None

    def add_to_head(self, value):
        new_head = Node(value)
        current_node = self.head_node

        if current_node != None:
            current_node.set_prev_node(new_head)
            new_head.set_next_node(current_node)
        
        self.head_node = new_head

        if self.tail_node == None:
            self.tail_node = new_head

    def add_to_tail(self, value):
        new_tail = Node(value)
        current_tail = self.tail_node

        if current_tail != None:
            new_tail.set_prev_node(current_tail)
            current_tail.set_next_node(new_tail)

        self.tail_node = new_tail

        if self.head_node == None:
            self.head_node = new_tail
        

    def remove_head(self):
        removed_head = self.head_node

        if removed_head == None:
            return None
        
        self.head_node = removed_head.get_next_node()

        if self.head_node != None:
            self.head_node.set_prev_node(None)

        if removed_head != self.tail_node:
            self.remove_tail()
        
        return removed_head.get_value()

    def remove_tail(self):
        removed_tail = self.tail_node

        if removed_tail == None:
            return None

        if self.tail_node != None:
            self.tail_node.set_next_node(None)

        if removed_tail != self.head_node:
            self.remove_head()

        return removed_tail.get_value()

    def remove_by_value(self, value_to_remove):
        node_to_remove = None
        current_node = self.head_node

        # Loop through, find the value and store for later use
        while current_node != None:
            if current_node.get_value == value_to_remove:
                node_to_remove = current_node
                break
            current_node = current_node.get_next_node()

        if node_to_remove == None:
            return None

        if node_to_remove == self.head_node:
            self.remove_head()
        elif node_to_remove == self.tail_node:
            self.remove_tail()
        else:
            next_node = node_to_remove.get_next_node()
            prev_node = node_to_remove.get_prev_node()
            next_node.set_prev_node(prev_node)
            prev_node.set_next_node(next_node)
        return node_to_remove

    def stringify_list(self):
        string = ''
        current_node = self.head_node
        while current_node:
            if current_node != None:
                string += str(current_node.get_value()) + "\n"
                current_node = current_node.get_next_node()
        return string
        
                

