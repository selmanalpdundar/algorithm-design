import random

def perm(A):    # it can proved that it generates one of the n! perms uniformly at random
    n = len( A)
    for i in range(n):
        p = random.randint(i, n-1)
        tmp = A[p]
        A[p] = A[i]
        A[i] = tmp

def headphone( A ):
    perm(A) # randomization
    n = len(A)
    best = 0
    for i in range(n): # i = 0, 1, ..., n-1
        if A[i] > A[best]:
            print("*"),  # buy a new headphone
            best = i
    print
    return best

def main():
    A = [1, 2, 3, 4, 5, 6, 7, 8] 
    print(A)
    i = headphone( A )
    print(A)
    print("A[i] =", A[i], ", i =", i)

main()
