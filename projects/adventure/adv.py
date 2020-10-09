from room import Room
from player import Player
from world import World

import random
from ast import literal_eval

class Queue():
    def __init__(self):
        self.queue = []
    def enqueue(self, value):
        self.queue.append(value)
    def dequeue(self):
        if self.size() > 0:
            return self.queue.pop(0)
        else:
            return None
    def size(self):
        return len(self.queue)

class Stack():
    def __init__(self):
        self.stack = []
    def push(self, value):
        self.stack.append(value)
    def pop(self):
        if self.size() > 0:
            return self.stack.pop()
        else:
            return None
    def size(self):
        return len(self.stack)
    def top(self):
        return self.stack[-1]

# Load world
world = World()


# You may uncomment the smaller graphs for development and testing purposes.
# map_file = "maps/test_line.txt"
# map_file = "maps/test_cross.txt"
# map_file = "maps/test_loop.txt"
# map_file = "maps/test_loop_fork.txt"
# map_file = "maps/test_line.txt"
# shortest is 2
# map_file = "maps/test_cross.txt"
# shortest is 14
# map_file = "maps/test_loop.txt"
# shortest is 14
# map_file = "maps/test_loop_fork.txt"
# shortest is 24
# map_file = "maps/main_maze.txt"
# shortest is 918
map_file = "maps/main_maze.txt"

# Loads the map into a dictionary
room_graph=literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)

# Print an ASCII map
world.print_rooms()

player = Player(world.starting_room)

# You may find the commands `player.current_room.id`, `player.current_room.get_exits()` and `player.travel(direction)` useful.
# Fill this out with directions to walk
# {
#   0: {'n': '?', 's': 5, 'w': '?', 'e': '?'},
#   5: {'n': 0, 's': '?', 'e': '?'}
# } 
# 500 entries (0-499) 
# `len(traversal_path) <= 2000`
# `len(traversal_path) < 960`

# traversal_path = ['n', 'n']


def get_reverse(dir):
    d = {
        'n': 's',
        's': 'n',
        'e': 'w',
        'w': 'e'
    }
    return d[dir]


traversal_path = []
visited_rooms = set()
s = Stack()
s.push([player.current_room, None])

# import pdb
# pdb.set_trace()
while s.size() > 0:
    v, exit = s.top()
    if v.id not in visited_rooms:
        visited_rooms.add(v.id)
    v_is_complete = True
    exits = v.get_exits()
    # random.shuffle(exits)
    for exit in exits:
        neighbor = v.get_room_in_direction(exit)  
        if neighbor.id not in visited_rooms:
            s.push([neighbor, exit])  
            traversal_path.append(exit)
            v_is_complete = False
            break
    if len(visited_rooms) == len(room_graph):
        break
    if v_is_complete:
        room, dir = s.pop()
        if dir:
            traversal_path.append(get_reverse(dir))

# print('traversal_path:', traversal_path)
# TRAVERSAL TEST
visited_rooms = set()
player.current_room = world.starting_room
visited_rooms.add(player.current_room)
for move in traversal_path:
    player.travel(move)
    visited_rooms.add(player.current_room)

if len(visited_rooms) == len(room_graph):
    print(f"TESTS PASSED: {len(traversal_path)} moves, {len(visited_rooms)} rooms visited")
else:
    print("TESTS FAILED: INCOMPLETE TRAVERSAL")
    print(f"{len(room_graph) - len(visited_rooms)} unvisited rooms")



#######
# UNCOMMENT TO WALK AROUND
#######
player.current_room.print_room_description(player)
while True:
    cmds = input("-> ").lower().split(" ")
    if cmds[0] in ["n", "s", "e", "w"]:
        player.travel(cmds[0], True)
    elif cmds[0] == "q":
        break
    else:
        print("I did not understand that command.")
