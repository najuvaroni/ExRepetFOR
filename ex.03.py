mulher = 0
homem = 0
grupo = 0
idadem = 0
idadeh = 0
idadeg = 0

for n in range(1,11):
    print(f"Digite as informações da pessoa:")
    sexo = input('Informe o genero: \nfeminino \nmasculino ')
    idade = int(input("Informe a idade: "))
    idadeg += idade

    if sexo == "feminino":
        mulher += 1
        idadem += idade
    elif sexo == "masculino":
        homem += 1
        idadeh += idade

mediam = idadem / mulher
mediah = idadeh / homem
mediag = idadeg / 10
print("Média da idade das mulheres: ", mediam, 'média idade dos homens: ', mediah,'média geral: ',mediag)
