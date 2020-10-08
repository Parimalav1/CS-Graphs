import random
import math


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


class User:
    def __init__(self, name):
        self.name = name


class SocialGraph:
    def __init__(self):
        self.last_id = 0
        self.users = {}
        self.friendships = {}

    def add_friendship(self, user_id, friend_id):
        """
        Creates a bi-directional friendship
        """
        if user_id == friend_id:
            print("WARNING: You cannot be friends with yourself")
        elif friend_id in self.friendships[user_id] or user_id in self.friendships[friend_id]:
            print("WARNING: Friendship already exists")
        else:
            self.friendships[user_id].add(friend_id)
            self.friendships[friend_id].add(user_id)

    def add_user(self, name):
        """
        Create a new user with a sequential integer ID
        """
        self.last_id += 1  # automatically increment the ID to assign the new user
        self.users[self.last_id] = User(name)
        self.friendships[self.last_id] = set()

    # {1: {8, 10, 5}, 2: {10, 5, 7}, 3: {4}, 4: {9, 3}, 5: {8, 1, 2}, 6: {10}, 7: {2}, 8: {1, 5}, 9: {4}, 10: {1, 2, 6}}
    # >>> sg = SocialGraph()
    # >>> sg.populate_graph(10, 2)
    # >>> print(sg.friendships)
    # {1: {8}, 2: set(), 3: {6}, 4: {9, 5, 7}, 5: {9, 10, 4, 6}, 6: {8, 3, 5}, 7: {4}, 8: {1, 6}, 9: {10, 4, 5}, 10: {9, 5}}

    # Note that in the above example, the average number of friendships is exactly 2 but the actual number of friends per user ranges anywhere from 0 to 4.

    # * Hint 1: To create N random friendships, you could create a list with all possible friendship combinations, shuffle the list, 
    # then grab the first N elements from the list. You will need to `import random` to get shuffle.
    # * Hint 2: `add_friendship(1, 2)` is the same as `add_friendship(2, 1)`. You should avoid calling one after the other since it will do nothing but print a warning. 
    # You can avoid this by only creating friendships where user1 < user2.

    def populate_graph(self, num_users, avg_friendships):
        """
        Takes a number of users and an average number of friendships
        as arguments

        Creates that number of users and a randomly distributed friendships
        between those users.

        The number of users must be greater than the average number of friendships.
        """
        # Reset graph
        # !!!! IMPLEMENT ME
        # self.last_id = 0
        # self.users = {}
        # self.friendships = {}
        # # Add users
        # for i in range(0, num_users):
        #     self.add_user(f"User {i}")
        # # Create friendships
        # possible_friendships = []
        # for user_id in self.users:
        #     for friend_id in range(user_id + 1, self.last_id + 1):
        #         possible_friendships.append((user_id, friend_id))
        # random.shuffle(possible_friendships)
        # # x = 0
        # for i in range(0, math.floor(num_users * avg_friendships / 2)):
        #     friendship = possible_friendships[i]
        #     self.add_friendship(friendship[0], friendship[1])

        self.last_id = 0
        self.users = {}
        self.friendships = {}
        # Add users
        for i in range(0, num_users):
            self.add_user(f"User {i}")
        # Create friendships
        for user_id in self.users:
            if user_id == num_users:
                break
            for i in range(math.floor(avg_friendships/2)):
                x = random.randint(user_id + 1, num_users)
                self.add_friendship(user_id, x)

    # {1: {8, 10, 5}, 2: {10, 5, 7}, 3: {4}, 4: {9, 3}, 5: {8, 1, 2}, 6: {10}, 7: {2}, 8: {1, 5}, 9: {4}, 10: {1, 2, 6}}
    # >>> connections = sg.get_all_social_paths(1)
    # >>> print(connections)
    # {1: [1], 8: [1, 8], 10: [1, 10], 5: [1, 5], 2: [1, 10, 2], 6: [1, 10, 6], 7: [1, 10, 2, 7]}
    # Note that in this sample, Users 3, 4 and 9 are not in User 1's extended social network.

    # * Hint 1: What kind of graph search guarantees you a shortest path?
    # * Hint 2: Instead of using a `set` to mark users as visited, you could use a `dictionary`. 
    # Similar to sets, checking if something is in a dictionary runs in O(1) time. 
    # If the visited user is the key, what would the value be?

    def get_all_social_paths(self, user_id):
        """
        Takes a user's user_id as an argument

        Returns a dictionary containing every user in that user's
        extended network with the shortest friendship path between them.

        The key is the friend's ID and the value is the path.
        """
        visited = {}  # Note that this is a dictionary, not a set
        # !!!! IMPLEMENT ME
        paths = {}
        q = Queue()
        q.enqueue([user_id])
        while q.size() > 0:
            path = q.dequeue()
            v = path[-1]
            if v not in visited:
                paths[v] = path
                visited[v] = True
                for friend in self.friendships[v]:
                    friendship_path = path + [friend]
                    q.enqueue(friendship_path)

        return paths


if __name__ == '__main__':
    sg = SocialGraph()
    sg.populate_graph(10, 2)
    print(sg.friendships)
    connections = sg.get_all_social_paths(1)
    print(connections)
