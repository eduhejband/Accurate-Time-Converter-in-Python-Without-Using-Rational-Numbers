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
DefinaHoraDia()    
