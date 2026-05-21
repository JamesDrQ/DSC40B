def cluster(graph, weights, level):
    visited = set()
    clusters = []

    for node in graph.nodes:
        if node not in visited:
            current_cluster = set()

            stack = [node]
            visited.add(node)

            while stack:
                curr = stack.pop()
                current_cluster.add(curr)

                for neighbor in graph.neighbors(curr):
                    if neighbor not in visited and weights(curr, neighbor) >= level:
                        visited.add(neighbor)
                        stack.append(neighbor)

            clusters.append(frozenset(current_cluster))

    return frozenset(clusters)