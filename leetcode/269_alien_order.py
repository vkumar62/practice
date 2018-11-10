
from collections import deque
class GraphNode:
    def __init__(self, char):
        self.char = char
        self.next_chars = dict()

    def __str__(self):
        return self.__repl__()

    def __repl__(self):
        return self.char + ' --> ' + ''.join(self.next_chars.keys())

class Solution:
    def alienOrder(self, words):
        """
        :type words: List[str]
        :rtype: str
        """
        def create_graph(words):

            graph_nodes = dict()

            for j in range(len(words)):
                word = words[j]
                for i in range(len(word)):
                    if word[i] not in graph_nodes:
                        graph_nodes[word[i]] = GraphNode(word[i])

                if j > 0:
                    word_0 = words[j-1]
                    for i in range(min(len(word_0), len(word))):
                        if word_0[i] != word[i]:
                            graph_nodes[word_0[i]].next_chars[word[i]] = graph_nodes[word[i]]
                            break
            return graph_nodes

        def topo_sort(node):
            if node.char in visited:
                return False 
            if node.char in temp_visited:
                return True
            temp_visited.add(node.char)
            for next_node in node.next_chars.values():
                cycle = topo_sort(next_node)
                if cycle:
                    return cycle
            visited.add(node.char)
            sorted_order.appendleft(node.char)
            return False

        # Create a graph of the characters
        graph = create_graph(words)

        sorted_order = deque()
        #Topo sort the graph
        visited = set()
        temp_visited = set()
        for char, graph_node in graph.items():
            if char not in visited:
                cycle = topo_sort(graph_node)
                if cycle:
                    return ''

        return ''.join(sorted_order)        

import pdb
words = [
  "wrt",
  "wrf",
  "er",
  "ett",
  "rftt"
]
pdb.set_trace()
print(Solution().alienOrder(words))
words = [
  "z",
  "x"
]
print(Solution().alienOrder(words))
words = [
  "z",
  "x",
  "z"
] 
print(Solution().alienOrder(words))
words = []
print(Solution().alienOrder(words))
words = [
  "z",
  "z"
] 
print(Solution().alienOrder(words))
words = ["ab","adc"]
print(Solution().alienOrder(words))
words = ["wnlb"]
print(Solution().alienOrder(words))
words = ["wrt", "wrtk"]
print(Solution().alienOrder(words))
words = ["za","zb","ca","cb"]
print(Solution().alienOrder(words))
