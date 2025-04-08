class IDDFS:
    def __init__(self, grid, start, goal):
        self.grid = grid
        self.start = start
        self.goal = goal
        self.rows = len(grid)
        self.cols = len(grid[0])
        self.max_depth = 0
        self.goal_found = False
        self.path = []

    def is_valid(self, x, y, visited):
        return (
            0 <= x < self.rows and
            0 <= y < self.cols and
            self.grid[x][y] == 0 and
            (x, y) not in visited
        )

    def depth_limited_search(self, current, depth, visited):
        x, y = current
        if not self.is_valid(x, y, visited):
            return False

        visited.add((x, y))
        self.path.append((x, y))

        if current == self.goal:
            self.goal_found = True
            return True

        if depth >= self.max_depth:
            self.path.pop()
            visited.remove((x, y))
            return False


        for dx, dy in [(-1,0), (1,0), (0,-1), (0,1)]:
            next_x, next_y = x + dx, y + dy
            if self.depth_limited_search((next_x, next_y), depth + 1, visited):
                return True


        self.path.pop()
        visited.remove((x, y))
        return False

    def iterative_deepening(self):
        MAX_DEPTH_LIMIT = self.rows * self.cols

        while not self.goal_found and self.max_depth <= MAX_DEPTH_LIMIT:
            self.path = []
            visited = set()
            if self.depth_limited_search(self.start, 0, visited):
                print(f"Path found at depth {self.max_depth} using IDDFS")
                print("Traversal Order:", self.path)
                return
            self.max_depth += 1

        if not self.goal_found:
            print(f"Path not found at max depth {MAX_DEPTH_LIMIT} using IDDFS")


if __name__ == "__main__":
    # Sample Input
    try:
        rows, cols = map(int, input().strip().split())
        grid = []
        for _ in range(rows):
            grid.append(list(map(int, input().strip().split())))

        start_input = input().strip().split()
        start = (int(start_input[1]), int(start_input[2]))

        goal_input = input().strip().split()
        goal = (int(goal_input[1]), int(goal_input[2]))

        iddfs = IDDFS(grid, start, goal)
        iddfs.iterative_deepening()
    except Exception as e:
        print("Error:", e)
        print("Please provide correct input format.")
