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

DefinaHoraMes()            
