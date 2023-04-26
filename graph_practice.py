# SWDV 610: Data Structures and Algorithms
# Graph practice

from collections import defaultdict

def add_edge(graph, u, v):
    graph[u].append(v)

def generate_edges(graph):
    edges = []

    for node in graph:
        for neighbour in graph[node]:
            edges.append((node, neighbour))

    return edges

def find_shortest_path(graph, start, end, path=[]):
    path = path + [start]
    if start == end: return path
    
    shortest = None
    for node in graph[start]:
        if node not in path:
            new_path = find_shortest_path(graph, node, end, path)

        if new_path:
            if not shortest or len(new_path) < len(shortest):
                shortest = new_path
        return shortest


def main():
    graph = defaultdict(list)
    todo = [('a','c'), ('b','c'), ('b','e'), ('c','d'), ('c','e'), 
            ('c','a'), ('c','b'), ('e','b'), ('d','c'), ('e','c')]
    
    for pair in todo:
        add_edge(graph, pair[0], pair[1])

    print(generate_edges(graph))
    print(graph)

    graph2 = {'a':['c'], 'b':['d'], 'c':['e'], 'd':['a', 'd'], 'e':['b','c']}
    print('\n', find_shortest_path(graph2, 'd', 'c'))

if __name__ == '__main__': main()