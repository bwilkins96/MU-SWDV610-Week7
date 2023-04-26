# SWDV 610: Data Structures and Algorithms
# Graph based solution to the missionaries and cannibals problem

class Vertex:
    def __init__(self, element):
        self._element = element

    def element(self):
        return self._element
    
    def __hash__(self):
        return hash(id(self))
    
