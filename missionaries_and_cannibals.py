# SWDV 610: Data Structures and Algorithms
# Graph based solution to the missionaries and cannibals problem
# River bank status is stored in tuple form: (num_missionaries, num_cannibals, bank_side)

from graph import Graph

def get_opposite(tup):
    side = 'l' if tup[2] == 'r' else 'r'
    return (3-tup[0], 3-tup[1], side)

def get_change(tup_before, tup_after):
    miss_change = abs(tup_after[0] - tup_before[0])
    cann_change = abs(tup_after[1] - tup_before[1])
    return miss_change + cann_change

def valid_combo(tup):
    return (tup[0] >= tup[1]) or (tup[0] == 0)

def valid_move(tup1_before, tup2_after):
    if tup1_before[2] == tup2_after[2]:
        return False
    
    total = tup1_before[0] + tup1_before[1] + tup2_after[0] + tup2_after[1]
    if total != 7 and total != 8:
        return False
    
    tup2_before = get_opposite(tup1_before)
    tup1_after = get_opposite(tup2_after)

    if not valid_combo(tup2_before) or not valid_combo(tup1_after):
        return False
    
    total_change = get_change(tup1_before, tup1_after)
    if total_change <= 0 or total_change > 2:
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

    # print()
    # print(mc_graph.vertices())
    # print('len:', len(mc_graph.vertices()))
    # print()
    # print(mc_graph.edges())
    # print('len', len(mc_graph.edges()))
    # print()

    shortest = mc_graph.get_shortest_path(start_pos, end_pos)
    print(shortest)

if __name__ == '__main__': main()