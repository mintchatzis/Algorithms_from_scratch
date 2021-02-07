def df_search(graph,root=None,item):
    '''Function implementing depth-first-search on input dictionary representing graph'''
    
    if root == None:
        root = graph.keys[0]
    
    
    tmpG = {}
    for vertex in graph:
        tmpG[vertex] = 0
    
    def inner(g,s):
        tmpG[s] = 1
        
        for pair in g[s]:
            if tmpG[pair] != 1:
                

    
graph = {"a":["b","c"],"b":["a","d","e"],"c":["a","f"],"d":["b","g"],"e":["b","g"],"f":["c","g"],"g":[]}
graph_values = {"a":1 , "b":2, "c":3, "d":4, "e":5, "f":6, "g":7}
    
    
        
print(df_search(graph,'a',7))


            
                
            
    
    
    

