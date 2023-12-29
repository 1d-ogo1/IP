import random


def bissect(f, a, b, tol):
    fa = f(a)
    while b - a > tol:
        m = (a + b) / 2
        fm = f(m)
        if fm == 0:
            return m
        if fm * fa > 0:
            a = m
            fa = fm
        else:
            b = m
    return (a + b) / 2


def binarysearch(seq, valor):
    a = 0
    b = len(seq)-1
    resp = []
    while a <= b:
        m = (b+a) // 2
        if valor == seq[m]:
            y = m - 1
            while valor == seq[m]:
                resp.append(m)
                m += 1
            while valor == seq[y]:
                resp.append(y)
                y -= 1
            return resp
        if valor < seq[m]:
            b = m-1
        else:
            a = m+1
    return resp


def posmax(v, k):
    pmax = k
    for i in range(k+1, len(v)):
        if v[i] > v[pmax]:
            pmax = i
    return pmax


def poxmin(v, k):
    pmin = k
    for i in range(k+1, len(v)):
        if v[i] < v[pmin]:
            pmin = i

    return pmin


def selectionsort(v):   # Procura nos index (n+1 --> len(v)) da lista por um valor maior que v[n] se existir subestitui
    # pelo v[n]
    for k in range(len(v)-1):
        x = posmax(v, k)
        if x != k:
            ant = v[k]
            v[k] = v[x]
            v[x] = ant

    return v


def insertionsort(v):  # Procura no index n+1 se este é maior que o anterior[k] ou menor e assim escolhe a sua posiçã
    # mexendo todos os valores para a direita consuante a posição escolhida
    for k in range(1, len(v), 1):
        if v[k] >= v[0]:
            j = v[0]
            v[0] = v[k]
            for i in range(1, len(v)-1):    # Passar todos os valores de v[i] para v[i+1]
                ant = v[i+1]
                v[i+1] = v[i]
            v[1] = j

    return v


def insertionsorts(a):
    for i in range(1, len(a)-1):
        valor_modificar = a[i]

        while a[i+1] > a[i] and i > 0:
            a[i], a[i+1] = a[i+1], a[i]
            i -= 1

    return a