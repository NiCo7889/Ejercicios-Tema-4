"""
Desarrollar los algoritmos necesarios para generar un árbol de Huffman a partir de la siguiente tabla, para lo cual deberá calcular primero las frecuencias de cada carácter 
a partir de la cantidad de apariciones del mismo, para resolver las siguientes actividades:
- la generación del árbol debe hacerse desde los caracteres de menor frecuencia hasta los de mayor, en el caso de que dos caracteres tengan la misma frecuencia, primero se 
toma el que este primero en el alfabeto, el carácter “espacio” y “coma” se consideraran anteúltimo y último respectivamente en el orden alfabético;
- descomprimir los siguientes mensajes, cuyo árbol ha sido construido de la misma manera que el ejemplo visto anteriormente:
- Mensaje  1:  “100010111010110000101110100011100000110110000001111001111010010110
0001101001110011010001011101011111110100001111001111110011110100011000110000
00101101011110111111101110101101101110011101101111001111111001010010100101000001
011010110001011001101000111001001011000011001000110101101010111111111110110111
0111001000010010101100011111110001000111011001100101101000110111110101101000
1101110000000111001001010100011111100001100101101011100110011110100011000110
000001011010111110011100”
-  Mensaje 2: “01101010110111001010001111010111001101110101101101000010001110101001
011110100111111101110010100011110101110011011101011000011000100110100011100100
10001100010110011001110010010000111101111010”
- finalmente, calcule el espacio de memoria requerido por el mensaje original y el comprimido.
"""

import heapq
from collections import Counter

class Node:
    def __init__(self, char, freq, left=None, right=None):
        self.char = char
        self.freq = freq
        self.left = left
        self.right = right

    def __lt__(self, other):
        return self.freq < other.freq

class HuffmanTree:
    def __init__(self, data):
        self.data = data
        self.tree = self.build_tree()

    def build_tree(self):
        freqs = Counter(self.data)
        heap = [Node(char, freq) for char, freq in freqs.items()]
        heapq.heapify(heap)

        while len(heap) > 1:
            left = heapq.heappop(heap)
            right = heapq.heappop(heap)
            heapq.heappush(heap, Node(None, left.freq + right.freq, left, right))

        return heap[0]

    def create_encoding_table(self, root=None, code=''):
        if root is None:
            root = self.tree

        if root.char is not None:
            return {root.char: code}

        encoding_table = {}
        if root.left:
            encoding_table.update(self.create_encoding_table(root.left, code + '0'))
        if root.right:
            encoding_table.update(self.create_encoding_table(root.right, code + '1'))

        return encoding_table

    def compress(self, message):
        encoding_table = self.create_encoding_table()
        return ''.join(encoding_table[char] for char in message)

    def decompress(self, compressed_message):
        root = self.tree
        current_node = root
        decoded_message = []

        for bit in compressed_message:
            if bit == '0':
                current_node = current_node.left
            else:
                current_node = current_node.right

            if current_node.char is not None:
                decoded_message.append(current_node.char)
                current_node = root

        return ''.join(decoded_message)

# Crear el árbol de Huffman con la tabla dada
data = "aabc, deeeff"
huffman_tree = HuffmanTree(data)

# Mensajes comprimidos
compressed_message1 = "10001011101011000010111010001110000011011000000111100111101001011000011010011100110100010111010111111101000011110011111100111101000110001100000010110101111011111110111010110110111001110110111100111111100101001010010100000101101011000101100110100011100100101100001100100011010110101011111111111011011101110010000100101011000111111100010001110110011001011010001101111101011010001101110000000111001001010100011111100001100101101011100110011110100011000110000001011010111110011100"
compressed_message2 = "0110101011011100101000111101011100110111010110110100001000111010100101111010011111110111001010001111010111001101110101100001100010011010001110010010001100010110011001110010010000111101111010"

# Descomprimir los mensajes
decompressed_message1 = huffman_tree.decompress(compressed_message1)

decompressed_message2 = huffman_tree.decompress(compressed_message2)

print("Mensaje 1 descomprimido: ", decompressed_message1)
print("Mensaje 2 descomprimido: ", decompressed_message2)


def memory_usage(message, encoding_table=None):
    if encoding_table is None:
        # Asumimos 8 bits por carácter (ASCII)
        bits_per_char = 8
    else:
        bits_per_char = sum(len(encoding_table[char]) for char in message) / len(message)

    total_bits = len(message) * bits_per_char
    total_bytes = total_bits / 8

    return total_bytes

# Calcular el espacio de memoria requerido por el mensaje original y el comprimido
encoding_table = huffman_tree.create_encoding_table()
original_memory_usage1 = memory_usage(decompressed_message1)
original_memory_usage2 = memory_usage(decompressed_message2)
compressed_memory_usage1 = memory_usage(decompressed_message1, encoding_table)
compressed_memory_usage2 = memory_usage(decompressed_message2, encoding_table)

print("Espacio de memoria requerido por el mensaje 1 original: {:.2f} bytes".format(original_memory_usage1))
print("Espacio de memoria requerido por el mensaje 2 original: {:.2f} bytes".format(original_memory_usage2))
print("Espacio de memoria requerido por el mensaje 1 comprimido: {:.2f} bytes".format(compressed_memory_usage1))
print("Espacio de memoria requerido por el mensaje 2 comprimido: {:.2f} bytes".format(compressed_memory_usage2))
