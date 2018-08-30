# -*- encoding: utf-8 -*-

def build_array(order):
    array = []
    for row in range(1, order +1):
        array.append([row])
    return array

def print_array(graph):
    for row in graph:
        print(row)

def insert_edge(graph, vertex_a, vertex_b):
    try:
        graph[vertex_a-1].append(vertex_b)
        graph[vertex_b-1].append(vertex_a)
        return graph
    except:
        return graph
    

def vertexes_adjacent(graph, vertex):
    try:
        aux = []
        for row in range(1, len(graph[vertex-1])):
            aux.append(graph[vertex-1][row])
        return aux
    except:
        return 'List index out of range'

def check_edges_between(graph, vertex_a, vertex_b):
    result = False
    for row in graph[vertex_a - 1]:
        if row == vertex_b:
            result = True
    return result

def degree_vertex(graph, vertex):
    try:
        return len(graph[vertex - 1])
    except:
        return 'List index out of range'

    
def breadth_search(array, vertex):
    li = [vertex]
    visited = []
    while len(li):
        visited.append(li[0])
        aux = vertexes_adjacent(array, li.pop(0))
        for i in aux:
            if i not in visited and i not in li:
                li.append(i)
    return visited
        
    
            
            


x = build_array(7)
print_array(x)
x = insert_edge(x, 1, 2)
x = insert_edge(x, 1, 3)
x = insert_edge(x, 1, 5)
x = insert_edge(x, 2, 4)
x = insert_edge(x, 3, 4)
x = insert_edge(x, 7, 5)
x = insert_edge(x, 3, 6)
print_array(x)
x = insert_edge(x, 2, 3)
print(vertexes_adjacent(x, 3))
print_array(x)
print(check_edges_between(x, 3 , 1))
print(degree_vertex(x, 2))
print(breadth_search(x,7))