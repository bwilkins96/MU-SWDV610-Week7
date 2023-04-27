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
        
        def __repr__(self):
            return '< ' + str(self.element()) + ' >'
    
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
        
        def __repr__(self):
            return '(' + str(self._origin) + ' --> ' + str(self._destination) + ')'
    
    def __init__(self, directed=False):
        self._outgoing = {}
        self._incoming = {} if directed else self._outgoing

    def is_directed(self):
        return self._incoming is not self._outgoing
    
    def vertex_count(self):
        return len(self._outgoing)
    
    def vertices(self):
        return self._outgoing.keys()
    
    def get_vertex(self, ele):
        for vert in self._outgoing:
            if vert.element() == ele:
                return vert
        
        return None
    
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

        return vert

    def insert_edge(self, origin, dest, ele=None):
        edge = self.Edge(origin, dest, ele)

        self._outgoing[origin][dest] = edge
        self._incoming[dest][origin] = edge

        return edge

    def BFS(self, start_vert, visited):
        level = [start_vert]
        while len(level) > 0:
            next_level = []

            for vert in level:
                for edge in self.incident_edges(vert):
                    other_vert = edge.opposite(vert)

                    if other_vert not in visited:
                        visited[other_vert] = edge 
                        next_level.append(other_vert)
            
            level = next_level

    def BFS2(self, start_vert, visited=None):
        if visited == None:
            visited = {start_vert: None}

        level = [start_vert]
        while len(level) > 0:
            next_level = []

            for vert in level:
                yield vert
                
                for edge in self.incident_edges(vert):
                    other_vert = edge.opposite(vert)

                    if other_vert not in visited:
                        visited[other_vert] = edge
                        next_level.append(other_vert)
            
            level = next_level


if __name__ == '__main__':
    test = Graph()

    a = test.insert_vertex('a')
    b = test.insert_vertex('b')
    c = test.insert_vertex('c')
    d = test.insert_vertex('d')
    e = test.insert_vertex('e')
    f = test.insert_vertex('f')
    g = test.insert_vertex('g')
    h = test.insert_vertex('h')
    i = test.insert_vertex('i')

    edge_points = [(a,b), (a,d), (a,e), (b,c), (b,e), (e,d),
                   (d,g), (d,h), (c,f), (f,h), (g,h), (h,i)]
    
    for points in edge_points:
        test.insert_edge(points[0], points[1])

    visited = {a: None}
    test.BFS(a, visited)
    
    #for vert in test.BFS2(a, visited):
    #    print(vert.element())

    print(visited)


