# SWDV 610: Data Structures and Algorithms
# Graph class

class Graph:
    class Vertex:
        def __init__(self, element):
            self._element = element

        def element(self):
            return self._element
        
        def __hash__(self):
            return hash(id(self))
    
    class Edge:
        def __init__(self, origin, dest, ele=None):
            self._origin = origin
            self._destination = dest
            self._element = ele
        
        def endpoints(self):
            return (self._origin, self._destination)
        
        def opposite(self, origin):
            if origin is self._origin:
                return self._destination
            return self._origin
    
    def __init__(self, directed=False):
        self._outgoing = {}
        self._incoming = {} if directed else self._outgoing

    def is_directed(self):
        return self._incoming is not self._outgoing
    
    def vertex_count(self):
        return len(self._outgoing)
    
    def vertices(self):
        return self._outgoing.keys()
    
    def edge_count(self):
        total = 0
        for v in self._outgoing:
            total += len(self._outgoing[v])

        return total if self.is_directed() else total // 2
    
    def edges(self):
        result = set()
        for map in self._outgoing.values():
            result.update(map.values())

        return result
    
    def get_edge(self, origin, dest):
        return self._outgoing[origin].get(dest)
    
    def degree(self, vert, outgoing=True):
        edges = self._outgoing if outgoing else self._incoming
        return len(edges[vert])
    
    def incident_edges(self, vert, outgoing=True):
        edges = self._outgoing if outgoing else self._incoming

        for e in edges[vert].values():
            yield e

    def insert_vertex(self, ele):
        vert = self.Vertex(ele)

        if self.is_directed(): self._incoming[vert] = {}
        self._outgoing[vert] = {}

    def insert_edge(self, origin, dest, ele=None):
        edge = self.Edge(origin, dest, ele)

        self._outgoing[origin][dest] = edge
        self._incoming[dest][origin] = edge