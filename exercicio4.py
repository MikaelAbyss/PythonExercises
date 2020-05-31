minhaLista = []
v = ['a', 'e', 'i', 'o', 'u']
for i in range(0, 10):
    minhaLista.append(str(input('Informe um caracter: ')))
conso = []
todasConsoantes = 0
for i in range(0, 10):
    if minhaLista[i] not in v:
        conso.append(minhaLista[i])
        todasConsoantes += 1
print("Na lista, o número de consoantes foi %d " % todasConsoantes)
print(conso)
