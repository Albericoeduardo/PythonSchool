#2
'''i = 1
while i <= 10:
    if i % 2 != 0:
        print(i)
    else:
        print("Número par")
    i += 1'''

#3
'''for j in range(9, -1, -1):
    print(j)'''

#4
'''k = -2999
while k <= 1000:
    print(k)
    k += 1'''

#5
'''number = int(input("Digite um número: "))
divisor = 0
for l in range(1, number):
    if number % l == 0:
        divisor += l
        if divisor == number:
            print(f'O número {divisor} é perfeito')'''

#6
userNumber = int(input("Digite um número: "))
fatorial = 1
for m in range(userNumber, 1, -1):
    fatorial *= m
print(f'O fatorial de {userNumber} é: {fatorial}')

#7
'''list = str(input("Digite o que quiser: ")).split()
palavra = ""
for i in list:
    if len(i) > len(palavra):
        palavra = i
print(f'A maior palavra é: {palavra}')'''
    