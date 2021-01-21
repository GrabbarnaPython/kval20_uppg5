#allt koden gör är att integrera ihop de olika programmen och dess funktioner. Den hämtar listans värde från List.py. Sedan skjuter den in imformation om nuvarande position till FindPath

import List
import FindPaths

coords = List.makeLists()

for x in range(len(coords)):
    for y in range(len(coords[x])):
        FindPaths.findPaths([x, y])