import random


class Node:
    def __init__(self, a, b, z):
        self.x = a
        self.y = b
        self.depth = z


class DFS:
    def __init__(self):
        self.directions = 4
        self.x_move = [1, -1, 0, 0]
        self.y_move = [0, 0, 1, -1]
        self.found = False
        self.N = 0
        self.source = None
        self.goal = None
        self.goal_level = 999999
        self.state = 0
        self.topo_order = []

    def generate_grid(self):
        self.N = random.randint(4, 7)
        grid = [[1 for _ in range(self.N)] for _ in range(self.N)]


        self.source = Node(random.randint(0, self.N - 1), random.randint(0, self.N - 1), 0)
        self.goal = Node(random.randint(0, self.N - 1), random.randint(0, self.N - 1), self.goal_level)

        while self.source.x == self.goal.x and self.source.y == self.goal.y:
            self.goal = Node(random.randint(0, self.N - 1), random.randint(0, self.N - 1), self.goal_level)

        return grid

    def print_grid(self, grid):
        print("Grid:")
        for row in grid:
            print(" ".join(map(str, row)))
        print(f"Source: ({self.source.x}, {self.source.y})")
        print(f"Goal: ({self.goal.x}, {self.goal.y})")

    def print_direction(self, m, x, y):
        if m == 0:
            print("Moving Down ({}, {})".format(x, y))
        elif m == 1:
            print("Moving Up ({}, {})".format(x, y))
        elif m == 2:
            print("Moving Right ({}, {})".format(x, y))
        else:
            print("Moving Left ({}, {})".format(x, y))

    def st_dfs(self, grid, u):
        grid[u.x][u.y] = 0
        self.topo_order.append((u.x, u.y))

        for j in range(self.directions):
            v_x = u.x + self.x_move[j]
            v_y = u.y + self.y_move[j]
            if (0 <= v_x < self.N) and (0 <= v_y < self.N) and grid[v_x][v_y] == 1:
                v_depth = u.depth + 1
                self.print_direction(j, v_x, v_y)
                if v_x == self.goal.x and v_y == self.goal.y:
                    self.found = True
                    self.goal.depth = v_depth
                    self.topo_order.append((v_x, v_y))
                    return
                child = Node(v_x, v_y, v_depth)
                self.st_dfs(grid, child)
                if self.found:
                    return

    def init(self):
        grid = self.generate_grid()
        self.print_grid(grid)
        self.st_dfs(grid, self.source)

        if self.found:
            print("Goal found")
            print("Number of moves required =", self.goal.depth)
            print("Topological order of node traversal:", self.topo_order)
        else:
            print("Goal cannot be reached from the starting block")


def main():
    d = DFS()
    d.init()


if __name__ == "__main__":
    main()