#t = int(input("Digite quantos nomes ira ter a lista\n"))
lista = ['j','i','h','g','f','e', 'd', 'c', 'b', 'a']
#lista = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
msg = ""
ordenado = True
perfi = 0
perfj = 0
i = ""
j = ""
#for a in range(t):

'''
while msg != "0":
    msg = str(input("\n\nDigite os nomes do usuário\n"))
    if msg != "0":
        lista.append(msg)
        print("Primeira lista -> ",lista)
        while msg.isnumeric():
            print ("\n\n\nerro")
            exit()
    
'''        
qtd = len(lista)-1
ordenado = False 
#for i in range(qtd -1):
    #perfi = perfi + 1
    
while not ordenado:
    perfi = perfi + 1
    ordenado = True  
    for j in range(qtd):
        perfj = perfj + 1
        if lista[j] > lista[j + 1]:
            ordenado = True
            temp = lista[j]
            lista[j] = lista[j+1]
            lista[j+1] = temp
            ordenado = False
        qtd = qtd -1
            

list(lista)
print ("Lista Ordenanda -> ",lista)
print (perfi)
print (perfj)
print(perfi*perfj
