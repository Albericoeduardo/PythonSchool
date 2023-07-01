list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
number = int(input("Digite um número entre 1 e 26: "))
if number > 26 or number <1:
    number = int(input(f'ERROR! digite o número novamente: '))

print(f'As lestra do alfabeto até a {number}° letra são: {list[:number]}')