# SWDV 610: Data Structures and Algorithms
# Graph based solution to the missionaries and cannibals problem

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