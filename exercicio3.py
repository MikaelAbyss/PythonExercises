# Será lido as 4 notas que o usuário digitar
numNota = float(input("Digite a primeira nota: "))
numNota2 = float(input("Digite a segunda nota: "))
numNota3 = float(input("Digite a terceira nota: "))
numNota4 = float(input("Digite a quarta nota: "))
suasNotas = [numNota, numNota2, numNota3, numNota4]
# Aqui será calculado a média das notas
numMedia = (numNota + numNota2 + numNota3 + numNota4) / 4
# Imprimindo as notas e a sua média
print("As respectivas notas são {} " .format(suasNotas), "e a sua média é {}".format(numMedia))
