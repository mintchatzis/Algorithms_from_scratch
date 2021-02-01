def get_edges(g):
    edges = []
    
    for key in g.keys():
        for v in g[key]:
            rev = (v,key)
            if rev not in edges:
                edges.append((key,v))
    return edges

graph = {
    "a":["b","c"],
    "b":["a","d","e"],
    "c":["a","f"],
    "d":["b","g"],
    "e":["b","g"],
    "f":["c","g"],
    "g":[]}

edges = get_edges(graph)
print(edges)