from math import floor

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
            return DefinaDia()
        
        
        except(ValueError):
            print("\n\n\nDigite apenas números\n\n\n\n\n\n")
            exit()
            
DefinaDia()
