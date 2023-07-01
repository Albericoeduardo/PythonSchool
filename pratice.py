#1
'''number1 = float(input("Digite um número: "))
number2 = float(input("Digite outro número: "))
if number1 > number2:
    print(f'O primeiro número digitado({number1}) é maior')
else:
    print(f'O segundo número({number2}) é maior')'''

#2
'''number3 = float(input("Digite um número: "))
if number3 > 0:
    print('Número positivo')
else: 
    print('Número negativo')'''

#3
'''letra = str(input("Digite F ou M: "))
if letra.lower() == 'f':
    print(f'A letra digitada é {letra.upper()}')
elif letra.lower() == 'm':
    print(f'A letra digitada é {letra.upper()}')
else:
    print(f'Digite F ou M')'''

#4
'''vogalConsoante = str(input('Digite uma letra: '))
if vogalConsoante.lower() == 'a' or vogalConsoante.lower() == 'e' or vogalConsoante.lower() == 'i' or vogalConsoante.lower() == 'o' or vogalConsoante.lower() == 'u':
    print('Vogal')
else:
    print('Consoante')'''

#5
'''nota1 = float(input("Digite a 1° nota: "))
nota2 = float(input("Digite a 2° nota: "))
media = (nota1 + nota2) /2
if media == 10:
    print(f'Aprovado com distinção, media = {media}')
elif media >= 7:
    print(f'Aprovado, sua média é = {media}')
else:
    print(f'Reprovado, sua média é = {media}')'''

#6
'''numbers = []
for i in range(3):
    number4 = float(input(f'Digite o {i+1}° número: '))
    numbers.append(number4)

print(f'O maior número é {max(numbers)}')
print(f'O menor número é {min(numbers)}')'''

#7
'''productPrices = []
for i in range(3):
    prices = float(input(f'Digite o {i+1}° preço: '))
    productPrices.append(prices)

print(f'O produto que voce deve comprar é o mais barato, no caso o que custa: {min(productPrices)}')'''

#8
'''numbers2 = []
for i in range(3):
    number5 = float(input(f'Digite o {i+1}° número: '))
    numbers2.append(number5)
numbers2.sort(reverse=True)

for j in numbers2:
    print(j)'''

#9
'''turno = str(input("Qual turno voce estuda? (M, V ou N) "))
if turno.lower() == 'm':
    print('Bom dia!')
elif turno.lower() == 'v':
    print('Boa tarde!')
elif turno.lower() == 'n':
    print('Boa noite!')
else:
    print('Valor inválido!')'''

#12
'''name = input("Digite seu nome de usuário: ")
password = input("Digite sua senha: ")
while True:
    if name == password:
        print("ERRO! Usuário e senha iguais")
        name = input("Digite seu nome novamente: ")
        password = input("Digite sua senha novamente: ")
    else:
        print("Cadastro Realizado!")
        print(f'Seja bem vindo, {name}!')
        break'''

#13 e 14
'''countryA = float(input("Digite a TAMANHO DA POPULAÇÃO do Páis A: "))
countryB = float(input("Digite a TAMANHO DA POPULAÇÃO do Páis B: "))
growthRateA = float(input("Digite a TAXA DE CRESCIMENTO do Páis A: "))
growthRateB = float(input("Digite a TAXA DE CRESCIMENTO do Páis B: "))
anos = 0
while countryA <= countryB:
    countryA *= growthRateA
    countryB *= growthRateB
    anos += 1

print(countryA)
print(countryB)
print(f'A população do País A atingirá ou ultrapassará o tamanho do Páis B em {anos} anos')'''

#15
'''num = 20
for i in range(1, num+1):
    print(i, end=" ")'''

#16
'''number = 0
i = 0
while i < 5:
    numbers = float(input(f'Digite o {i+1}° número: '))
    i += 1
    if numbers > number:
        number = numbers
print(number)'''

#17
'''number = 0
i = 0
while i < 5:
    numbers = float(input(f'Digite o {i +1}° número: '))
    number += numbers
    i += 1

media = number/i

print(f'A soma dos números é: {number} e a média é: {media}')'''

#18
'''for i in range(50):
    if i % 2 ==0:
        continue
    else:
        print(f'O número {i} é impar')'''

#19 e 20
'''number1 = int(input("Digite um número inteiro: "))
number2 = int(input("Digite outro número inteiro: "))
for i in range(number1 +1, number2):
    print(f'{i} é um número inteiro entre {number1} e {number2}')
print(f'A soma dos número é: {number1 + number2}')'''

#21
'''num = int(input("Digite um número para gerar sua tabuada: "))
for i in range(1, 11):
    print(f'{i} * {num} = {i*num}')'''

#22
'''list = []
i = 0
while i < 5:
    number = int(input(f'Digite o {i +1}° número: '))
    list.append(number)
    i += 1
print(list)'''

#23
'''list = []
i = 0
while i < 10:
    number = float(input(f'Digite o {i +1}° número: '))
    list.append(number)
    i += 1
print(list[::-1])'''

#24
'''notas = []
for i in range(4):
    nota = float(input(f'Digite a {i+1}° nota: '))
    notas. append(nota)
print(f'A 1° nota é: {notas[0]}\nA 2° nota é: {notas[1]}\nA 3° nota é: {notas[2]}\nA 4° nota é: {notas[3]}\nA média é: {sum(notas)/len(notas)}')'''

#25
'''vogais = ['a', 'e', 'i', 'o', 'u']
consoantes = []
for i in range(10):
    consoante = str(input(f'Digite o {i+1}° caractere: '))
    if consoante not in vogais:
        consoantes.append(consoante)

print(f'A quantidade de consoantes detectadas foram: {len(consoantes)}')
for i in range(len(consoantes)):
    print(f'As consoantes encontradas foram: {consoantes[i]}')'''

#26
'''numbers = []
pares = []
impares = []
for i in range(20):
    number = int(input(f'Digite o {i+1}° número: '))
    numbers.append(number)
    if number %2 == 0:
        pares.append(number)
    else:
        impares.append(number)
print(f'Lista de números: {numbers}')
print(f'Lista de números pares: {pares}')
print(f'Lista de números impares: {impares}')'''

#27
'''medias = []
for i in range(10):
    notas = 0
    print(f'Bem vindo aluno {i+1}, digite suas notas:')
    for j in range(4):
        nota = float(input(f'Digite a {j+1}° nota: '))
        notas += nota
    media = notas / 4
    medias.append(media)
    print(notas)
    print(media)
print(f'As médias foram: {medias}')
print("Médias acima de 7 abaixo:")
for i in range(len(medias)):
    if medias[i] > 7:
        print(f'A média do aluno {i+1} foi: {medias[i]}')'''

#28
'''list = []
numberMulti = 1
for i in range(5):
    number = int(input(f'Digite o {i+1}° número: '))
    list.append(number)
    numberMulti *= number
print(f'Os números são: {list}')
print(f'A multiplicação entre eles é: {numberMulti}')
print(f'A soma entre eles é: {sum(list)}')'''

#29
'''idades = []
alturas = []
for i in range(5):
    print(f'Bem vindo {i+1}° pessoa!')
    idade = int(input("Digite sua idade: "))
    idades.append(idade)
    altura = float(input("Digite sua altura: "))
    alturas.append(altura)
print(idades[::-1])
print(alturas[::-1])'''

#37