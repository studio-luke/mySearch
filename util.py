import heapq


class MyData:

    def push(self, item):
        raise NotImplementedError

    def pop(self):
        raise NotImplementedError

    def isEmpty(self):
        raise NotImplementedError


class MyStack(MyData):

    def __init__(self):
        self.list = []

    def push(self, item):
        self.list.append(item)

    def pop(self):
        return self.list.pop()

    def isEmpty(self):
        return len(self.list) == 0

    def __repr__(self):
        return 'MyStack()'


class MyQueue(MyData):

    def __init__(self):
        self.list = []

    def push(self, item):
        self.list.insert(0, item)

    def pop(self):
        return self.list.pop()

    def isEmpty(self):
        return len(self.list) == 0

    def __repr__(self):
        return 'MyQueue()'


class MyPriorityQueue(MyData):

    def __init__(self):
        self.count = 0
        self.heap = []
        """ Q. Is it better to use list with a pair of tuple
        in terms of efficiency, other than dictionary? """

    def push(self, item, priority=0):
        entry = (priority, self.count, item)
        heapq.heappush(self.heap, entry)
        self.count += 1
        # self.heap.append(entry)
        """ What is the difference between append and heappush?
        How does heapq acts? """

    def pop(self):
        _, _, item = heapq.heappop(self.heap)
        return item

    def isEmpty(self):
        return len(self.heap) == 0

    def __repr__(self):
        return 'MyPriorityQueue()'

# some comments!

class MyCounter(dict):

    def __getitem__(self, idx):
        self.setdefault(idx, 0)
        return dict.__getitem__(self, idx)


def MyManhattanDistance(coord1, coord2):
    return abs(coord1[0] - coord2[0]) + abs(coord1[1] - coord2[1])