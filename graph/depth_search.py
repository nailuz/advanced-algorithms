def build_list(order):
    result = []
    for row in range(order):
        result.append([row])
    return result

def print_graph(graph):
    for row in range(len(graph)):
        print(graph[row])

def insert_adj(graph, vertex_a, vertex_b):
    try:
        if graph[vertex_a] and graph[vertex_b]:
            return [graph[vertex_a].append(vertex_b), graph[vertex_b].append(vertex_a)]
    except:
        pass

def vertexes_adj(graph, vertex):
    try:
        result = []
        for row in graph[vertex][1:]:
            result.append(row)
        return result
    except:
        pass
    

def degree_vertex(graph, vertex):
    try:
        return len(graph[vertex])-1
    except:
        pass

def depth_search(graph, vertex):
    aux_visited = build_list(len(graph))
    result = []
    sequence = []
    result.append(vertex)
    sequence.append(vertex)
    while len(sequence):
        adj = [i for i in vertexes_adj(graph, sequence[-1]) if i not in set(vertexes_adj(aux_visited, sequence[-1]))]
        if adj:
            insert_adj(aux_visited, sequence[-1], adj[0])
            aux_visited[sequence[-1]].append(adj[0])
            result.append(adj[0])
            sequence.append(adj[0])
        else:
            del sequence[-1]
    return result

def breadth_search(array, vertex):
    li = [vertex]
    visited = []
    while len(li):
        visited.append(li[0])
        aux = vertexes_adj(array, li.pop(0))
        for i in aux:
            if i not in visited and i not in li:
                li.append(i)
    return visited

#deploy
graph = build_list(15)
insert_adj(graph, 0, 1)
insert_adj(graph, 0, 2)
insert_adj(graph, 1, 3)
insert_adj(graph, 1, 4)
insert_adj(graph, 2, 5)
insert_adj(graph, 2, 6)
insert_adj(graph, 3, 7)
insert_adj(graph, 3, 8)
insert_adj(graph, 4, 9)
insert_adj(graph, 4, 10)
insert_adj(graph, 5, 11)
insert_adj(graph, 5, 12)
insert_adj(graph, 6, 13)
insert_adj(graph, 6, 14)
print_graph(graph)
print(depth_search(graph, 0))
print(breadth_search(graph,0))