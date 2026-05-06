def mode(numbers):
    if len(numbers) == 0:
        return None
    
    counts = {}
    for num in numbers:
        if num not in counts:
            counts[num] = 1
        else:
            counts[num] += 1
    
    max_count = 0
    mode = 0
    for num in counts:
        if counts[num] > max_count:
            max_count = counts[num]
            mode = num
    return mode