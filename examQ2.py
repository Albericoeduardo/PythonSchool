list = []
iguais = 0
while True:
    number = float(input("Digite um número (ou 0 para sair): "))
    if number == 0:
        break
    list.append(number)

for i in range(len(list)):
    times = list.count(list[i])
    if times > 1:
        iguais += 1

if times != 0:
    print(f'Existem {iguais} números iguais na lista!')