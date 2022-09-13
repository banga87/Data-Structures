import Node
import LinkedList

def swap_nodes(input_list, value1, value2):
    node1_previous = None
    node2_previous = None
    node1 = input_list.head_node
    node2 = input_list.head_node

    if value1 == value2:
        print("Elements you want to swap are the same. Try again.")

    # Search for value1 and store in node1
    while node1 != None:
        if node1.get_value() == value1:
            break
        node1_previous = node1
        node1 = node1.get_next_node()

    # Search for value2 and store in node2
    while node2 != None:
        if node2.get_value() == value2:
            break
        node2_previous = node2
        node2 = node2.get_next_node()

    if node1 == None or node2 == None:
        print('Swap not possible. One or more values not found in list.')

    # Swap node1
    if node1_previous == None:
        input_list.head_node = node2
    else:
        node1_previous.set_next_node(node2)

    # Swap node2
    if node2_previous == None:
        input_list.head_node = node1
    else:
        node2_previous.set_next_node(node1)

    # We haven't reconnected the 'next nodes' yet
    # Temp value used so we don't orphan a node during swaps
    temp_node = node1.get_next_node()
    node1.set_next_node(node2.get_next_node())
    node2.set_next_node(temp_node)

def find_middle_node1(input_list):
    fast = input_list.head_node
    slow = input_list.head_node
    while fast:
        fast = fast.get_next_node()
        if fast:
            fast = fast.get_next_node()
            slow = slow.get_next_node()
    return slow

def find_middle_node2(input_list):
    fast = input_list.head_node
    slow = input_list.head_node
    counter = 1
    while fast:
        fast = fast.get_next_node()
        if counter % 2 != 0:
            slow = slow.get_next_node()
        counter += 1
    return slow

def nth_last_node(input_list, n):
    nth = None
    tail = input_list.head_node
    counter = 1
    while tail:
        tail = tail.get_next_node()
        counter += 1
        if counter >= n + 1:
            if nth == None:
                nth = input_list.head_node
            else:
                nth = nth.get_next_node()
    return nth

