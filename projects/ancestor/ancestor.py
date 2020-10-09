
from util import Stack

# The list is given to you as the ancestor list so before going on to the tests 
# I made a mock test of the example
# family = [(1,3), (2,3), (3,6), (5,6), (5, 7), (4,5), (4,8), (8,9), (11, 8), (10,1)]
#     print(earliest_ancestor(family, 6))

# earliest_ancestors =
# {    1: {3},
#      2: {3},
#      3: {6},
#      5: {6, 7},
#      4: {5, 8},
#      8: {9},
#      11: {8},
#      10: {1}
# }

def earliest_ancestor(ancestors, starting_node):
    # making parents vertices/nodes
    vertices = {}
    for i in range(len(ancestors)):
        key = ancestors[i][1]
        value = ancestors[i][0]
        if key in vertices:
            vertices[key].add(value)
        else:
            vertices[key] = set()
            vertices[key].add(value)
    # print('vertices:', vertices)
    visited = set()
    s = Stack()
    s.push(starting_node)
    distance = {}
    distance[starting_node] = 0
    max_dist = 0
    while s.size() > 0:
        # v-child's(6 in the graph) vertex or node
        v = s.pop()
        if v not in visited:
            visited.add(v)
            if v in vertices:
                for parent in vertices[v]:
                    s.push(parent)
                    # calculating distance from child to next vertex or node
                    distance[parent] = distance[v] + 1
                    max_dist = max(max_dist, distance[parent])
                   
    earliest_ancestors = []
    for key, value in distance.items():
        if max_dist > 0 and value == max_dist:
            earliest_ancestors.append(key)
    # print('earliest_ancestors:', earliest_ancestors)
    
    if len(earliest_ancestors):
        return min(earliest_ancestors)
    else:
        return -1
    
    
# do ancestors with bft
# construct a graph and use the function recursively.
