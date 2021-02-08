from graph import Graph

def df_search(graph,item, root = None):
    '''Function implementing depth-first-search on given graph object'''
    
    graph.init_visited()
    
    for node in graph.graph.keys():
        
    
    


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
    
    


            
                
            
    
    
    

