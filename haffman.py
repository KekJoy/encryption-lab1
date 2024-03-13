from heapq import heapify, heappop, heappush


class Node:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

    def __lt__(self, other):
        # Определяем поведение оператора < для Node, чтобы heapq мог сравнивать узлы
        return self.freq < other.freq


def huffman_coding(symb2freq):
    """Построение дерева Хаффмана и создание кодов для символов."""
    # Создаем приоритетную очередь с узлами
    nodes = [Node(char, freq) for char, freq in symb2freq.items()]
    heapify(nodes)  # Превращаем список узлов в кучу на основе частот

    # Строим дерево Хаффмана
    while len(nodes) > 1:
        # Извлекаем два узла с наименьшей частотой
        node1 = heappop(nodes)
        node2 = heappop(nodes)

        # Создаем новый узел с этими двумя узлами в качестве детей
        merged = Node(None, node1.freq + node2.freq)
        merged.left = node1
        merged.right = node2

        # Возвращаем новый узел в кучу
        heappush(nodes, merged)

    # Дерево Хаффмана построено, остался один узел, являющийся корнем
    root = nodes[0]

    # Генерация кодов Хаффмана
    codes = {}

    def generate_codes(node, current_code=""):
        if node is None:
            return
        if node.char is not None:
            codes[node.char] = current_code
        generate_codes(node.left, current_code + "0")
        generate_codes(node.right, current_code + "1")

    generate_codes(root)
    return codes
