def DefinaNome():
    Flag = False
    while not Flag:
        try:
            x = int(input("Digite a quantidade de segundos\n"))
            trn = x


            y = (x/(60*60))

            yy = round(y, 0)

            z = y - int(y)

            zz = (6000*(z))/100

            zzz = zz - int(zz)
            
            zzzz= (6000*(zzz))/100

            if(x<3600):
                i = 0
                print ("Valor em  {} horas  {} minutos e {} segundos ".format(i, int(round(zz,0)),int(round(zzzz,0))))
            elif (zz >59):
                i = 0
                print ("Valor em  {} horas  {} minutos e {} segundos ".format(int(round(y,0)),i,int(round(zzzz,0))))
            elif (zzzz >59):
                i = 0
                print ("Valor em  {} horas  {} minutos e {} segundos ".format(int(round(y,0)), int(round(zz,0)),i))
            else:
                print ("Valor em  {} horas  {} minutos e {} segundos ".format(int(round(y,0)), int(round(zz,0)),int(round(zzzz,0))))
            Flag = True
        
        
        except(ValueError):
            print("\n\n\nDigite apenas números\n\n\n\n\n\n")
            exit()
            
DefinaNome()
