def CP(A, B):
    if len(A) != len(B):
        raise ValueError("A and B must be the ssame lenght!")
    
    P_A = 0
    for i in A:
        if i == 1:
            P_A += 1

    P_AB = 0
    for i in range(len(A)):
        if A[i] ==1 and  B[i] ==1:
            P_AB += 1

    if P_A == 0:
        return 0
    else:
        return P_AB/P_A
    




A = list(map(int, input("Enter list A separated with spaces: ").split()))
B = list(map(int, input("Enter list B separated with spaces: ").split()))
print(CP(A,B))