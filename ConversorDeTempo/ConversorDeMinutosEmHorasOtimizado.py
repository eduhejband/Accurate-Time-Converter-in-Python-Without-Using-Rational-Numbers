from math import floor

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
            return DefinaMin()
        
        
        except(ValueError):
            print("\n\n\nDigite apenas números\n\n\n\n\n\n")
            exit()
            
DefinaMin()
