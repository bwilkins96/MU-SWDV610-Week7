# SWDV 610: Data Structures and Algorithms
# Graph based solution to the missionaries and cannibals problem

from graph import Graph

# (M, C, B)

def valid_combo(tup):
    return tup[0] >= tup[1]

def valid_move(tup1, tup2):
    if tup1[0] == tup2[0] and tup1[1] == tup2[1]:
        return False
    
    if tup1[2] == tup2[2]:
        return False

    return True

def build_mc_graph():
    mc_graph = Graph()

    # Generate possible vertices
    for side in ['l', 'r']:
        for num_miss in [1, 2, 3]:
            for num_cann in [1, 2, 3]:
                possible = (num_miss, num_cann, side)

                if valid_combo(possible):
                    mc_graph.insert_vertex(possible)

    # Generate possible edges
    vertices = mc_graph.vertices()
    for vert in vertices:
        for other in vertices:
            if not mc_graph.get_edge(vert, other):
                if valid_move(vert.element(), other.element()):
                    mc_graph.insert_edge(vert, other)

    return mc_graph

def main():
    mc_graph = build_mc_graph()
    start_pos = mc_graph.get_vertex((3, 3, 'r'))

    #print(mc_graph.vertices())
    #print()
    print(len(mc_graph.edges()))

if __name__ == '__main__': main()