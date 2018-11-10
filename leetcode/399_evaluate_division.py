class Node:
    def __init__(self, var):
        self.var = var
        self.children = {}


class Solution:
    def calcEquation(self, equations, values, queries):
        """
        :type equations: List[List[str]]
        :type values: List[float]
        :type queries: List[List[str]]
        :rtype: List[float]
        """
        
        nodes = dict()
        
        # Form the graph
        for equation, value in zip(equations, values):
            src, dest = equation
            if src not in nodes:
                nodes[src] = Node(src)
            if dest not in nodes:
                nodes[dest] = Node(dest)
            
            src_node = nodes[src]
            dest_node = nodes[dest]
            src_node.children[dest_node] = value
            dest_node.children[src_node] = 1.0/value
            
        result = []
        
        # Now go through the queries one by one and calculate the product of the edges
        for query in queries:
            src, dest = query
            if src not in nodes or dest not in nodes:
                result.append(-1.0)
            else:
                result.append(self.get_quotient(nodes[src], nodes[dest], set()))
        return result
    
    def get_quotient(self, node, target_node, visited):
        
        if not node:
            return -1.0
        if node == target_node:
            return 1.0
        if node in visited:
            return -1.0

        visited.add(node)
        for child, val in node.children.items():
            res = self.get_quotient(child, target_node, visited)
            if res != -1.0:
                # Target is found here
                return val * res
        return -1.0
       
equations = [["x1","x2"],["x2","x3"],["x3","x4"],["x4","x5"]]
values = [3.0,4.0,5.0,6.0]
queries = [["x1","x5"],["x5","x2"],["x2","x4"],["x2","x2"],["x2","x9"],["x9","x9"]] 

print(Solution().calcEquation(equations, values, queries))
