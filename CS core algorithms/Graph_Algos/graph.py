class Graph():
    '''Graph representation using dictionary of sets
        connections: list of tuples, eg. ('a','b'), meaning nodes a and b are linked
        directed: if True, graph is directed
    '''

    def __init__(self, connections = None, directed = False):
        self.__graph = {}
        self.__directed = directed
        self.__visited = self.init_visited()  #keeps track of 'visited' status of each node
        self.__data = self.__init_data()
        
        #construct graph from given connections
        if connections is not None:
            for pair in connections:
                self.add(pair)
                
    def __init_vertex(self,vertex):
        self.__graph[vertex] = set()
        self.__data[vertex] = None
        self.__visited[vertex] = False
        
    def add(self,pair):
        '''
           Adds connection to graph.
           Comp: O(1)
        '''
        node1,node2 = pair
        
        #Create nodes, if they don't already exist
        if node1 not in self.__graph:
            self.__init_vertex(node1)
        if node2 not in self.__graph:
            self.__init_vertex(node2)
          
        #Add one-way connection between nodes
        self.__graph[node1].add(node2)
            
        #for undirected graph, add reverse connection too
        if (not self.__directed):
            self.__graph[node2].add(node1)
        return
        
    def init_visited(self):
        '''
           Returns a dictionary which stores the 'visited status' of every node
           Comp: O(n)
        '''
        temp = {}
        for key in self.__graph.keys():
            temp[key] = False
        return temp

    def __init_data(self):
        '''
            Returns a dictionary representing the data stored in each graph node
            all initialized to None
            Comp: O(n)
        '''
        temp = {}
        for key in self.__graph.keys():
            temp[key] = None
        return temp
    
    def get_neighbors(self,vertex):
        return self.__graph[vertex]
    
    def get_all_data(self):
        return self.__data
    
    def get_data(self,vertex):
        return self.__data[vertex]
    
    def get_vertices(self):
        return self.__graph.keys()
    
    def get_graph_rep(self):
        return self.__graph
    
    def get_visited(self,vertex):
        '''
            Returns true if given vertex has been visited
        '''
        return self.__visited[vertex]
    
    def get_size(self):
        return len(self.__graph)
    
    def set_visited(self,vertex,visited):
        self.__visited[vertex] = visited
        return
    
    def set_data(self,vertex,value):
        self.__data[vertex] = value
        return
    
    def is_empty(self):
        return self.__graph == {}

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
    print(f"Your undirected graph, sir: \n {g_undir.get_graph_rep()}")
    print(f"Your directed graph, sir: \n {g_dir.get_graph_rep()}")
    
    
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
