def assign_good_and_evil(graph):
    labels = {}
    for start in graph.nodes:
        if start not in labels:
            labels[start] = 'good'
            stack = [start]
            while stack:
                node = stack.pop()
                for neighbor in graph.neighbors(node):
                    opposite = 'evil' if labels[node] == 'good' else 'good'

                    if neighbor not in labels:
                        labels[neighbor] = opposite
                        stack.append(neighbor)
                    elif labels[neighbor] != opposite:
                        return None
    return labels