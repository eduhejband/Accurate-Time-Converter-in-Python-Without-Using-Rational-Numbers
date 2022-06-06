
nota1 = float(input("\nDigite a nota da média do primeiro bimestre\n"))
nota2 = float(input("\n\n\nDigite a nota da média do segundo bimestre\n"))
nota3 = float(input("\n\n\nDigite a nota da média do terceiro bimestre\n"))
nota4 = float(input("\n\n\nDigite a nota da média do quarto bimestre\n"))

print ("\n\n___________________________________________________________________________________________________")
x1 = int(input("\n\n\nDigite o peso do primeiro bimestre\n"))
x2 = int(input("\n\n\nDigite o peso do segundo bimestre\n"))
x3 = int(input("\n\n\nDigite o peso do terceiro bimestre\n"))
x4 = int(input("\n\n\nDigite o peso do quarto bimestre\n"))

print ("\n\n___________________________________________________________________________________________________")
divisor = int(x1)+int(x2)+int(x3)+int(x4)

media = ((int(x1)*float(nota1))+(int(x2)*float(nota2))+(int(x3)*float(nota3))+(int(x4)*float(nota4)))/int(divisor)

print ("\n\n\nMédia final:", float(media))

if (media >=6):
    print("\n\nAluno está aprovado")
else:
    print("\n\nAluno está reprovado")
