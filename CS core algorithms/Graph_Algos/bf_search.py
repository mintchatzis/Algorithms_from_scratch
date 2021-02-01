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
                    
graph = {"a":["b","c"],"b":["a","d","e"],"c":["a","f"],"d":["b","g"],"e":["b","g"],"f":["c","g"],"g":[]}

bf_search(graph,"a")
                    

    
            
                
            
    
    
    
