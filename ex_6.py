import heapq


def dijkstra_algorithm(
        start: str, end: str,
        graph: dict[str: list[tuple[str, int]]]
) -> int:
    """
        Find the shortest path distance between two cities using Dijkstra's algorithm.

        Args:
            start: Starting city name
            end: Destination city name
            graph: Dictionary mapping city names to lists of (neighbor, weight) tuples

        Returns:
            Shortest distance from start to end city

        Note:
            Assumes the graph is connected and a path exists between start and end.
        """
    dist = {start: 0}
    queue = [(0, start)]

    while queue:
        current_dist, name = heapq.heappop(queue)
        if name == end:
            return dist[end]

        for neighbor, weight in graph.get(name):
            new_dist = current_dist + weight
            if neighbor not in dist or new_dist < dist[neighbor]:
                dist[neighbor] = new_dist
                heapq.heappush(queue, (new_dist, neighbor))


if __name__ == "__main__":
    n = int(input("Enter count of cities: "))
    m = int(input("Enter count of roads: "))

    graph = {}
    for _ in range(m):
        A, B, weight = input().split()
        weight = int(weight)

        graph.setdefault(A, []).append((B, weight))
        graph.setdefault(B, []).append((A, weight))

    start, end = input().split()
    print(dijkstra_algorithm(start, end, graph))
