cliente = int(input('Digite a quantidade de clientes: '))
soma = 0
for z in range(1, cliente+1):
    z = float(input("Informe a temperatura: "))
    soma += z
    if z <= 37.2:
       print("Está normal")

    elif 37.3 >= z <= 38:
      print("Estado febril")

    elif z > 38 and z <= 39:
      print("Com febre")

    else:
     print("Febre alta")

media = soma / cliente
print('A média das temperaturas é: ', media, ' e a quantidade de clientes é', cliente)
