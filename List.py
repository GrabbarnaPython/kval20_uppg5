rad = int(input("Antal rader? "))
kol = int(input("Antal kolumner? "))
d1=[]
for i in range(rad):
    d1.append([])
    print("vad ska rad",i+1,"vara. Skriv med mellanslag")
    ap = input()
    split = ap.split()
    ma = map(int, split)
    d2=list(ma)
    for l in range(kol):
        d1[i].append(d2[l])
for z in range(len(d1)):
    print(d1[z])
    print(d1[0][0])