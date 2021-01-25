import random
def makeLists():
    y = int(input("Antal rader? "))
    x = int(input("Antal kolumner? "))
    coords=[]
    for i in range(y):
        coords.append([])
        print("vad ska rad",i+1,"vara. Skriv med mellanslag")
        ap = input()
        split = ap.split()
        ma = map(int, split)
        d2=list(ma)
        for l in range(x):
            coords[i].append([])
            coords[i][l].append(d2[l])
            coords[i][l].append(0)
            coords[i][l].append(0)
    for z in range(len(coords)):
        print(coords[z])

    return coords
def randomlist():
    y = int(input("Antal rader? "))
    x = int(input("Antal kolumner? "))
    coords=[]
    for i in range(y):
        coords.append([])
        print("vad ska rad",i+1,"vara. Skriv med mellanslag")
        ap = input()
        split = ap.split()
        ma = map(int, split)
        d2=list(ma)
        for l in range(x):
            coords[i].append([])
            coords[i][l].append(d2[l])
            coords[i][l].append(0)
            coords[i][l].append(0)
    for z in range(len(coords)):
        print(coords[z])

    return coords