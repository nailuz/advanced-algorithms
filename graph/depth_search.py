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
    initial = vertex
    result.append(vertex)
    sequence.append(vertex)
    adj = vertexes_adj(graph, sequence[-1])
    while True:
        if not sequence:
            print('quebrei')
            break
        adj = vertexes_adj(graph, sequence[-1])
        if adj[0] in graph[vertex][1:] and adj[0] not in aux_visited[vertex][1:]:
            aux_visited[vertex].append(adj[0])
            sequence.append(adj[0])
            result.append(adj[0])
            vertex = adj[0]
        else:
            del sequence[-1]
    return result



#deploy
graph = build_list(9)
insert_adj(graph, 0, 1)
insert_adj(graph, 1, 2)
insert_adj(graph, 2, 3)
insert_adj(graph, 2, 6)
insert_adj(graph, 2, 4)
insert_adj(graph, 6, 8)
insert_adj(graph, 4, 5)
insert_adj(graph, 5, 7)
print_graph(graph)
print(depth_search(graph, 0))
