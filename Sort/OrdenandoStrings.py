x = int(input("Digite quantos nomes vao ter a lista\n"))
user = []

for a in range(x):
    msg = str(input("\n\nDigite os nomes do usuário\n"))
    user.append(msg)
    while msg.isnumeric():
        print ("\n\n\nerro")
        exit()
list.sort(user)
print("\n\n\n", user)
