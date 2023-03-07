import math

def suite(A, B, N):
    u0 = A
    u1 = B
    dictio = {0: u0, 1: u1}
    n = 0
    while n != N:
        u0 = (u0 + u1) / 2.0
        u1 = 2 / (1/u0 + 1/u1)
        n += 1
        dictio[n] = u0
    return dictio

def exercice2():
    while True:
        A = float(input("Rentrer A > "))
        B = float(input("Rentrez B > "))
        N = int(input("Rentrez N > "))
        if not N > 0:
            print("N doit être une entier tel que N > 0")
        elif not A > 0:
            print("A doit être une entier tel que N > 0")
        elif not B > 0:
            print("B doit être une entier tel que N > 0")
        else:
            dictio = suite(A, B, N)
            break       
    i = len(dictio) - 1             
    print("A=", A, " B=", B, " N=", N, " => suite = (", dictio[i], ", ", dictio[i-1], ")")

