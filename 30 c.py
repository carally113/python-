A = int(input())
B = int(input())
C = int(input())
V = int(input())
D = int(input())
Q = int(input())
if A > B and A > C and A > V and A > D and A > Q:
    print(A)
elif B > A and B > C and B > V and B > D and B > Q:
    print(B)
else:
    print(C)
if V > A and V > B and V > C and V > D and V > Q:
    print(V)
elif D > A and D > B and D > C and D > V and D > Q:
    print(D)
else:
    print(Q)
if A < B and A < C and A < V and A < D and A < Q:
    print(A)
elif B < A and B < C and B < V and B < D and B < Q:
    print(B)
else:
    print(C)
if V < A and V < B and V < C and V < D and V < Q:
    print(V)
elif D < A and D < B and D < C and D < V and D < Q:
    print(D)
else:
    print(Q)