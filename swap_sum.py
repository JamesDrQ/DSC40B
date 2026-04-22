def swap_sum(A, B):
    sum_A = sum(A)
    sum_B = sum(B)
    diff = sum_A - sum_B + 10
    if diff % 2 != 0:
        return None
    target = diff // 2
    i = 0
    j = 0
    while i < len(A) and j < len(B):
        current = A[i] - B[j]
        if current == target:
            return (i, j)
        elif current < target:
            i += 1
        else:
            j += 1
    
    return None
