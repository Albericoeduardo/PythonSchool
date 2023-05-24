import random

#Não funcional com opções
'''number = random.randint(1, 100)
print(number)
print("Adivinhe o número de 1 a 100!!")
escolha = int(input("Selecione um número: "))
while True:
    print(number - escolha)
    if escolha == number:
        print(f'Acertou!! o número era {number} mesmo!')
        break
    elif number - escolha > 10:
        escolha = int(input("Está frio! Selecione outro número: "))
    elif number - escolha <= 10 and number - escolha > 5:
        escolha = int(input(f'Está quente! Entre {number - 10} e {number + 10} casas: '))
    elif number - escolha <= 5:
        escolha = int(input(f'Está pegando fogo! Entre {number - 5} e {number + 5} casas: '))
    else:
        escolha = int(input("Errado! Selecione outro número: "))'''

#Funcional sem opções
number = random.randint(1, 100)
print(number)
print("Adivinhe o número de 1 a 100!!")
escolha = int(input("Selecione um número: "))
while True:
    print(number - escolha)
    if escolha == number:
        print(f'Acertou!! o número era {number} mesmo!')
        break
    else:
        escolha = int(input("Errado! Selecione outro número: "))