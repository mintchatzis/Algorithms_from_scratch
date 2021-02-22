from graph import Graph

def bf_search(g,r):
    tmpG = {}
    for vertex in g:
        tmpG[vertex] = 0
    tmpG[r] = 1
    print(tmpG)
    
    queue = [r]
    
    while len(queue) != 0:
            vertex = queue.pop(0)
            print(vertex, "has been searched.")
            
            for pair in g[vertex]:
                if tmpG[pair] != 1:
                    queue.append(pair)
                    tmpG[pair] = 1
                    
def bf_search(graph,item,root = None):
    '''Function implementing breadth-first-search on given graph object'''
    
    graph.init_visited()
    
    def inner_rec(vertex):
        if graph.get_data(vertex) == item:
            return vertex
        graph.set_visited(vertex,True)
        
        return
    
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
    
    g_undir = Graph(init_connections)
    g_dir = Graph(init_connections,directed=True)
    
    i = 0
    for vertex in g_undir.get_vertices():
        g_undir.set_data(vertex,i)
        i += 1
    print(g_undir.get_all_data())
    
    #print(g_undir.graph)
    print(df_search(g_undir,5))           
                
            
    
    
    
