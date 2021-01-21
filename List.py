def makeLists():
    x = int(input("Antal rader? "))
    y = int(input("Antal kolumner? "))
    coords=[]
    for i in range(x):
        coords.append([])
        print("vad ska rad",i+1,"vara. Skriv med mellanslag")
        ap = input()
        split = ap.split()
        ma = map(int, split)
        d2=list(ma)
        for l in range(y):
            coords[i].append([])
            coords[i][l].append(d2[l])
            coords[i][l].append(0)
            coords[i][l].append(0)
    for z in range(len(coords)):
        print(coords[z])

    return coords
