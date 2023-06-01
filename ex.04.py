contador = 0

for numero in range(5, 101):

    if numero % 7 == 0 and numero % 5 != 0:

        print(numero, end=" ")
        contador += 1

print("\nQuantidade de números:", contador)
