t = int(input("Digite quantos nomes ira ter a lista\n"))
lista = []
msg = ""
#for a in range(t):

while msg != "0":
    msg = str(input("\n\nDigite os nomes do usuário\n"))
    if msg != "0":
        lista.append(msg)
        print("Primeira lista -> ",lista)
        while msg.isnumeric():
            print ("\n\n\nerro")
            exit()
    
        
qtd = len(lista)
for i in range(qtd -1):
    for j in range(qtd -1):
        if lista[j] > lista[j + 1]:
            temp = lista[j]
            lista[j] = lista[j+1]
            lista[j+1] = temp
            

list(lista)
print ("Lista Ordenanda -> ",lista)
