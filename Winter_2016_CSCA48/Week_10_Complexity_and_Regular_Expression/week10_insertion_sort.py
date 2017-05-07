def insertion_sort(L):
    for i in range(1, len(L)):                   # 5 steps
        current_val = L[i]                      # 3 steps
        j = i                                   # 2 steps
        while(j > 0 and L[j-1] > current_val):  # 8 steps
            L[j] = L[j-1]                       # 5 steps
            j = j -1                            # 3 steps
        L[j] = current_val                      # 3 steps
        
        # worst case analysis
        # steps 5-8 may happen up to n times (8 + 5 + 3 + 3) * n = 19n
        # steps 1-3 + 5-8 may happen up to n times (5 + 3 + 2 + 19n) * n = 10n + 19n^2
        # T(n) = 19n^2 + 10n
        
if(__name__ == "__main__"):
    L = [5, 7, 1, 9, 3, 2, 0, 4, 6, 8]
    insertion_sort(L)
    print(L2)