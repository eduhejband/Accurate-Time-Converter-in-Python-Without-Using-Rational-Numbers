from math import ceil
from math import floor

def DefinaAno():
    Flag = False
    while not Flag:
        try:
        
            segundosT = int(input("Digite a quantidade de segundos\n"))
            
            ano = int(segundosT/(86400*30.396473*12))
            segundosRest = segundosT%(86400*30.396473*12)
            
            mes = int(segundosRest/(86400*30.396473))
            segundosRest1 = segundosRest%(86400*30.396473)
            
            
            dias = int(segundosRest1/86400)
            segundosRest2 = segundosRest1%86400
            
            horas = int(segundosRest2/3600)
            segundosRest3 = segundosRest2%3600
            
            minutos = int(segundosRest3/60)
            segundos = segundosRest3%60
            segundos = int(segundos)
            
            print ("Valor em {} anos {} meses {} dias {} horas  {} minutos e {} segundos ".format(ceil(ano),int(mes),dias,horas,minutos,segundos))
            Flag = True
           
            
            
            print("____________________________________________________")
            print ("\n\n\n\n\n")
            exit()
        
        
        except(ValueError):
            print("\n\n\nDigite apenas números\n\n\n\n\n\n")
            exit()



def DefinaMes():
    Flag = False
    while not Flag:
        try:
        
            segundosT = int(input("Digite a quantidade de segundos\n"))
            
            mes = int(segundosT/(86400*30.396473))
            segundosRest = segundosT%(86400*30.396473)
            
            
            dias = int(segundosRest/86400)
            segundosRest1 = segundosRest%86400
            
            horas = int(segundosRest1/3600)
            segundosRest2 = segundosRest1%3600
            
            minutos = int(segundosRest2/60)
            segundos = segundosRest2%60
            segundos = int(segundos)
            
            print ("Valor em {} meses {} dias {} horas  {} minutos e {} segundos ".format(int(mes),dias,horas,minutos,segundos))
            Flag = True
           
            
            
            print("____________________________________________________")
            print ("\n\n\n\n\n")
            exit()
        
        
        except(ValueError):
            print("\n\n\nDigite apenas números\n\n\n\n\n\n")
            exit()



def DefinaDia():
    Flag = False
    while not Flag:
        try:
        
            segundosT = int(input("Digite a quantidade de segundos\n"))
  
            dias = int(segundosT/86400)
            segundosRest = segundosT%86400
            
            horas = int(segundosRest/3600)
            segundosRest1 = segundosRest%3600
            
            minutos = int(segundosRest1/60)
            segundos = segundosRest1%60
            segundos = int(segundos)
            
            print ("Valor em {} dias {} horas  {} minutos e {} segundos ".format(dias,horas,minutos,segundos))
            Flag = True
           
            
            
            print("____________________________________________________")
            print ("\n\n\n\n\n")
            exit()
        
        
        except(ValueError):
            print("\n\n\nDigite apenas números\n\n\n\n\n\n")
            exit()



def DefinaHoras():
    Flag = False
    while not Flag:
        try:
        
            segundosT = int(input("Digite a quantidade de segundos\n"))
  
 
            
            horas = int(segundosT/3600)
            segundosRest1 = segundosT%3600
            
            minutos = int(segundosRest1/60)
            segundos = segundosRest1%60
            segundos = int(segundos)
            
            print ("Valor em  {} horas  {} minutos e {} segundos ".format(horas,minutos,segundos))
            Flag = True
           
            
            
            print("____________________________________________________")
            print ("\n\n\n\n\n")
            exit()
        
        
        except(ValueError):
            print("\n\n\nDigite apenas números\n\n\n\n\n\n")
            exit()
            


def DefinaMin():
    Flag = False
    while not Flag:
        try:
        
            minutosT = int(input("Digite a quantidade de Minutos\n"))
  
 

            
            horas = int(minutosT/60)
            segundosRest1 = minutosT%60
            
            minutos = segundosRest1%60
            minutos = int(minutos)
    
 
            print ("Valor em  {} horas  {} minutos ".format(horas,minutos))
            Flag = True
           
            
            
            print("____________________________________________________")
            print ("\n\n\n\n\n")
            exit()
        
        
        except(ValueError):
            print("\n\n\nDigite apenas números\n\n\n\n\n\n")
            exit()



def DefinaMinD():
    Flag = False
    while not Flag:
        try:
        
            minutosT = int(input("Digite a quantidade de minutos\n"))
  
            dias = int(minutosT/1440)
            minutosRest = minutosT%1440
            
            horas = int(minutosRest/60)
            minutosRest1 = minutosRest%60
            
            
            minutos = minutosRest1%60
            minutos = int(minutos)
            
            print ("Valor em {} dias {} horas e {} minutos".format(dias,horas,minutos))
            Flag = True
           
            
            
            print("____________________________________________________")
            print ("\n\n\n\n\n")
            exit()
        
        
        except(ValueError):
            print("\n\n\nDigite apenas números\n\n\n\n\n\n")
            exit()
            



