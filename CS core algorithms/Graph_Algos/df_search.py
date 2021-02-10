from graph import Graph

def df_search(graph,item, root = None):
    '''Function implementing depth-first-search on given graph object'''
    
    graph.init_visited()
    
    def inner_rec(vertex):
        if graph.get_data(vertex) == item:
            return vertex
        graph.set_visited(vertex,True)
        
        neighbors = graph.get_neighbors(vertex)
        for neighbor_ver in neighbors:
            if not graph.get_visited(neighbor_ver):
                inner_rec(neighbor_ver)
        return None     #no more neighbors to explore
    
    for vertex in graph.get_vertices():
        result = inner_rec(vertex)
        if result is not None:
            return result
    return None


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
    
    i = 0
    for vertex in g_undir.get_vertices():
        g_undir.set_data(vertex,i)
        i += 1
    print(g_undir.get_all_data())
        
    
    #print(g_undir.graph)
    print(df_search(g_undir,5))
    
    
    


            
                
            
    
 