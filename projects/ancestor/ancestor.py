class Ancestor:
    def __init__(self):
        self.vertices = {}
    
    def add_dataset(self, dataset):
        for data in dataset:
            if data[0] not in self.vertices:
                self.vertices[data[0]] = set()
            self.vertices[data[0]].add(data[1])
    
    def earliest_ancestor(self, id):
        stack = [[vertex] for vertex in self.vertices if id in self.vertices[vertex]]
        traversing = True
        visited = set()
        while (traversing):
            traversing = False
            for i in range(len(stack)):
                path = stack[i]
                v = path[-1]
                if v not in visited:
                    visited.add(v)
                    for vertex in self.vertices:
                        if v in self.vertices[vertex]:
                            traversing = True
                            stack.append([*path, vertex])
        highest_generation = 0
        for i in range(len(stack)):
            if len(stack[i]) > highest_generation:
                highest_generation = len(stack[i])
        stack = [path for path in stack if len(path) == highest_generation]
        if len(stack) == 0:
            return -1
        elif len(stack) > 1:
            cur_path = stack[0]
            smallest_index = cur_path[-1]
            for i in range(1, len(stack)):
                if stack[i][-1] < smallest_index:
                    cur_path = stack[i]
                    smallest_index = stack[i][0]
            return cur_path
        else:
            return stack[0]


dataset = [(2, 3), (1, 3), (3, 6), (5, 6), (5, 7), (4, 5), (4, 8), (8, 9), (11, 8), (10, 1)]

ancestor = Ancestor()
ancestor.add_dataset(dataset)
print(ancestor.earliest_ancestor(6))




