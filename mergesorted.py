# Welson Kuang, {INSERT NAME}
# CMPE 187 Group MW 14
# 14 March 2026

""" Merging Sorted Arrays: Given two sorted arrays, merge them into a single array. This code aims to highlight Data Flow Testing.
"""

# For stylistic separation of text
def dashes():
    print("-" * 100)

###

# Function for merging two sorted arrays
def merger(A, B):
    C = []

    i = 0
    j = 0
    # Merging...
    while i < len(A) and j < len(B):
        if A[i] <= B[j]:
            C.append(A[i])
            i += 1
        else:
            C.append(B[j])
            j += 1

    # Append the rest!
    while i < len(A):
        C.append(A[i])
        i += 1

    while j < len(B):
        C.append(B[j])
        j += 1

    return C

A = [1,2,7,11]
B = [3,7,13,16,29]
print(merger(A,B))
