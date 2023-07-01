list = []
menor = 0
while True:
    number = float(input("Digite um número: "))
    if number == 0:
        break
    list.append(number)
    menor = number
    if number < menor:
        menor = number
print(f'O maior número da lista é: {max(list)}')
print(f'O menor número da lista é: {menor}')