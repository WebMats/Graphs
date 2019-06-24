import random

class User:
    def __init__(self, name):
        self.name = name

class SocialGraph:
    def __init__(self):
        self.lastID = 0
        self.users = {}
        self.friendships = {}

    def addFriendship(self, userID, friendID):
        """
        Creates a bi-directional friendship
        """
        if userID == friendID:
            print("WARNING: You cannot be friends with yourself")
        elif friendID in self.friendships[userID] or userID in self.friendships[friendID]:
            print("WARNING: Friendship already exists")
        else:
            self.friendships[userID].add(friendID)
            self.friendships[friendID].add(userID)

    def addUser(self, name):
        """
        Create a new user with a sequential integer ID
        """
        self.lastID += 1  # automatically increment the ID to assign the new user
        self.users[self.lastID] = User(name)
        self.friendships[self.lastID] = set()

    def populateGraph(self, numUsers, avgFriendships):
        """
        Takes a number of users and an average number of friendships
        as arguments

        Creates that number of users and a randomly distributed friendships
        between those users.

        The number of users must be greater than the average number of friendships.
        """
        # Reset graph
        self.lastID = 0
        self.users = {}
        self.friendships = {}
        generated_users = []
        # !!!! IMPLEMENT ME
        for j in range(1, numUsers+1):
            generated_users.append(j)
            self.addUser(j)
        for k in range(len(generated_users)):
            index = random.randint(0, len(generated_users) - 1)
            generated_users[k], generated_users[index] = generated_users[index], generated_users[k]
        for user in generated_users:
            number_of_friends = random.randint(0, avgFriendships * 2)
            for num in range(number_of_friends):
                new_friend = generated_users[random.randint(0, len(generated_users) - 1)]
                while(new_friend == user or new_friend in self.friendships[user]):
                    new_friend = generated_users[random.randint(0, len(generated_users) - 1)]
                self.friendships[user].add(new_friend)

    def getAllSocialPaths(self, userID):
        """
        Takes a user's userID as an argument

        Returns a dictionary containing every user in that user's
        extended network with the shortest friendship path between them.

        The key is the friend's ID and the value is the path.
        """
        visited = {}  # Note that this is a dictionary, not a set
        # !!!! IMPLEMENT ME
        # iterate over users
        for user in self.users:
            target = self.users[user].name
            visited[target] = []
            # do a Breath First Search for nearest path to user from userID
            queue = [[self.users[userID].name]]
            found = False
            while len(queue) > 0 and found == False:
                path = queue.pop()
                v = path[-1]
                if v == target:
                    found = True
                    visited[target] = path
                else:
                    for friend in self.friendships[v]:
                        if friend not in path:
                            queue.insert(0, [*path, friend])
        return visited


if __name__ == '__main__':
    sg = SocialGraph()
    sg.populateGraph(10, 2)
    print(sg.friendships)
    connections = sg.getAllSocialPaths(1)
    print(connections)


