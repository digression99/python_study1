ar = [9, 8, 7, 6, 5, 4, 3, 2, 1]

def insertionSort(ar):
    for i in range(1, len(ar)):
        for j in range(i, 0, -1):
            if ar[j] < ar[j - 1]:
                ar[j], ar[j - 1] = ar[j - 1], ar[j]

insertionSort(ar)
#print(ar)

def mergeSort(A, p = 0, r = None):
    if r is None: r = len(A)
    if p < r - 1:
        q = int((p + r) / 2)
        mergeSort(A, p, q)
        mergeSort(A, q, r)
        merge(A, p, q, r)

def merge(A, p, q, r):
    B, i, j = [], p, q

    while True:
        if A[i] <= A[j]:
            B.append(A[i])
            i += 1
        else:
            B.append(A[j])
            j += 1

        if i == q:
            while j < r:
                B.append(A[j])
                j += 1
            break

        if j == r:
            while i < q:
                B.append(A[i])
                i += 1
            break
    A[p:r] = B

import random

# a = [random.randint(0, 100) for k in range(20)]
# print(a)
# mergeSort(a)
# print(a)

print(False == 0)
#print(isinstance(True, int))
