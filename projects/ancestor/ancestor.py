
from util import Stack

# The list is given to you as the ancestor list so before going on to the tests 
# I made a mock test of the example
# family = [(1,3), (2,3), (3,6), (5,6), (5, 7), (4,5), (4,8), (8,9), (11, 8), (10,1)]
#     print(earliest_ancestor(family, 6))

def earliest_ancestor(ancestors, starting_node):
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
        v = s.pop()
        # path = s.pop()
        # v = path[-1]
        if v not in visited:
            visited.add(v)
            if v in vertices:
                for parent in vertices[v]:
                    s.push(parent)
                    distance[parent] = distance[v] + 1
                    max_dist = max(max_dist, distance[parent])
                    # if max_dist == distance[parent]:

    # print(distance, 'max_dist:', max_dist)
    earliest_ancestors = []
    for key, value in distance.items():
        if max_dist > 0 and value == max_dist:
            earliest_ancestors.append(key)
    # print('earliest_ancestors:', earliest_ancestors)
    
    if len(earliest_ancestors):
        return min(earliest_ancestors)
    else:
        return -1
    
