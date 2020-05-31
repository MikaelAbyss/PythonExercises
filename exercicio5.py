# Definindo os vetores
listaImpares = []
listaPar = []
listaPrincipal = []

# Criando um loop de no máximo 20 números sejam digitados
for i in range(0, 20):
    numeros = int(input("Digite os números aqui: "))
    listaPrincipal.append(numeros)
# Aqui se realiza a divisão por 2 e caso o restante seja 1, o número será impar e será adicionado na sua lista
    if (numeros%2) == 1:
        listaImpares.append(numeros)
        print("O número é impar! {}" .format(listaImpares))
# Caso na divisão apenas reste 0, o número será intepretado como par e adicionado a sua lista
    else:
        listaPar.append(numeros)
        print("O número é par! {}" .format(listaPar))
print("Todos os números digitados foram {}".format(listaPrincipal))
print("Todos os números impares digitados foram {}".format(listaImpares))
print("Todos os números pares digitados foram {}".format(listaPar))
