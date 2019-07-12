line = input().split(" ")
a = float(line[0])
b = float(line[1])
c = float(line[2])

greaterAB = (a+b + abs(a-b))/2
greaterBC = (b+c + abs(b-c))/2
greaterABC = (greaterAB + greaterBC + abs(greaterAB-greaterBC))/2
print("%d eh o maior" %greaterABC)
