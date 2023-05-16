import random
number = random.randint(1,100)
print(number)
print("Jogo da adivinhação! Tente adivinhar um número entre 1 e 100:")
escolha = int(input("Escolhe um número: "))
if escolha == number:
    print("Parabens!!! Você acertou o número😁")
elif escolha >= number + 20:
    print("Está frio, o número está muito abaixo")
    escolha = int(input("Escolha outro número: "))
elif escolha >= number - 20:
    print("Está frio, o número está muito acima")
    escolha = int(input("Escolha outro número: "))




