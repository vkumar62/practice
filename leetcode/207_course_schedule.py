from collections import defaultdict
import pdb
class Solution:
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        
        def topo_sort(graph, node, visited, seen):
            if node in visited:
                return False
            
            seen.add(node)

            if node not in graph:
                return True
            
            for v in graph[node]:
                if v in seen:
                    return False
                elif v not in visited:
                    order = topo_sort(graph, v, visited, seen)
                    if not order:
                        return False
            
            visited.add(node)
            return True
            
        
        pdb.set_trace()
        # Form the graph
        graph = defaultdict(set)
        for u,v in prerequisites:
            graph[u].add(v)
            # Check for u/v >= numCourses ?
            
        #Topologically sort the graph
        visited = set()
        for u in graph.keys():
            if u not in visited:
                order = topo_sort(graph, u, visited, set())
                if not order:
                    return False
        return True

prereq = [[1,0],[2,0],[3,1],[3,2]]
prereq = [[0,1],[0,2],[1,2]]
print(Solution().canFinish(2, prereq))
