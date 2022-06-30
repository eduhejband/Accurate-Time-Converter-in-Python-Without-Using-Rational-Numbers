def DefinaMin():
    Flag = False
    while not Flag:
        try:
            x = int(input("Digite a quantidade de Minutos\n"))
        
            y = (x/(60))

            z = y - int(y)

            zz = (6000*(z))/100
            
            zzzz = (x*60)
            

            print ("Valor em  {} horas  {} minutos".format(int(y), int(zz)))
            Flag = True
            print("\n\n")
            print("ou {} segundos".format(int(zzzz)))
            print("____________________________________________________")
            print ("\n\n\n\n\n")
            return DefinaMin()
        
        
        except(ValueError):
            print("\n\n\nDigite apenas números\n\n\n\n\n\n")
            return DefinaMin()
            
DefinaMin()
