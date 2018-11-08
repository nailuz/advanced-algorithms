# -*- coding: utf-8 -*-
import string

def gerarGrafo(ordem = 5):
    aux = {}
    for row in range(ordem):
        aux[string.ascii_uppercase[row]] = []
    return aux

def criarArestas(grafo, vertice_out, vertice_in):
    if (vertice_out in grafo) and (vertice_in in grafo):
        grafo[vertice_out].append(vertice_in)
        return grafo

def verticesAdjacentes(grafo , vertice):
    if vertice in grafo:
        aux = []
        for row in grafo[vertice]:
            aux.append(row)
        return aux

def caminhoMinimo(grafo, vertice_inicial):
    copy = grafo
    graph_aux = gerarGrafo(len(grafo))
    graph_aux[vertice_inicial].append(0)
    lista = [vertice_inicial]
    visitado = []
    contador = 1
    ajudante = 0
    while(len(lista)):
        visitado.append(lista[0])
        aux = verticesAdjacentes(copy, lista.pop(0))
        tamanho = len(aux)
        for row in aux:
            if row not in visitado and row not in lista:
                lista.append(row)
                graph_aux[row].append(contador)
            tamanho -= 1
        contador += 1
    print(graph_aux)

# 0 1 2 3 4 5 6
# A B C D E F G 
# CODIGO
graph = gerarGrafo(7)
print('Gerar primeiro grafico')
print(graph)
graph = criarArestas(graph, 'A', 'B')
graph = criarArestas(graph, 'A', 'D')
graph = criarArestas(graph, 'B', 'D')
graph = criarArestas(graph, 'B', 'E')
graph = criarArestas(graph, 'C', 'A')
graph = criarArestas(graph, 'C', 'F')
graph = criarArestas(graph, 'D', 'C')
graph = criarArestas(graph, 'D', 'E')
graph = criarArestas(graph, 'D', 'F')
graph = criarArestas(graph, 'D', 'G')
graph = criarArestas(graph, 'E', 'G')
graph = criarArestas(graph, 'G', 'F')
print('\nAdicionando as areastas')
print(graph)
print('\nCaminho minimo')
caminhoMinimo(graph, 'C')