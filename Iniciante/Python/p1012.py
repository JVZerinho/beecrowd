a, b, c = input().split()
a = float(a)
b = float(b)
c = float(c)

pi = 3.14159

areaT = (a * c) / 2
areaC = pi * (c ** 2)
areaTr = ((a + b) * c) / 2
areaQ = b ** 2
areaR = a * b

print(f"TRIANGULO: {areaT:.3f}")
print(f"CIRCULO: {areaC:.3f}")
print(f"TRAPEZIO: {areaTr:.3f}")
print(f"QUADRADO: {areaQ:.3f}")
print(f"RETANGULO: {areaR:.3f}")
