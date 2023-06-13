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