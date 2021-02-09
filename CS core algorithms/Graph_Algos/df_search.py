from graph import Graph

def df_search(graph,item, root = None):
    '''Function implementing depth-first-search on given graph object'''
    
    graph.init_visited()
    
    def inner_rec(vertex):
        if graph.data[vertex] == item:
            return vertex
        
        neighbors = graph[vertex]
        for neighbor in neighbors:
            if not graph.visited[vertex]:
                inner_rec(neighbor)
    
    for node in graph.graph.keys():
        result = inner_rec(node)

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
    
    


            
                
            
    
