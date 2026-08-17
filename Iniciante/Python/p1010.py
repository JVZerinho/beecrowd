# Lê a primeira linha inteira e separa os três valores
numP, qnt, val = input().split()

# Converte os valores separados para os tipos matemáticos corretos
numP = int(numP)
qnt = int(qnt)
val = float(val)

# Lê a segunda linha inteira e separa os três valores
numP2, qnt2, val2 = input().split()

# Converte os valores da segunda peça
numP2 = int(numP2)
qnt2 = int(qnt2)
val2 = float(val2)

total = (qnt * val) + (qnt2 * val2)
print(f"VALOR A PAGAR: R$ {total:.2f}")
