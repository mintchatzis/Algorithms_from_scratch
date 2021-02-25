from graph import Graph
                    
def bf_search(graph,item,root = None):
    '''
        Function implementing breadth-first-search on given
        graph object using a queue (FIFO)
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
    
    graph.init_visited()
    
    def inner_rec(q):
        #stopping condition
        if len(q) == 0:
            return None
        
        #pop next queue item and check it
        vertex = q.pop(0)
        if graph.get_visited(vertex):
            return None
        print(f"Visiting vertex: {vertex}")
        if graph.get_data(vertex) == item:
            return vertex
        graph.set_visited(vertex,True)

        #get all vertices connected to the one just explored
        neighbors = graph.get_neighbors(vertex)
        for neighbor_ver in neighbors:
            if not graph.get_visited(neighbor_ver):
                q.append(neighbor_ver)
        
        #call recursive function with new queue and thread result back to caller
        res = inner_rec(q)
        if res is not None:
            return res
        return None
        
    return inner_rec([root])
                    
                    
if __name__ == "__main__":
    
    init_connections = [ ('a', 'c'), ('a', 'b'),
                         ('b', 'd'),('b', 'e'),
                         ('c', 'f'),
                         ('d', 'g'),
                         ('e', 'g'),
                         ('f', 'g') ]
    
    g_undir = Graph(init_connections)
    g_dir = Graph(init_connections,directed=True)
    
    i = 0
    for vertex in g_undir.get_vertices():
        g_undir.set_data(vertex,i)
        i += 1
    print(g_undir.get_all_data())
    
    #print(g_undir.graph)
    print(bf_search(g_undir,6))         
                
            
    
    
    
