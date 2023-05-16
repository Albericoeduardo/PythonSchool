#1
soma = 0
for i in range(10):
    num = float(input("Digite um número: "))
    soma += num

media = soma/10
print(f'A média dos números é: {media}')
#2
for i in range(1000):
    i += 1
    print(i)
#3
i = 10
while i >= -10:
    print(i)
    i -= 1 
#4
i = 1
while i <=100:
    if i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)
    i +=1
    
#5
i = 1
num = float(input("Digite um número: "))
while i <= num:
    print(num / i)
    i += 1