def DefinaMinM():
    Flag = False
    while not Flag:
        try:
        
            minutosT = int(input("Digite a quantidade de minutos\n"))
            
            
            
            meses = int(minutosT/43200)
            minutosRest = minutosT%43200
            
            dias = int(minutosRest/1440)
            minutosRest1 = minutosRest%1440
            
            horas = int(minutosRest1/60)
            minutosRest2 = minutosRest1%60
            
            
            minutos = minutosRest2%60
            minutos = int(minutos)
            
            print ("Valor em {} meses {} dias {} horas e {} minutos".format(meses,dias,horas,minutos))
            Flag = True
           
            
            
            print("____________________________________________________")
            print ("\n\n\n\n\n")
            exit()
        
        
        except(ValueError):
            print("\n\n\nDigite apenas números\n\n\n\n\n\n")
            exit()



def DefinaMinA():
    Flag = False
    while not Flag:
        try:
        
            minutosT = int(input("Digite a quantidade de minutos\n"))
            
            ano = int(minutosT/(1440*30.396473*12))
            minutosRest = minutosT%(1440*30.396473*12)
            
            meses = int(minutosRest/43200)
            minutosRest1 = minutosRest%43200
            
            dias = int(minutosRest1/1440)
            minutosRest2 = minutosRest1%1440
            
            horas = int(minutosRest2/60)
            minutosRest3 = minutosRest2%60
            
            
            minutos = minutosRest3%60
            minutos = int(minutos)
            
            print ("Valor em {} anos {} meses {} dias {} horas e {} minutos".format(ano,meses,dias,horas,minutos))
            Flag = True
           
            
            
            print("____________________________________________________")
            print ("\n\n\n\n\n")
            exit()
        
        
        except(ValueError):
            print("\n\n\nDigite apenas números\n\n\n\n\n\n")
            exit()


def DefinaHoraAno():
    Flag = False
    while not Flag:
        try:
        
            minutosT = int(input("Digite a quantidade de horas\n"))
            
            ano = int(minutosT/(24*30.396473*12))
            minutosRest = minutosT%(24*30.396473*12)
            
            meses = int(minutosRest/720)
            minutosRest1 = minutosRest%720
            
            dias = int(minutosRest1/24)
            minutosRest2 = minutosRest1%24
            
            horas = int(minutosRest2%60)
            
            
            print ("Valor em {} anos {} meses {} dias e {} horas ".format(ano,meses,dias,horas))
            Flag = True
           
            
            
            print("____________________________________________________")
            print ("\n\n\n\n\n")
            return exit()
        
        
        except(ValueError):
            print("\n\n\nDigite apenas números\n\n\n\n\n\n")
            return exit()
            


def DefinaHoraMes():
    Flag = False
    while not Flag:
        try:
        
            minutosT = int(input("Digite a quantidade de horas\n"))
            
            
            
            meses = int(minutosT/720)
            minutosRest1 = minutosT%720
            
            dias = int(minutosRest1/24)
            minutosRest2 = minutosRest1%24
            
            horas = int(minutosRest2%60)
            
            print ("Valor em {} meses {} dias e {} horas ".format(meses,dias,horas))
            Flag = True
           
            print("____________________________________________________")
            print ("\n\n\n\n\n")
            return exit()
        
        
        except(ValueError):
            print("\n\n\nDigite apenas números\n\n\n\n\n\n")
            return exit()
            
def DefinaHoraDia():
    Flag = False
    while not Flag:
        try:
        
            minutosT = int(input("Digite a quantidade de horas\n"))
            
            dias = int(minutosT/24)
            minutosRest2 = minutosT%24
            
            horas = int(minutosRest2%24)
            
            print ("Valor em {} dias e {} horas ".format(dias,horas))
            Flag = True
           
            print("____________________________________________________")
            print ("\n\n\n\n\n")
            return exit()
        
        
        except(ValueError):
            print("\n\n\nDigite apenas números\n\n\n\n\n\n")
            return exit()

            
print("Guia:\n")

print("1 - Segundos -> Ano")

print ("\n\n2 - Segundos -> Mês\n\n")

print("3 - Segundos -> Dias\n\n")

print("4 - Segundos -> Horas\n\n")

print("5 - Minutos -> Horas\n\n")

print("6 - Minutos -> Dias\n\n")

print("7 - Minutos -> Meses\n\n")

print("8 - Minutos -> Ano\n\n")

print("9 - Horas -> Dias\n\n")

print("10 - Horas -> Meses\n\n")

print("11 - Horas -> Anos\n\n")

print("_____________________________\n\n\n\n\n")


t = int(input("Digite o conversor escolhido\n"))

if (t==1):
    print("\n\n\n\n\n")
    DefinaAno()

elif (t == 2):
    print("\n\n\n\n\n")
    DefinaMes()
    
elif (t == 3):
    print("\n\n\n\n\n")
    DefinaDia()

elif (t == 4):
    print("\n\n\n\n\n")
    DefinaHoras()
    
elif (t == 5):
    print("\n\n\n\n\n")
    DefinaMin()

elif (t == 6):
    print("\n\n\n\n\n")
    DefinaMinD()
    
elif (t == 7):
    print("\n\n\n\n\n")
    DefinaMinM()
    
elif (t == 8):
    print("\n\n\n\n\n")
    DefinaMinA()

elif (t == 9):
    print("\n\n\n\n\n")
    DefinaHoraDia()
    
elif (t == 10):
    print("\n\n\n\n\n")
    DefinaHoraMes()
    
elif (t == 11):
    print("\n\n\n\n\n")
    DefinaHoraAno()
