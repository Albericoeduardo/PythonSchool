idade = int(input('Qual sua idade?'))

if idade >= 18:
	print("Você pode dirigir, colega!")
elif idade > 16 and idade < 18:
	print("Você está quase lá, falta apenas 1 ano")
else:
	print("Se acalme acalme, ainda vai demorar um pouco!")