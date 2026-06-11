def slc(graph, d, k):

    parent = {}

    def find(x):
        if parent[x] != x:
            parent[x] = find(parent[x])
        return parent[x]

    def union(x, y):
        root_x = find(x)
        root_y = find(y)

        if root_x != root_y:
            parent[root_y] = root_x
            return True

        return False

    for node in graph.nodes:
        parent[node] = node

    num_clusters = len(graph.nodes)

    edges = sorted(graph.edges, key=d)

    for edge in edges:
        if num_clusters == k:
            break

        u, v = edge

        if union(u, v):
            num_clusters -= 1

    clusters = {}

    for node in graph.nodes:
        root = find(node)

        if root not in clusters:
            clusters[root] = set()

        clusters[root].add(node)

    return frozenset(frozenset(cluster) for cluster in clusters.values())