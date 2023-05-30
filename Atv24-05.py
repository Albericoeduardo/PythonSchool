import random

#1
'''list = ["Limao", "Caju", "Acerola", "Laranja", "Goiaba", "Banana",
         "Pitaya", "Uva", "Pera", "Maça", "Tamarindo", "Açai"]
list.insert(10, 'Joao')
print(list[10])'''

#2
'''numbers = [1, 6, 8, 9, 3, 5, 6, 2, 3, 4, 1, 90, 3, 88, 54, 2, 34, 
          78, 23, 98, 34, 23, 7, 8, 6, 1, 9, 2, 3, 4, 5, 2, 66, 
          7, 4, 85, 36, 2, 3, 9, 52, 13, 16, 21, 8, 9, 3, 5, 6, 
          2, 3, 4, 1, 90, 3, 88, 54, 2, 34, 78, 23, 98, 34, 23, 
          7, 8, 6, 1, 9, 2, 3, 4, 5, 2, 66, 7, 4, 85, 36, 2, 3, 
          9, 52, 13, 16, 25, 8, 9, 8, 5, 6, 2, 3, 4, 1, 90, 3, 
          88, 54, 2, 34, 78, 230, 98, 34, 23, 7, 8, 6, 1, 9, 2, 
          3, 4, 5, 2, 66, 7, 4, 85, 36, 2, 3, 9, 52, 13, 16, 26, 
          8, 9, 5, 5, 6, 2, 3, 4, 1, 90, 3, 88, 54, 2, 34, 78, 
          23, 98, 34, 23, 7, 8, 6, 109, 9, 2, 3, 4, 5, 2, 66, 7, 
          4, 85, 36, 2, 3, 9, 52, 13, 16, 23, 8, 9, 3, 5, 6, 2, 3, 
          4, 1, 90, 3, 88, 54, 2, 34, 78, 23, 98, 34, 231, 7, 
          8, 6, 1, 9, 2, 3, 4, 5, 2, 66, 7, 4, 85, 36, 2, 3, 9, 
          52, 13, 16, 28, 8, 9, 1, 5, 6, 2, 3, 4, 1, 90, 3, 88, 
          54, 2, 34, 78, 23, 98, 34, 23, 7, 8, 6, 1, 9, 2, 3, 
          4, 5, 2, 66, 7, 4, 85, 36, 2, 3, 9, 52, 13, 16, 29]

soma = sum(numbers)
print(soma)

#3
max = max(numbers)
print(max)'''

#4
'''words = ["O", "seu", "Tatá", "tá?", "Não", "o", "seu", "Tatá", 
         "não", "tá", "mas", "a", "mulher", "do", "seu", "Tatá", 
         "tá", ".", "E", "quando", "a", "mulher", "do", "seu", 
         "Tatá", "tá", "é", "a", "mesma", "coisa", "que", "o", 
         "seu", "Tatá", "tá", "tá?"]

tata = words.count('Tatá')
print(tata)'''

#5
'''alfabeto = ["a", "b", "c", "d", "e", "f", "g", "h"]
alfabeto.reverse()
print(alfabeto)'''

#6
'''numbersList = [1, 3, 5, 7, 9, 11, 13, 10, 14]

for i in range(len(numbersList)):
    if numbersList[i] > numbersList[i+1]:
        print(f'Ordem incorreta! {numbersList[i]} é maior que {numbersList[i+1]}')
    else:
        print(f'Ordem correta {numbersList[i]}')'''

#7
'''userNumbers = []
while True:
    userNumber = input("Digite quantos números quiser(digite 'sair' para sair ou parar): ")
    if userNumber.lower() == 'sair':
        break
    userNumbers.append(int(userNumber))

total = sum(userNumbers)
media = total / len(userNumbers)
print(f'A média é {media}')'''

#8
'''num = 2
for i in range(len(numbersList)):
    print(f'A multiplicação de cada elemento da lista por {num} é {numbersList[i]} * {num} = {numbersList[i] * num} ')'''

#9
'''list1 = [15, 32, 51, 42, 15, 61]
list2 = [61, 23, 51, 62, 124, 4]

total1 = sum(list1)
total2 = sum(list2)
print(f'{total1} {total2}')

if total1 == total2:
    print('Listas iguais')
else:
    print('listas diferentes')'''

#10
'''impar = []
for i in range(len(numbersList)):
    if numbersList[i] % 2 == 0:
        print(f'{numbersList[i]} é número par')
    else:
        print(f'{numbersList[i]} é número impar')
        impar.append('impar')
        break

if impar[0] == 'impar':
    print('A lista contém números impares')'''

#11
'''count = 0
for i in range(len(numbers)):
    if numbers[i] < 100:
        print(f'{numbers[i]} é menor que 100!')
        count += 1
print(f'A quantidade de números menor que 100 é = {count}')'''

#12
'''palavra = random.choice(list).lower()
print(palavra)
letras = ['_'] * len(palavra)
print(letras)
letrasUsadas = []

while True:
    print(f'A palavra contem {len(letras)} letras')
    letra = input((f'JOGO DA FORCA! Escolha uma letra e vejá se contem na palavra: '))

    if letra in letrasUsadas:
        print(f'Você ja tentou usar a letra: {letra.upper()}, tente outra')
        continue

    letrasUsadas.append(letra)

    if letra in palavra:
        for i in range(len(palavra)):
            if palavra[i] == letra:
                letras[i] == letra
        
        if '_' not in letrasUsadas:
            print(f'parabéns voce ganhou! A palavra era {palavra} mesmo')
            break
    else:
        print(f'{letra} não encontrada na palavra')'''