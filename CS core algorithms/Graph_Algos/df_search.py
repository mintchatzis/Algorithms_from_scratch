from graph import Graph

def df_search(graph,root,item):
    '''
        Function implementing depth-first-search on given graph object
        Inputs:
            - graph: graph object of class Graph
            - root: vertex to start search from, 'None' will perform search from first vertex found
            - item: item to search the graph for
        Returns: Vertex containing item OR 'None' if item not found
    '''
    
    if graph.is_empty():
        return None
    if root is None:
        root = next(iter(graph.get_vertices())) #set root to first vertex found
    if root not in graph.get_vertices():
        return None
        
    graph.init_visited() #set all vertices to unvisited
    
    def inner_rec(vertex):
        if graph.get_data(vertex) == item:
            return vertex
        graph.set_visited(vertex,True)
        print(f"Visiting vertex: {vertex}")
        
        neighbors = graph.get_neighbors(vertex)
        for neighbor_ver in neighbors:
            if not graph.get_visited(neighbor_ver):
                result = inner_rec(neighbor_ver)
                if result is not None:
                    return result
        return None     #no more neighbors to explore
    
    return inner_rec(root)


if __name__ == "__main__":
    
    init_connections = [ ('a', 'c'), ('a', 'b'),
                         ('b', 'd'),('b', 'e'),
                         ('c', 'f'),
                         ('d', 'g'),
                         ('e', 'g'),
                         ('f', 'g'),
                         ]
    
    g_undir = Graph(init_connections)
    #print(g_undir.get_graph_rep())
    g_dir = Graph(init_connections,directed=True)
    
    i = 0
    for vertex in g_undir.get_vertices():
        g_undir.set_data(vertex,i)
        i += 1
    print(g_undir.get_all_data())
        
    
    #print(g_undir.graph)
    print(df_search(g_undir,'x',5))
    
    
    


            
                
            
    
 