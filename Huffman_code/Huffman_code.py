import sys
import heapq


class Node(object):
    def __init__(self, value, weight):
        self.value = value
        self.weight = weight
        self.left = None
        self.right = None

    def __lt__(self, other_node):
        return self.weight < other_node.weight

    def __str__(self):
        return str(self.value) + ' ' + str(weight)


class HuffmanTree:
    def __init__(self, pair=None, node=None):
        self.root = Node(None)


def get_frecuencies(data):
    """
    Get frecuencies function :Get the frecuencies of each char and then sorted these frecuencies 
    Input:
        data -> data str value 

    Outoput:
        frecuencies sorted 
    """
    frecuencies = {}
    for char in data:
        if not char in frecuencies:
            frecuencies[char] = 1
        else:
            frecuencies[char] += 1

    frecuencies_sorted = sorted(zip(frecuencies.values(), frecuencies.keys()))

    for s in range(len(frecuencies_sorted)):
        value = frecuencies_sorted[s][1]
        weight = frecuencies_sorted[s][0]
        frecuencies_sorted[s] = Node(value, weight)

    return frecuencies_sorted


def huffman_encoding(data):
    """
    Huffman encoding function : Huffman encoding function that encodes the data 
    Input:
        data -> data str value 
    Output:
        huffman code  
        huffman tree 
    """
    if len(get_frecuencies(data)) == 1:
        return '0' * len(data)

    huffman_code = ''
    huffman_tree = create_huffman_tree(data)
    table = create_huffman_table(huffman_tree)

    for elem in data:
        huffman_code += table[elem]

    return huffman_code, huffman_tree


def create_huffman_tree(data):
    """
    Create huffman tree function
    Input:
        data -> data str value
    Output:
        frecuencies  
    """
    frecuencies = get_frecuencies(data)
    heapq.heapify(frecuencies)

    while len(frecuencies) != 1:
        aux = Node(None, None)
        left = heapq.heappop(frecuencies)
        aux.left = left
        right = heapq.heappop(frecuencies)
        aux.right = right
        aux.weight = left.weight + right.weight
        heapq.heappush(frecuencies, aux)

    return frecuencies


def create_huffman_table(huffman_tree):
    """
    Create huffman table function
    Input: 
        huffman tree 
    Outout:
        table -> dict of frecuencies 
    """
    table = {}

    def get_binary_code(node, current_code=''):
        if node is None:
            return
        if node.left is None and node.right is None:
            table[node.value] = current_code
        get_binary_code(node.left, current_code + '0')
        get_binary_code(node.right, current_code + '1')

    get_binary_code(huffman_tree[0])
    return table


def huffman_decoding(data, tree):
    """
    huffman decoding fucntion
    Input:
        data -> data str value 
        tree -> huffman tree
    Output:
        decoded -> decoded data 
    """
    if len(get_frecuencies(data)) == 1:
        return len(get_frecuencies(data)) * str(tree.value)

    decoded = ''
    n = len(data)
    count = 0
    while count < n:
        current = tree[0]
        while current.left != None and current.right != None:
            if data[count] == '0':
                current = current.left
            else:
                current = current.right

            count += 1

        decoded += current.value
    return decoded


def test_cases_huffman_tree(data):
    """
    test cases huffman trees fucntion 
    Input:
        data -> data str value 
    Output:
        Warning messages
        or 
        Decoded messages  
    """

    if type(data) != str:
        print('Invalid data argument..', data)
        return

    if len(str(data)) == 0 or data is None:
        print('Empty data argument...')
        return

    if type(data) == None:
        print('No data argument provided...')

    print("The size of the data is: {}\n".format(sys.getsizeof(data)))
    print("The content of the data is: {}\n".format(data))

    encoded_data, tree = huffman_encoding(data)

    print("The size of the encoded data is: {}\n".format(
        sys.getsizeof(int(encoded_data.replace(' ', ''), base=2))))
    print("The content of the encoded data is: {}\n".format(encoded_data))

    decoded_data = huffman_decoding(encoded_data, tree)
    print("The size of the decoded data is: {}\n".format(
        sys.getsizeof(decoded_data)))
    print("The content of the encoded data is: {}\n".format(decoded_data))


if __name__ == "__main__":
    # Test case 1
    test_cases_huffman_tree('The bird is the word')  # decoded data
    # Test case 2
    test_cases_huffman_tree('hello world')  # decoded data
    # Test case 3
    test_cases_huffman_tree('')  # Empty data argument...
    # Test case 4
    test_cases_huffman_tree(123)  # Invalid data argument.. 123
    # Test case 5
    test_cases_huffman_tree(None)  # Invalid data argument.. None
