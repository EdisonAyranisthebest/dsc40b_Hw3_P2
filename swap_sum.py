def swap_sum(A, B):
 
    SA = sum(A)
    SB = sum(B)

    D = SB - SA - 10
    if D % 2 != 0:
        return None  

    t = D // 2  

    i, j = 0, 0
    n, m = len(A), len(B)

    while i < n and j < m:
        diff = B[j] - A[i]
        if diff == t:
            return (i, j)
        if diff < t:
            j += 1  
        else:
            i += 1  

    return None
