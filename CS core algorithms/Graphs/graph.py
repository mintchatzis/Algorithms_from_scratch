graph = {
    "a" : ["c"],
    "b" : ["c", "e"],
    "c" : ["a", "b", "d", "e"],
    "d" : ["c"],
    "e" : ["c", "b"],
    "f" : [] }

def gen_edges(graph):
    edges = []
    
    for vertice in graph:
        for pair in graph[vertice]:
            edges.append((vertice,pair))
    return edges


edge_list = gen_edges(graph)
    