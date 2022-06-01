h = input ("Quantas horas voce trabalha?\n")

m = input ("\n\n Quanto voce ganha por hora\n")

s = float(h) * float(m)

print ("\n\n\nSalario bruto é igual a", s)


Ir = float(s) * 0.11
print ("\nImposto de Renda é", Ir)

INSS = float(s) * 0.08
print ("\nINSS é", INSS)

Sindicato = float(s) * 0.05
print ("\nSindicato é ", Sindicato)

SL = float(s) - (float(Sindicato) + float(INSS) + float(Ir))
print ("\nSalario Liquido é",SL)
