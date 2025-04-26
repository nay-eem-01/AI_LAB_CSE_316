import random


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.cluster = None


class KMeans:
    def __init__(self, points_count, clusters_count, grid_size=30):
        self.points_count = points_count
        self.clusters_count = clusters_count
        self.grid_size = grid_size
        self.mat = [[0 for _ in range(grid_size)] for _ in range(grid_size)]
        self.points = []
        self.clusters = []
        self.start()

    def start(self):
        self.points = [Point(random.randint(0, self.grid_size - 1), random.randint(0, self.grid_size - 1)) for _ in
                       range(self.points_count)]
        self.clusters = [Point(random.randint(0, self.grid_size - 1), random.randint(0, self.grid_size - 1)) for _ in
                         range(self.clusters_count)]

        while True:
            for p in self.points:
                min_dist = float('inf')
                for idx, c in enumerate(self.clusters):
                    dist = abs(p.x - c.x) + abs(p.y - c.y)
                    if dist < min_dist:
                        min_dist = dist
                        p.cluster = idx

            old_centers = [(c.x, c.y) for c in self.clusters]
            for i in range(self.clusters_count):
                members = [p for p in self.points if p.cluster == i]
                if members:
                    avg_x = sum(p.x for p in members) // len(members)
                    avg_y = sum(p.y for p in members) // len(members)
                    self.clusters[i].x = avg_x
                    self.clusters[i].y = avg_y

            new_centers = [(c.x, c.y) for c in self.clusters]
            if old_centers == new_centers:
                break

        for p in self.points:
            self.mat[p.y][p.x] = 1
        for c in self.clusters:
            self.mat[c.y][c.x] = 2

        self.print_grid()

    def print_grid(self):
        size_y = len(self.mat)
        size_x = len(self.mat[0])

        print("\nClustered Data Visualization (P = Point, C = Cluster Center):\n")
        for y in reversed(range(size_y)):
            print(f"{y:2d} | ", end="")
            for x in range(size_x):
                if self.mat[y][x] == 0:
                    print(".", end=" ")
                elif self.mat[y][x] == 1:
                    print("P", end=" ")
                elif self.mat[y][x] == 2:
                    print("C", end=" ")
            print()

        print("    ", end="")
        for x in range(size_x):
            print(f"{x % 10}", end=" ")
        print()


def main():
    points = 100
    clusters = 10
    kmeans = KMeans(points, clusters)


if __name__ == "__main__":
    main()
