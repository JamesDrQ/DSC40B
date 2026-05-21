def biggest_descendent(graph, root, value):
    biggest = {}
    def dfs(node):
        best = value[node]

        for child in graph.neighbors(node):
            child_best = dfs(child)
            best = max(best, child_best)
        
        biggest[node] = best
        return best
    dfs(root)
    return biggest
