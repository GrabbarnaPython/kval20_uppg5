x = int(input("Antal rader? "))
y = int(input("Antal kolumner? "))
cord=[]
for i in range(x):
    cord.append([])
    print("vad ska rad",i+1,"vara. Skriv med mellanslag")
    ap = input()
    split = ap.split()
    ma = map(int, split)
    d2=list(ma)
    for l in range(y):
        cord[i].append([])
        cord[i][l].append(d2[l])
        cord[i][l].append(0)
        cord[i][l].append(0)
for z in range(len(cord)):
    print(cord[z])
