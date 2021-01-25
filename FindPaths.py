def lookAround(x, y, i, lista, coords): #sparar paths        
    lista.append(coords[x][y])

    if i == 1:
        return lookAround(x, y + 1, i + 1, lista, coords)
    elif i == 2:
        return lookAround(x + 1, y, i + 1, lista, coords)
    elif i == 3:
        return lookAround(x, y - 1, i + 1, lista, coords)
    elif i == 4:
        return lookAround(x, y - 1, i + 1, lista, coords)
    elif i == 5:
        return lookAround(x - 1, y, i + 1, lista, coords)
    elif i == 6:
        return lookAround(x - 1, y, i + 1, lista, coords)
    elif i == 7:
        return lookAround(x, y + 1, i + 1, lista, coords)
    elif i == 8:
        return lookAround(x, y + 1, i + 1, lista, coords)
    else:
        return lista

        