class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return str(self.value)


class LinkedList:
    def __init__(self):
        self.head = None

    def __str__(self):
        cur_head = self.head
        out_string = ""
        while cur_head:
            out_string += str(cur_head.value) + " -> "
            cur_head = cur_head.next
        return out_string

    def append(self, value):

        if self.head is None:
            self.head = Node(value)
            return

        node = self.head
        while node.next:
            node = node.next

        node.next = Node(value)

    def size(self):
        size = 0
        node = self.head
        while node:
            size += 1
            node = node.next

        return size


def union(llist_1, llist_2):
    """
    Union function: Union of the 2 list given  
    Input: 
        llist_1 -> list 1
        llist_2 -> list 2
    Output:
        new_list -> union of list_1 and list_2   
    """
    # Your Solution Here
    if llist_1 == None or llist_2 == None:
        print("This is not a valid List")
        return LinkedList()

    new_list = LinkedList()
    node_1 = llist_1.head

    while node_1:
        new_list.append(node_1.value)
        node_1 = node_1.next
     #
    node_2 = llist_2.head
    #node_1 = llist_1.head
    while node_2:
        in_list = False
        while node_1:
            if node_2.value == node_1.value:
                in_list = True
                break
            node_1 = node_1.next
        if not in_list:
            new_list.append(node_2.value)
        node_2 = node_2.next
    return new_list


def intersection(llist_1, llist_2):
    """
    Intersection function: Intersection of the 2 list given  
    Input: 
        llist_1 -> list 1
        llist_2 -> list 2
    Output:
        intersected_elements -> Intersected elements of list_1 and list_2
    """
    # Your Solution Here
    if llist_1 == None or llist_2 == None:
        print("This is not a valid list")
        return LinkedList()

    intersected_elements = LinkedList()
    node_1 = llist_1.head
    node_2 = llist_2.head
    while node_1:
        while node_2:
            if node_1.value == node_2.value:
                intersected_elements.append(node_1.value)
                break
            node_2 = node_2.next
        node_2 = llist_2.head
        node_1 = node_1.next
    return intersected_elements


if __name__ == '__main__':

    # Test case 1
    linked_list_1 = LinkedList()
    linked_list_2 = LinkedList()

    element_1 = [3, 2, 4, 35, 6, 65, 6, 4, 3, 21]
    element_2 = [6, 32, 4, 9, 6, 1, 11, 21, 1]

    for i in element_1:
        linked_list_1.append(i)

    for i in element_2:
        linked_list_2.append(i)

    print("Union:")
    # expected: 3 -> 2 -> 4 -> 35 -> 6 -> 65 -> 6 -> 4 -> 3 -> 21 -> 6 -> 32 -> 4 -> 9 -> 6 -> 1 -> 11 -> 21 -> 1 ->
    print(union(linked_list_1, linked_list_2))
    print('\n')
    print("Intersection")
    # expected: 4 -> 6 -> 6 -> 4 -> 21 ->
    print(intersection(linked_list_1, linked_list_2))

    print('\n---------------------------------------------\n')

    # Test case 2

    linked_list_3 = LinkedList()
    linked_list_4 = LinkedList()

    element_1 = [3, 2, 4, 35, 6, 65, 6, 4, 3, 23]
    element_2 = [1, 7, 8, 9, 11, 21, 1]

    for i in element_1:
        linked_list_3.append(i)

    for i in element_2:
        linked_list_4.append(i)

    print("Union:")
    # expected: 3 -> 2 -> 4 -> 35 -> 6 -> 65 -> 6 -> 4 -> 3 -> 23 -> 1 -> 7 -> 8 -> 9 -> 11 -> 21 -> 1 ->
    print(union(linked_list_3, linked_list_4))
    print('\n')
    print("Intersection:")
    print(intersection(linked_list_3, linked_list_4))  # expected: nothing

    print('\n---------------------------------------------\n')

    # Test case 3

    linked_list_5 = LinkedList()
    linked_list_6 = LinkedList()

    element_1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    element_2 = []

    for i in element_1:
        linked_list_5.append(i)

    for i in element_2:
        linked_list_5.append(i)

    print("Union:")
    # expected: 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7 -> 8 -> 9 -> 10 ->
    print(union(linked_list_5, linked_list_6))
    print('\n')
    print("Intersection:")
    # expected: "This is not a valid list"
    print(intersection(linked_list_5, None))

    print('\n---------------------------------------------\n')

    # Test case 4

    linked_list_7 = LinkedList()
    linked_list_8 = LinkedList()

    element_1 = []
    element_2 = []

    for i in element_1:
        linked_list_7.append(i)

    for i in element_2:
        linked_list_8.append(i)

    print("Union:")
    print(union(linked_list_7, linked_list_8))  # expected: nothing
    print('\n')
    print("Intersection:")
    print(intersection(None, None))  # expected: This is not a valid list (s)
