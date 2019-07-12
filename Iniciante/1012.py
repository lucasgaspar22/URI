line = input().split(" ")
a = float(line[0])
b = float(line[1])
c = float(line[2])

aTriangle = a*c/2
aCircle = 3.14159*c**2
aTrape = (a+b)*c/2
aSquare = b**2 
aRectangle = a*b

print("TRIANGULO: %.3f" %aTriangle)
print("CIRCULO: %.3f" %aCircle)
print("TRAPEZIO: %.3f" %aTrape)
print("QUADRADO: %.3f" %aSquare)
print("RETANGULO: %.3f" %aRectangle)
