
homemvelho = 0
idadehomemvelho = 0
cmulheresmenos20 = 0

for i in range(1, 9):
    print(f"Digite as informações da pessoa:")
    nome = input("Nome: ")
    idade = int(input("Idade: "))
    sexo = input("Sexo (M/F): ")


    if sexo.upper() == "M" and idade > idadehomemvelho:
        homemvelho = nome
        idadehomemvelho = idade


    if sexo.upper() == "F" and idade < 20:
        cmulheresmenos20 += 1


print(f"\nO homem mais velho é:", homemvelho)
print(f"A quantidade de mulheres com menos de 20 anos é:",cmulheresmenos20)
