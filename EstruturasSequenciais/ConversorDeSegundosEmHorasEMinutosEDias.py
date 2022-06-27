from math import floor

def DefinaDia():
    Flag = False
    while not Flag:
        try:
            x = int(input("Digite a quantidade de segundos\n"))
        
            y = (x/(60*60*24))
            
            h = y - int(y)
            
            hh = (2400*h)/100

            z = hh - int(hh)

            zz = (6000*(z))/100

            zzz = zz - int(zz)
            
            zzzz= (6000*(zzz))/100

            
            if(x < 3600):
                i = 0
                print ("Valor em {} dias {} horas  {} minutos e {} segundos ".format(int(y), i, int(floor(zz)),int(round(zzzz))))
            elif (floor(zz) >59.9):
                i = 0
                print ("Valor em {} dias {} horas  {} minutos e {} segundos ".format(int(y),int(floor(hh)),i,int(round(zzzz))))
            elif (floor(zzzz) >59.9):
                i = 0
                print ("Valor em {} dias {} horas  {} minutos e {} segundos ".format(int(y),int(floor(hh)), int(floor(zz)),i))
            
            elif(x<3600) and (floor(zz)>59.9):
                i = 0
                print ("Valor em {} dias {} horas  {} minutos e {} segundos ".format(int(y),i, i,int(round(zzzz))))
                
            elif(x<3600) and (floor(zzzz)>59.9):
                i = 0
                print ("Valor em {} dias {} horas  {} minutos e {} segundos ".format(int(y),i, int(floor(zz)),i))
            
            else:
                print ("Valor em {} dias {} horas  {} minutos e {} segundos ".format(int(y),int(floor(hh)), int(floor(zz)),int(round(zzzz))))
            Flag = True
            print("____________________________________________________")
            print ("\n\n\n\n\n")
            return DefinaDia()
        
        
        except(ValueError):
            print("\n\n\nDigite apenas números\n\n\n\n\n\n")
            exit()
            
DefinaDia()
