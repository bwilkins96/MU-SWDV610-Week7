# SWDV 610: Data Structures and Algorithms
# Graph based solution to the missionaries and cannibals problem

from graph import Graph

# (M, C, B)

def valid_combo(tup):
    return (tup[0] >= tup[1]) or (tup[0] == 0)

def valid_move(tup1, tup2):
    if tup1[2] == tup2[2]:
        return False
    
    total = tup1[0] + tup1[1] + tup2[0] + tup2[1]
    if total != 7 and total != 8:
        return False

    return True

def build_mc_graph():
    mc_graph = Graph()

    # Generate possible vertices
    for side in ['l', 'r']:
        for num_miss in [0, 1, 2, 3]:
            for num_cann in [0, 1, 2, 3]:
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
    end_pos = mc_graph.get_vertex((3, 3, 'l'))

    print()
    print(mc_graph.vertices())
    print('len:', len(mc_graph.vertices()))
    print()
    print(mc_graph.edges())
    print('len', len(mc_graph.edges()))
    print()

    shortest = mc_graph.get_shortest_path(start_pos, end_pos)
    print(shortest)

if __name__ == '__main__': main()