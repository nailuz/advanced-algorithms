# -*- coding: utf-8 -*-
import string

class graph():
    def __init__(self, order = 5):
        self.graph = {}
        for row in range(order):
            self.graph[string.ascii_uppercase[row]] = []
    
    def _add_(self, vertex_in, vertex_out, value = 1):
        if vertex_in in self.graph and vertex_out in self.graph:
            self.graph[vertex_in].append({vertex_out: value})

meugrafp = graph()
print(meugrafp.graph)
print(meugrafp.graph)
meugrafp._add_('A', 'B', 5)
print(meugrafp.graph)
