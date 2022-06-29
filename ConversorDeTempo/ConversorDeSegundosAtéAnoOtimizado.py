from math import ceil

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
            return DefinaAno()
        
        
        except(ValueError):
            print("\n\n\nDigite apenas números\n\n\n\n\n\n")
            exit()
            
DefinaAno()
