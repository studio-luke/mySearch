
import util
import game

def testFunc():
    """
    This function is designed to test 'My own util.py functions'.
    """
    pass


def BreathFirstSearch(problem):
    visited = set()
    fringe = util.MyQueue()
    fringe.push( (problem.getInitialState(), []) )

    iteration = 0
    while not fringe.isEmpty():
        state, plan = fringe.pop()
        if problem.isGoal(state): return plan
        if tuple(sum(state,[])) not in visited:
            visited.add(tuple(sum(state, [])))
            for successor in problem.getSuccessors(state):
                action, next_state, _ = successor
                new_plan = plan + [action]
                fringe.push( (next_state, new_plan) )

        iteration += 1
        if not iteration % 20000:
            print(iteration, "nodes expanded.")
    else:
        return None


def AstarSearch(problem):
    visited = set()
    fringe = util.MyPriorityQueue()
    # heuristic = game.matchedHeuristic
    heuristic = game.distanceHeuristic

    ini_state = problem.getInitialState()
    fringe.push( (ini_state, 0, []), heuristic(problem, ini_state) )

    iteration = 0
    while not fringe.isEmpty():
        state, cost, plan = fringe.pop()
        if problem.isGoal(state):
            print(iteration, "nodes expanded.")
            return plan
        if tuple(sum(state,[])) not in visited:
            visited.add(tuple(sum(state, [])))
            for successor in problem.getSuccessors(state):
                action, next_state, next_cost = successor
                new_plan = plan + [action]
                new_cost = cost + next_cost
                fringe.push( (next_state, new_cost, new_plan),
                             new_cost + heuristic(problem, next_state) )

        iteration += 1
        if not iteration % 20000:
            print(iteration, "nodes expanded.")

    else:
        return None


if __name__ == '__main__':
    # sol_len_max = float("-inf")
    # for i in range(100):
    #     problem = game.NumberPuzzle(3)
    #     print()
    #     problem.printState()
    #     sol = AstarSearch(problem)
    #     print(sol)
    #     if sol_len_max < len(sol):
    #         print("New Record! Solution", len(sol), "actions long.")
    #         sol_len_max = len(sol)
    #         longest_problem = problem.getInitialState()
    #
    # print("Maximum Solution Length: ", sol_len_max)
    # print(longest_problem)

    problem = game.NumberPuzzle(3)
    problem.printState()
    sol = AstarSearch(problem)
    print(sol)