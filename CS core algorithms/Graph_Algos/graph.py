class Graph():
    def __init__(self, connections = None, directed = False):
        '''Graph representation using dictionary of sets'''
        
        self.graph = {} 
        self.data = {}
        self.directed = directed
        
        if connections is not None:
            for pair in connections:
                self.add(pair)
        
        self.visited = self.init_visited()  #keeps track of 'visited' status of each node
    
    def add(self,pair):
        '''
           Adds connection to graph.
           Comp: O(1)
        '''
        node1,node2 = pair
        
        if node1 not in self.graph:
            self.graph[node1] = set()
        self.graph[node1].add(node2)
        
        #for undirected graph, add reverse connection too
        if (not self.directed):
            if node2 not in self.graph:
                self.graph[node2] = set()
            self.graph[node2].add(node1)
        return
        
    def init_visited(self):
        '''
           Returns a dictionary which stores the 'visited status' of every node
           Comp: O(n)
        '''
        temp = {}
        for key in self.graph.keys():
            temp[key] = False
        return temp        


if __name__ == "__main__":
    
    init_connections = [ ('a', 'c'), ('a', 'b'),
                         ('b', 'd'),('b', 'e'),
                         ('c', 'f'),
                         ('d', 'g'),
                         ('e', 'g'),
                         ('f', 'g') ]
    
    extra_connections = [('g','h'),
                         ('h','f')]
    
    g_undir = Graph(init_connections)
    g_dir = Graph(init_connections,directed=True)
    print(f"Your undirected graph, sir: \n {g_undir.graph}")
    print(f"Your directed graph, sir: \n {g_dir.graph}")
    
    
    tests = []
    
    #Graph initialization with 0 arguments
    def test1():
        pass
    tests.append(test1)
    
    #Graph initialization with given edges, directed = False
    def test2():
        g_undir = Graph(init_connections)
        
        expected = {
            "a":{"b","c"},
            "b":{"a","d","e"},
            "c":{"a","f"},
            "d":{"b","g"},
            "e":{"b","g"},
            "f":{"c","g"},
            "g":{"d","e","f"} }
        
        assert g_undir.graph == expected
        
    #tests.append(test2)
    
    ##Graph initialization with given edges, directed = True
    def test3():
        pass
    tests.append(test3)
    
    def run_tests():
        for test in tests:
            test()
        print(f"All {len(tests)} tests passed.")
    #run_tests()

"""
STORAGE
_______
def get_edges(g):
    '''returns edges of a graph'''
    edges = []
    
    for key in g.keys():
        for v in g[key]:
            rev = (v,key)
            if rev not in edges:
                edges.append((key,v))
    return edges

edges = get_edges(undir_graph)
print(edges)

undir_graph = {
    "a":{"b","c"},
    "b":{"a","d","e"},
    "c":{"a","f"},
    "d":{"b","g"},
    "e":{"b","g"},
    "f":{"c","g"},
    "g":{"d","e","f"}}
    
dir_graph = {
    "a":{"b","c"},
    "b":{"d","e"},
    "c":{"f"},
    "d":{"g"},
    "e":{"g"},
    "f":{"g"},
    "g":set()}
"""
