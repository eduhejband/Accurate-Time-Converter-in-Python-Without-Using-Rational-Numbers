t = int(input("Digite quantos nomes ira ter a lista\n"))
lista = []

for a in range(t):
    msg = str(input("\n\nDigite os nomes do usuário\n"))
    lista.append(msg)
    print("Primeira lista -> ",lista)
    while msg.isnumeric():
        print ("\n\n\nerro")
        exit()
for i in range(a):
    for j in range(a):
            if lista[j] > lista[j + 1]:
                temp = lista[j]
                lista[j] = lista[j+1]
                lista[j+1] = temp
list(lista)
print ("Lista Ordenanda -> ",lista)
