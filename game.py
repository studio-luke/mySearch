
import random
import copy
import util

class Directions:
    EAST = 'East'
    WEST = 'West'
    NORTH = 'North'
    SOUTH = 'South'

    def directionToVector(direction):
        if direction == 'East': return (1, 0)
        elif direction == 'West': return (-1, 0)
        elif direction == 'North': return (0, -1)
        else: return (0, 1)


class NumberPuzzle:
    """
    This is a N-square number puzzle game, in which the puzzle frame is square,
    and there're 1 to N^2 - 1 number blocks in the puzzle.
    The size of the puzzle should be N^2, so that means there's one empty space.
    You can move a number block to east, west, north, south,
    if there's an empty space that the number block can be moved.
    The goal is to place every number blocks in the right order, increasing by 1

    For example, 4-square number puzzle is solved when the puzzles are posed like below:
     1   2   3   4
     5   6   7   8
     9  10  11  12
    13  14  15   -      (- : empty space)
    """

    def __init__(self, size):
        """
        To demonstrate this problem, we'll make a two-dimensional list of numbers 0 to N^2 - 1.
        Number 0 means empty space.
        :param size: represents the size of N-square puzzle, in other words, size equals N.
        """
        self.size = size
        self.initialState = list(range(1, size ** 2)) + [0]
        while not self.isSolvable():
            random.shuffle(self.initialState)

        self.initialState = [self.initialState[i*size:(i+1)*size] for i in range(size)]
        # self.size = 4
        # self.initialState = [[ 6,  5,  4,  7],
        #                      [ 9,  1, 11,  2],
        #                      [ 13, 3, 10,  8],
        #                      [14,  0, 15, 12]]

        self. size = 3
        self.initialState = [[6, 4, 7],
                             [8, 5, 0],
                             [3, 2, 1]]

        print(self.getInvCount(self.initialState))
        self.max_num_len = len(str(size**2 - 1))

    def isSolvable(self):
        """
        Note that self.initialState is yet one-dimensional list.
        """
        obj = self.initialState
        assert list not in [type(a) for a in obj]

        if self.isGoal([obj]): return False
        inv_is_odd = self.getInvCount([obj]) % 2
        if self.size % 2:
            return not inv_is_odd
        else:
            blank_row = obj.index(0) // self.size
            blank_is_odd  = blank_row % 2
            return not blank_is_odd ^ inv_is_odd

    def getInvCount(self, numbers):
        order = sum(numbers, [])
        inversion, idx = 0, 1
        for n in order:
            if n == 0: continue
            for m in order[idx:]:
                if m == 0: continue
                if n > m: inversion += 1
            idx += 1
        return inversion

    def getInitialState(self):
        return self.initialState

    def isGoal(self, state):
        goal_state = list(range(1, self.size**2)) + [0]
        # goal_state = [goal_state[i*self.size:(i+1)*self.size] for i in range(self.size)]
        return sum(state, []) == goal_state

    def getSuccessors(self, state):
        empty_pos = sum(state, []).index(0)
        empty_x = empty_pos % self.size
        empty_y = empty_pos // self.size

        successors = []
        for direction in [Directions.EAST, Directions.WEST, Directions.NORTH, Directions.SOUTH]:
            dx, dy = Directions.directionToVector(direction)
            targ_x, targ_y = empty_x - dx, empty_y - dy
            if targ_x in range(self.size) and targ_y in range(self.size):
                action = (state[targ_y][targ_x], direction)
                # next_state = self.getNextState(state, action)
                next_state = copy.deepcopy(state)
                next_state[empty_y][empty_x] = next_state[targ_y][targ_x]
                next_state[targ_y][targ_x] = 0
                cost = 1
                successor = (action, next_state, cost)
                successors.append(successor)
        return successors

    def getNextState(self, state, action):
        targ, direction = action

        targ_pos = sum(state, []).index(targ)
        targ_x = targ_pos % self.size
        targ_y = targ_pos // self.size

        dx, dy = Directions.directionToVector(direction)
        next_x = targ_x + dx
        next_y = targ_y + dy

        next_state = copy.deepcopy(state)
        assert next_state[next_y][next_x] == 0
        next_state[next_y][next_x] = next_state[targ_y][targ_x]
        next_state[targ_y][targ_x] = 0

        return next_state

    def printState(self):
        if self.size > 40:
            print("Too huge to print out!")
            return
        for line in self.initialState:
            for number in line:
                if number == 0:
                    number = ' '
                whitespace = self.max_num_len - len(str(number))
                print(' '*whitespace + str(number), end='  ')
            print()


def nullHeuristic(problem, state):
    return 1


def matchedHeuristic(problem, state):
    order = sum(state, [])
    ans_order = [a for a in range(1, problem.size ** 2)] + [0]

    value = 0
    for i in range(problem.size):
        if order[i] == ans_order[i]: continue
        if order[i] == 0: continue
        value += 1
    return value


def distanceHeuristic(problem, state):
    order = sum(state, [])
    ans_order = [a for a in range(1, problem.size ** 2)] + [0]

    value = 0
    for i in range(problem.size):
        if order[i] == ans_order[i]: continue
        if order[i] == 0: continue
        j = ans_order.index(order[i])

        ix, iy = i % problem.size, i // problem.size
        jx, jy = j % problem.size, j // problem.size

        value += util.MyManhattanDistance((ix, iy), (jx, jy))
    return value






