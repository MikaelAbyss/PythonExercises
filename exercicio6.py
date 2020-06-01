minhaListaNegativa = []
minhaListaPositiva = []
minhaListaCompleta = []

for i in range(0,10):
    numInt = int(input("Digite um número positivo ou negativo: "))
    minhaListaCompleta.append(int(numInt))
    # Se o numInt for menor que 0, ele será interpretado como um número negativo e adicionado a sua devida lista.
    if (numInt) < 0:
        minhaListaNegativa.append(numInt)
        print("Um número negativo foi adicionado! {}".format(minhaListaNegativa))
    # Caso o contrário, o numInt seja maior que 0, será adicionado na lista de números positivos.
    else:
        minhaListaPositiva.append(numInt)
        print("Um número positivo foi adicionado! {}".format(minhaListaPositiva))
# Aqui iremos imprimir todos os vetores, deis dos números negativos, positivos e todos ambos que foram digitados.
print("Todos os números digitados foram: {}".format(minhaListaCompleta))
print("Todos os números negativos digitados foram: {}".format(minhaListaNegativa))
print("Todos os números positivos digitados foram: {}".format(minhaListaPositiva))
