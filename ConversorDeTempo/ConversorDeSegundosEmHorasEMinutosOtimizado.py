from math import floor

def DefinaSegs():
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
            return DefinaSegs()
        
        
        except(ValueError):
            print("\n\n\nDigite apenas números\n\n\n\n\n\n")
            exit()
            
DefinaSegs()
