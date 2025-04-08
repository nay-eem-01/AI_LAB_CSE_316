class GraphColoring:
    def __init__(self, no_of_colors, graph):
        self.graph = graph
        self.no_of_colors = no_of_colors
        self.V = len(graph)
        self.colors = [0] * self.V

    def solve(self, v=0):
        if v == self.V:
            return True

        for c in range(1, self.no_of_colors + 1):
            if self.is_possible(v, c):
                self.colors[v] = c
                if self.solve(v + 1):
                    return True
                self.colors[v] = 0  # Backtracking

        return False

    def is_possible(self, v, c):
        for i in range(self.V):
            if self.graph[v][i] == 1 and self.colors[i] == c:
                return False
        return True

    def graph_coloring(self):
        if self.solve():
            print(f"Coloring Possible with {self.no_of_colors} Colors")
            print("Color Assignment:", self.colors)
        else:
            print(f"Coloring Not Possible with {self.no_of_colors} Colors")


if __name__ == "__main__":
    try:
        N, M, K = map(int, input().strip().split())

        graph = [[0 for _ in range(N)] for _ in range(N)]

        for _ in range(M):
            u, v = map(int, input().strip().split())
            graph[u][v] = 1
            graph[v][u] = 1

        gc = GraphColoring(K, graph)
        gc.graph_coloring()

    except Exception as e:
        print("Error:", e)
        print("Please check the input format.")
