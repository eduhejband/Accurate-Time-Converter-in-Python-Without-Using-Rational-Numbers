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
            
DefinaMinA()       
