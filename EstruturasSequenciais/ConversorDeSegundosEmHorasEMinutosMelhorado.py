from math import floor

def DefinaNome():
    Flag = False
    while not Flag:
        try:
            x = int(input("Digite a quantidade de segundos\n"))
        
            y = (x/(60*60))

            yy = round(y, 0)

            z = y - int(y)

            zz = (6000*(z))/100

            zzz = zz - int(zz)
            
            zzzz= (6000*(zzz))/100

            
            if(x < 3600):
                i = 0
                print ("Valor em  {} horas  {} minutos e {} segundos ".format(i, int(floor(zz)),int(round(zzzz))))
            elif (floor(zz) >59.9):
                i = 0
                print ("Valor em  {} horas  {} minutos e {} segundos ".format(int(floor(y)),i,int(round(zzzz))))
            elif (floor(zzzz) >59.9):
                i = 0
                print ("Valor em  {} horas  {} minutos e {} segundos ".format(int(floor(y)), int(floor(zz)),i))
            
            elif(x<3600) and (floor(zz)>59.9):
                i = 0
                print ("Valor em  {} horas  {} minutos e {} segundos ".format(i, i,int(round(zzzz))))
                
            elif(x<3600) and (floor(zzzz)>59.9):
                i = 0
                print ("Valor em  {} horas  {} minutos e {} segundos ".format(i, int(floor(zz)),i))
            
            else:
                print ("Valor em  {} horas  {} minutos e {} segundos ".format(int(floor(y)), int(floor(zz)),int(round(zzzz))))
            Flag = True
        
        
        except(ValueError):
            print("\n\n\nDigite apenas números\n\n\n\n\n\n")
            exit()
            
DefinaNome()
