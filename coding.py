from math import log
from util import Node
from heapq import *
from itertools import groupby

class SourceUnit:
    def __init__(self, name, probability):
        self.name = name
        self.probability = probability

    def entropy(self):
        return self.log2(1 / self.probability) 

    def __repr__(self):
        return "{" + "name: {0}, probability: {1}".format(self.name, self.probability) + "}"

    @staticmethod
    def log2(number):
        return log(number, 2)


class Coding():
    def __init__(self, source_units):
        self.source_units = source_units
        if not self.is_source_uints_valid():
            raise Exception("Source unit not valid")
        self.codex = []

    def __repr__(self):
        return str([item for item in self.source_units])

    def array_of_probability(self):
        return [source_unit.probability for source_unit in self.source_units]

    def encode_table(self):
        result = {}
        for i in range(len(self.source_units)):
            result[self.source_units[i].name] = self.codex[i]
        return result

    def decode_table(self):
        result = {}
        for i in range(len(self.source_units)):
            result[self.codex[i]] = self.source_units[i].name
        return result

    @staticmethod
    def find(key, keys):
        result = []
        for item in keys:
            if item.startswith(key):
                result.append(item)
        return result

    def code(self, text, table):
        keys = table.keys()
        alt_text = text

        temp = ''
        for i in range(len(text)):
            temp += text[i]
            find_keys = Coding.find(temp, keys)
            if len(find_keys) == 1 and temp == find_keys[0]:
                alt_text = alt_text.replace(temp, table[find_keys[0]], 1)
                temp = ''

        return alt_text

    def encode(self, text):
        table = self.encode_table()
        return self.code(text, table)
    
    def decode(self, text):
        table = self.decode_table()
        return self.code(text, table)

    def sort(self, reverse=False):
        self.source_units = sorted(self.source_units, key=lambda obj: obj.probability, reverse=reverse)
        
    def is_source_uints_valid(self):
        sum = 0
        for source_unit in self.source_units:
            sum += source_unit.probability
        return abs(sum - 1) < 0.00000000001

    def source_units_average_length(self):
        if not self.is_source_uints_valid():
            raise Exception("Source units is not valid") 

        average_length = 0;
        for i in range(len(self.source_units)):
            average_length += self.source_units[i].probability * len(self.codex[i])

        return average_length

    def entropy(self):
        if not self.is_source_uints_valid():
           raise Exception("Source units is not valid") 
        
        entropy = 0;
        for source_unit in self.source_units:
            entropy += source_unit.probability * source_unit.entropy()

        return entropy

    def k_t(self):
        return self.entropy() / self.source_units_average_length()

    def k_n(self):
        return SourceUnit.log2(len(self.source_units)) / self.source_units_average_length()

    @staticmethod
    def source_units_from_text(text):
        text_length = len(text)
        return [SourceUnit(a, len(list(b))/text_length) for a, b in groupby(sorted(text))]

class Shannon(Coding):
    def __init__(self, source_units):
        super().__init__(source_units)
        self.create_code()

    def create_code(self):
        self.sort(reverse=True)
        sum = 0
        l = 0
        for i in range(len(self.source_units)):
            l = int(self.source_units[i].entropy() + 1)
            self.codex.append(Shannon.bin(sum, l))
            sum += self.source_units[i].probability
        
    def __repr__(self):
        result = {}
        for i in range(len(self.source_units)):
            result[self.source_units[i].name] = self.codex[i]
        return str(result)
        

    @staticmethod
    def bin(number, length):
        result = ''
        for i in range(length):
            result += str(int(number * 2))
            number = number*2 - int(number*2)     
        return result 
        
class Fano(Coding):
    def __init__(self, source_units):
        super().__init__(source_units)
        self.codex = [''] * len(source_units)
        self.sort(reverse=True)
        self.create_code()

    def create_code(self):
        start = 0
        end = len(self.source_units)
        self.divide(self.array_of_probability(), start, end)

    @staticmethod
    def find_middle(array_of_probability, start, end):
        min = 1
        for i in range(start, end):
            delta = abs(sum(array_of_probability[start:i]) - sum(array_of_probability[i:end]))
            if delta < min:
                min = delta
                result = i
        return result

    def divide(self, array_of_probability, start, end):
        i = Fano.find_middle(array_of_probability, start, end)
        for j in range(start, i):
            self.codex[j] += "0"
        for j in range(i, end):
            self.codex[j] += "1"
        if end - start <= 2:
            return
        self.divide(array_of_probability, start, i)
        self.divide(array_of_probability, i, end)


class Huffman(Coding):
    def __init__(self, source_units):
        super().__init__(source_units)
        self.sort(reverse=False)
        self.codex = [''] * len(source_units)
        self.create_code()

    def create_code(self):
        item_queue = self.create_heap()
        self.get_code("", item_queue[0])

    def get_code(self, s, node):
        if node.item != None:
            if not s:
                self.codex[node.item] = "0"
            else:
                self.codex[node.item] = s
        else:
            self.get_code(s+"1", node.left)
            self.get_code(s+"0", node.right)


    def create_heap(self):
        item_queue = [Node(i, self.source_units[i].probability) for i in range(len(self.source_units))]
        heapify(item_queue)
        while len(item_queue) > 1:
            left = heappop(item_queue)
            right = heappop(item_queue)
            node = Node(None, left.weight + right.weight)
            node.setChildren(left, right)
            heappush(item_queue, node)
        return item_queue