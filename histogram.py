def histogram(points, bins):
    n = len(points)
    densities = []
    i = 0

    for a, b in bins:
        count = 0
        
        while i < n and points[i] < a:
            i += 1
        
        while i < n and points[i] < b:
            count += 1
            i += 1
        
        width = b - a
        densities.append(count / (n * width))
    
    return densities