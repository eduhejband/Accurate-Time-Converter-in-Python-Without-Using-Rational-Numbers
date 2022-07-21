from math import ceil
from math import floor

def DefinaAno():
    Flag = False
    while not Flag:
        try:
        
            segundosT = int(input(" Digite a quantidade de segundos\n"))
            
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
            
            print (" Valor em {} anos {} meses {} dias {} horas  {} minutos e {} segundos ".format(ceil(ano),int(mes),dias,horas,minutos,segundos))
            Flag = True
           
            
            
            print("____________________________________________________")
            print ("\n\n\n\n\n")
            return DefinaAno()
        
        
        except(ValueError):
            print("\n\n\n Digite apenas números\n\n\n\n\n\n")
            return Chamamento()



def DefinaMes():
    Flag = False
    while not Flag:
        try:
        
            segundosT = int(input(" Digite a quantidade de segundos\n"))
            
            mes = int(segundosT/(86400*30.396473))
            segundosRest = segundosT%(86400*30.396473)
            
            
            dias = int(segundosRest/86400)
            segundosRest1 = segundosRest%86400
            
            horas = int(segundosRest1/3600)
            segundosRest2 = segundosRest1%3600
            
            minutos = int(segundosRest2/60)
            segundos = segundosRest2%60
            segundos = int(segundos)
            
            print (" Valor em {} meses {} dias {} horas  {} minutos e {} segundos ".format(int(mes),dias,horas,minutos,segundos))
            Flag = True
           
            
            
            print("____________________________________________________")
            print ("\n\n\n\n\n")
            return DefinaMes()
         
        
        except(ValueError):
            print("\n\n\n Digite apenas números\n\n\n\n\n\n")
            return Chamamento()



def DefinaDia():
    Flag = False
    while not Flag:
        try:
        
            segundosT = int(input(" Digite a quantidade de segundos\n"))
  
            dias = int(segundosT/86400)
            segundosRest = segundosT%86400
            
            horas = int(segundosRest/3600)
            segundosRest1 = segundosRest%3600
            
            minutos = int(segundosRest1/60)
            segundos = segundosRest1%60
            segundos = int(segundos)
            
            print (" Valor em {} dias {} horas  {} minutos e {} segundos ".format(dias,horas,minutos,segundos))
            Flag = True
           
            
            
            print("____________________________________________________")
            print ("\n\n\n\n\n")
            return DefinaDia()
        
        
        except(ValueError):
            print("\n\n\n Digite apenas números\n\n\n\n\n\n")
            return Chamamento()



def DefinaHoras():
    Flag = False
    while not Flag:
        try:
        
            segundosT = int(input(" Digite a quantidade de segundos\n"))
  
 
            
            horas = int(segundosT/3600)
            segundosRest1 = segundosT%3600
            
            minutos = int(segundosRest1/60)
            segundos = segundosRest1%60
            segundos = int(segundos)
            
            print (" Valor em  {} horas  {} minutos e {} segundos ".format(horas,minutos,segundos))
            Flag = True
            print("____________________________________________________")
            print ("\n\n\n\n\n")
            return DefinaHoras()
            
        except(ValueError):
            print("\n\n\n Digite apenas números\n\n\n\n\n\n")
            return Chamamento()
            
            
def DefinaSegsMin():
    Flag = False
    while not Flag:
        try:
        
            segundosT = int(input(" Digite a quantidade de segundos\n"))
  
 
            
            minutos = int(segundosT/60)
            segundosRest1 = segundosT%60
            segundos = int(segundosRest1)
            
            print (" Valor em  {} minutos e {} segundos ".format(minutos,segundos))
            Flag = True
           
            
            
            print("____________________________________________________")
            print ("\n\n\n\n\n")
            
            return DefinaSegsMin()
        
        
      
        
        
        except(ValueError):
            print("\n\n\n Digite apenas números\n\n\n\n\n\n")
            return Chamamento()
            


def DefinaMin():
    Flag = False
    while not Flag:
        try:
        
            minutosT = int(input(" Digite a quantidade de Minutos\n"))
  
 

            
            horas = int(minutosT/60)
            segundosRest1 = minutosT%60
            
            minutos = segundosRest1%60
            minutos = int(minutos)
    
 
            print (" Valor em  {} horas  {} minutos ".format(horas,minutos))
            Flag = True
           
            
            
            print("____________________________________________________")
            print ("\n\n\n\n\n")
            return DefinaMin()
        
        
        except(ValueError):
            print("\n\n\n Digite apenas números\n\n\n\n\n\n")
            return Chamamento()



def DefinaMinD():
    Flag = False
    while not Flag:
        try:
        
            minutosT = int(input(" Digite a quantidade de minutos\n"))
  
            dias = int(minutosT/1440)
            minutosRest = minutosT%1440
            
            horas = int(minutosRest/60)
            minutosRest1 = minutosRest%60
            
            
            minutos = minutosRest1%60
            minutos = int(minutos)
            
            print (" Valor em {} dias {} horas e {} minutos".format(dias,horas,minutos))
            Flag = True
           
            
            
            print("____________________________________________________")
            print ("\n\n\n\n\n")
            return DefinaMinD()
        
        
        except(ValueError):
            print("\n\n\n Digite apenas números\n\n\n\n\n\n")
            return Chamamento()
            



def DefinaMinM():
    Flag = False
    while not Flag:
        try:
        
            minutosT = int(input(" Digite a quantidade de minutos\n"))
            
            
            
            meses = int(minutosT/43200)
            minutosRest = minutosT%43200
            
            dias = int(minutosRest/1440)
            minutosRest1 = minutosRest%1440
            
            horas = int(minutosRest1/60)
            minutosRest2 = minutosRest1%60
            
            
            minutos = minutosRest2%60
            minutos = int(minutos)
            
            print (" Valor em {} meses {} dias {} horas e {} minutos".format(meses,dias,horas,minutos))
            Flag = True
           
            
            
            print("____________________________________________________")
            print ("\n\n\n\n\n")
            return DefinaMinM()
        
        
        except(ValueError):
            print("\n\n\n Digite apenas números\n\n\n\n\n\n")
            return Chamamento()



def DefinaMinA():
    Flag = False
    while not Flag:
        try:
        
            minutosT = int(input(" Digite a quantidade de minutos\n"))
            
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
            
            print (" Valor em {} anos {} meses {} dias {} horas e {} minutos".format(ano,meses,dias,horas,minutos))
            Flag = True
           
            
            
            print("____________________________________________________")
            print ("\n\n\n\n\n")
            return DefinaMinA()
        
        
        except(ValueError):
            print("\n\n\n Digite apenas números\n\n\n\n\n\n")
            return Chamamento()


def DefinaHoraAno():
    Flag = False
    while not Flag:
        try:
        
            horasT = int(input(" Digite a quantidade de horas\n"))
            
            ano = int(horasT/(24*30.396473*12))
            horasRest = horasT%(24*30.396473*12)
            
            meses = int(horasRest/720)
            horasRest1 = horasRest%720
            
            dias = int(horasRest1/24)
            horasRest2 = horasRest1%24
            
            horas = int(horasRest2%60)
            
            
            print (" Valor em {} anos {} meses {} dias e {} horas ".format(ano,meses,dias,horas))
            Flag = True
           
            
            
            print("____________________________________________________")
            print ("\n\n\n\n\n")
            return DefinaHoraAno()
        
        
        except(ValueError):
            print("\n\n\n Digite apenas números\n\n\n\n\n\n")
            return Chamamento()
            


def DefinaHoraMes():
    Flag = False
    while not Flag:
        try:
        
            horasT = int(input(" Digite a quantidade de horas\n"))
            
            
            
            meses = int(horasT/720)
            horasRest1 = horasT%720
            
            dias = int(horasRest1/24)
            horasRest2 = horasRest1%24
            
            horas = int(horasRest2%60)
            
            print (" Valor em {} meses {} dias e {} horas ".format(meses,dias,horas))
            Flag = True
           
            print("____________________________________________________")
            print ("\n\n\n\n\n")
            return DefinaHoraMes()
        
        
        except(ValueError):
            print("\n\n\n Digite apenas números\n\n\n\n\n\n")
            return Chamamento()
            
            
def DefinaHoraDia():
    Flag = False
    while not Flag:
        try:
        
            horasT = int(input(" Digite a quantidade de horas\n"))
            
            dias = int(horasT/24)
            horasRest2 = horasT%24
            
            horas = int(horasRest2%24)
            
            print (" Valor em {} dias e {} horas ".format(dias,horas))
            Flag = True
           
            print("____________________________________________________")
            print ("\n\n\n\n\n")
            return DefinaHoraDia()
        
        
        except(ValueError):
            print("\n\n\n Digite apenas números\n\n\n\n\n\n")
            return Chamamento()
   
            
def DefinaDiaToAnos():
    Flag = False
    while not Flag:
        try:
        
            diasT = int(input(" Digite a quantidade de dias\n"))
            
            
            
            ano = (diasT/(30.396473*12))
            diasRest = (diasT%(30.396473*12))
            
            meses = int(diasRest/30.396473)
            diasRest1 = diasRest%30.396473
            
            dias = diasRest1%30.396473
            
            
            
            print (" Valor em {} anos {} meses {} dias ".format(int(ano),meses, int(dias)))
            Flag = True
           
            print("____________________________________________________")
            print ("\n\n\n\n\n")
            return DefinaDiaToAnos()
        
        
        except(ValueError):
            print("\n\n\n Digite apenas números\n\n\n\n\n\n")
            return Chamamento()
            
def DefinaDiaToMeses():
    Flag = False
    while not Flag:
        try:
        
            diasT = int(input(" Digite a quantidade de dias\n"))
            
            
            meses = int(diasT/30.396473)
            diasRest1 = diasT%30.396473
            
            dias = diasRest1%30.396473
            
            
            
            print (" Valor em {} meses {} dias ".format(int(meses), int(dias)))
            Flag = True
           
            print("____________________________________________________")
            print ("\n\n\n\n\n")
            return DefinaDiaToMeses()
        
        
        except(ValueError):
            print("\n\n\n Digite apenas números\n\n\n\n\n\n")
            return Chamamento()
  
            
def DefinaMesesAno():
    Flag = False
    while not Flag:
        try:
        
            mesesT = int(input(" Digite a quantidade de meses\n"))
            
            ano = (mesesT/12)
            mesesRest = mesesT%12
            
            anos = int(ano)
            meses = int(mesesT)
            
            print (" Valor em {} anos e {} meses ".format(anos,meses))
            Flag = True
           
            print("____________________________________________________")
            print ("\n\n\n\n\n")
            return DefinaMesesAno()
        
        
        except(ValueError):
            print("\n\n\n Digite apenas números\n\n\n\n\n\n")
            return Chamamento()
            
            
def DefinaAnoToMeses():
    Flag = False
    while not Flag:
        try:
        
            anosT = int(input(" Digite a quantidade de anos\n"))
            
            mes = int(anosT*12)
           
            
            print (" Valor {} meses ".format(int(mes)))
            Flag = True
            
            
            print("____________________________________________________")
            print ("\n\n\n\n\n")
            return DefinaAnoToMeses()
        
        
        except(ValueError):
            print("\n\n\n Digite apenas números\n\n\n\n\n\n")
            return Chamamento()
            
            
            
def DefinaAnoToDias():
    Flag = False
    while not Flag:
        try:
        
            anosT = int(input(" Digite a quantidade de anos\n"))
            
            dia = int(anosT*12*30.396473)
           
            
            print (" Valor {} dias ".format(int(dia)))
            Flag = True
            
            
            print("____________________________________________________")
            print ("\n\n\n\n\n")
            return DefinaAnoToDias()
        
        
        except(ValueError):
            print("\n\n\n Digite apenas números\n\n\n\n\n\n")
            return Chamamento()
            


def DefinaAnoToHoras():
    Flag = False
    while not Flag:
        try:
        
            anosT = int(input(" Digite a quantidade de anos\n"))
            
            hora = int(anosT*12*30.396473*24)
           
            
            print (" Valor {} horas ".format(int(hora)))
            Flag = True
            
            
            print("____________________________________________________")
            print ("\n\n\n\n\n")
            return DefinaAnoToHoras()
        
        
        except(ValueError):
            print("\n\n\n Digite apenas números\n\n\n\n\n\n")
            return Chamamento()
            


def DefinaAnoToMin():
    Flag = False
    while not Flag:
        try:
        
            anosT = int(input(" Digite a quantidade de anos\n"))
            
            minute = int(anosT*12*30.396473*24*60)
           
            
            print (" Valor {} minutos ".format(int(minute)))
            Flag = True
            
            
            print("____________________________________________________")
            print ("\n\n\n\n\n")
            return DefinaAnoToMin()
        
        
        except(ValueError):
            print("\n\n\n Digite apenas números\n\n\n\n\n\n")
            return Chamamento()


            
def DefinaAnoToSegs():
    Flag = False
    while not Flag:
        try:
        
            anosT = int(input(" Digite a quantidade de anos\n"))
            
            segs = int(anosT*12*30.396473*24*60*60)
           
            
            print (" Valor {} segundos ".format(int(segs)))
            Flag = True
            
            
            print("____________________________________________________")
            print ("\n\n\n\n\n")
            return DefinaAnoToSegs()
        
        
        except(ValueError):
            print("\n\n\n Digite apenas números\n\n\n\n\n\n")
            return Chamamento()
            
            
            
def DefinaMesToDias():
    Flag = False
    while not Flag:
        try:
        
            mesesT = int(input(" Digite a quantidade de meses\n"))
            
            dias = int(mesesT*30.396473)
           
            print (" Valor {} dias ".format(int(dias)))
            Flag = True
            
            
            print("____________________________________________________")
            print ("\n\n\n\n\n")
            return DefinaMesToDias()
        
        
        except(ValueError):
            print("\n\n\n Digite apenas números\n\n\n\n\n\n")
            return Chamamento()
            
            
            
def DefinaMesToHoras():
    Flag = False
    while not Flag:
        try:
        
            mesesT = int(input(" Digite a quantidade de meses\n"))
            
            horas = int(mesesT*30.396473*24)
           
            print (" Valor {} horas ".format(int(horas)))
            Flag = True
            
            
            print("____________________________________________________")
            print ("\n\n\n\n\n")
            return DefinaMesToHoras()
        
        
        except(ValueError):
            print("\n\n\n Digite apenas números\n\n\n\n\n\n")
            return Chamamento()

            
def DefinaMesToMin():
    Flag = False
    while not Flag:
        try:
        
            mesesT = int(input(" Digite a quantidade de meses\n"))
            
            minutes = int(mesesT*30.396473*24*60)
           
            print (" Valor {} minutos ".format(int(minutes)))
            Flag = True
            
            
            print("____________________________________________________")
            print ("\n\n\n\n\n")
            return DefinaMesToMin()
        
        
        except(ValueError):
            print("\n\n\n Digite apenas números\n\n\n\n\n\n")
            return Chamamento()
            

def DefinaMesToSegs():
    Flag = False
    while not Flag:
        try:
        
            mesesT = int(input(" Digite a quantidade de meses\n"))
            
            segs = int(mesesT*30.396473*24*60*60)
           
            print (" Valor {} segundos ".format(int(segs)))
            Flag = True
            print("____________________________________________________")
            print ("\n\n\n\n\n")
            return DefinaMesToSegs()
        
        
        except(ValueError):
            print("\n\n\n Digite apenas números\n\n\n\n\n\n")
            return Chamamento()
     
            
def DefinaDiaToHoras():
    Flag = False
    while not Flag:
        try:
        
            diasT = int(input(" Digite a quantidade de dias\n"))
            
            horas = int(diasT*24)
           
            print (" Valor {} horas ".format(int(horas)))
            Flag = True
            print("____________________________________________________")
            print ("\n\n\n\n\n")
            return DefinaDiaToHoras()
        
        
        except(ValueError):
            print("\n\n\n Digite apenas números\n\n\n\n\n\n")
            return Chamamento()
            


def DefinaDiaToMinutes():
    Flag = False
    while not Flag:
        try:
        
            diasT = int(input(" Digite a quantidade de dias\n"))
            
            minutes = int(diasT*24*60)
           
            print (" Valor {} minutos ".format(int(minutes)))
            Flag = True
            print("____________________________________________________")
            print ("\n\n\n\n\n")
            return DefinaDiaToMinutes()
        
        
        except(ValueError):
            print("\n\n\n Digite apenas números\n\n\n\n\n\n")
            return Chamamento()



def DefinaDiaToSegundos():
    Flag = False
    while not Flag:
        try:
        
            diasT = int(input(" Digite a quantidade de dias\n"))
            
            segundos = int(diasT*24*60*60)
           
            print (" Valor {} segundos ".format(int(segundos)))
            Flag = True
            print("____________________________________________________")
            print ("\n\n\n\n\n")
            return DefinaDiaToSegundos()
        
        
        except(ValueError):
            print("\n\n\n Digite apenas números\n\n\n\n\n\n")
            return Chamamento()
      
      
            
def DefinaHorasToMinutes():
    Flag = False
    while not Flag:
        try:
        
            horasT = int(input(" Digite a quantidade de horas\n"))
            
            minutos = int(horasT*60)
           
            print (" Valor {} minutos ".format(int(minutos)))
            Flag = True
            print("____________________________________________________")
            print ("\n\n\n\n\n")
            return DefinaHorasToMinutes()
        
        
        except(ValueError):
            print("\n\n\n Digite apenas números\n\n\n\n\n\n")
            return Chamamento()
            

def DefinaHorasToSegundos():
    Flag = False
    while not Flag:
        try:
        
            horasT = int(input(" Digite a quantidade de horas\n"))
            
            segundos = int(horasT*60*60)
           
            print (" Valor {} segundos ".format(int(segundos)))
            Flag = True
            print("____________________________________________________")
            print ("\n\n\n\n\n")
            return DefinaHorasToSegundos()
        
        
        except(ValueError):
            print("\n\n\n Digite apenas números\n\n\n\n\n\n")
            return Chamamento()
            

def DefinaMinToSegundos():
    Flag = False
    while not Flag:
        try:
        
            horasT = int(input(" Digite a quantidade de minutos\n"))
            
            segundos = int(horasT*60)
           
            print (" Valor {} segundos ".format(int(segundos)))
            Flag = True
            print("____________________________________________________")
            print ("\n\n\n\n\n")
            
            return DefinaMinToSegundos()
        
        
        except(ValueError):
            print("\n\n\n Digite apenas números\n\n\n\n\n\n")
            
            return Chamamento()

def Chamamento():
    
    Flag = False
    while not Flag:
        try:
            
        
            print("  Guia:\n")
            
            print("-- Ordem Crescente--\n")
            
            print("________________________")

            print("\n\n 1 - Segundos -> Ano")

            print ("\n\n 2 - Segundos -> Mês\n\n")

            print(" 3 - Segundos -> Dias\n\n") 

            print(" 4 - Segundos -> Horas\n\n")

            print(" 5 - Segundos -> Minutos\n\n")

            print(" 6 - Minutos -> Horas\n\n")

            print(" 7 - Minutos -> Dias\n\n")

            print(" 8 - Minutos -> Meses\n\n")

            print(" 9 - Minutos -> Ano\n\n")

            print(" 10 - Horas -> Dias\n\n")

            print(" 11 - Horas -> Meses\n\n")

            print(" 12 - Horas -> Anos\n\n")

            print(" 13 - Dias -> Anos\n\n")

            print(" 14 - Dias -> Meses\n\n")

            print(" 15 - Meses -> Anos\n\n")
            
            print("-- Ordem Decrescente--\n")
            
            print("________________________")

            print("\n\n 16 - Anos -> Meses\n\n")

            print(" 17 - Anos -> Dias\n\n")

            print(" 18 - Anos -> Horas\n\n")

            print(" 19 - Anos -> Minutos\n\n")

            print(" 20 - Anos -> Segundos\n\n")

            print(" 21 - Meses -> Dias\n\n")

            print(" 22 - Meses -> Horas\n\n")

            print(" 23 - Meses -> Minutos\n\n")

            print(" 24 - Meses -> Segundos\n\n")

            print(" 25 - Dias -> Horas\n\n")

            print(" 26 - Dias -> Minutos\n\n")

            print(" 27 - Dias -> Segundos\n\n")

            print(" 28 - Horas -> Minutos\n\n")

            print(" 29 - Horas -> Segundos\n\n")

            print(" 30 - Minutos -> Segundos\n\n")
            
            print(" Após ingressar em um conversor, para retornar ao início basta digitar qualquer letra\n\n")

            print("_____________________________\n\n\n\n\n")
            
            Flag = True
 
            t = int(input(" Digite o conversor escolhido\n"))

            if (t==1):
                print("\n\n\n\n\n")
                DefinaAno()

            elif (t == 2):
                print("\n\n\n\n\n")
                DefinaMes()
    
            elif (t == 3):
                print("\n\n\n\n\n")
                DefinaDia()

            elif (t == 4):
                print("\n\n\n\n\n")
                DefinaHoras()
    
            elif (t == 5):
                print("\n\n\n\n\n")
                DefinaSegsMin()
    
    
            elif (t == 6):
                print("\n\n\n\n\n")
                DefinaMin()

            elif (t == 7):
                print("\n\n\n\n\n")
                DefinaMinD()
    
            elif (t == 8):
                print("\n\n\n\n\n")
                DefinaMinM()
    
            elif (t == 9):
                print("\n\n\n\n\n")
                DefinaMinA()

            elif (t == 10):
                print("\n\n\n\n\n")
                DefinaHoraDia()
    
            elif (t == 11):
                print("\n\n\n\n\n")
                DefinaHoraMes()
    
            elif (t == 12):
                print("\n\n\n\n\n")
                DefinaHoraAno()
    
            elif (t == 13):
                print("\n\n\n\n\n")
                DefinaDiaToAnos()
    
            elif (t == 14):
                print("\n\n\n\n\n")
                DefinaDiaToMeses()
    
            elif (t == 15):
                print("\n\n\n\n\n")
                DefinaMesesAno()
    
            elif (t == 16):
                print("\n\n\n\n\n")
                DefinaAnoToMeses()
    
            elif (t == 17):
                print("\n\n\n\n\n")
                DefinaAnoToDias()
    
            elif (t == 18):
                print("\n\n\n\n\n")
                DefinaAnoToHoras()
    
            elif (t == 19):
                print("\n\n\n\n\n")
                DefinaAnoToMin()
    
            elif (t == 20):
                print("\n\n\n\n\n")
                DefinaAnoToSegs()
    
            elif (t == 21):
                print("\n\n\n\n\n")
                DefinaMesToDias()
    
            elif (t == 22):
                print("\n\n\n\n\n")
                DefinaMesToHoras()
    
            elif (t == 23):
                print("\n\n\n\n\n")
                DefinaMesToMin()
    
            elif (t == 24):
                print("\n\n\n\n\n")
                DefinaMesToSegs()
    
            elif (t == 25):
                print("\n\n\n\n\n")
                DefinaDiaToHoras()
    
            elif (t == 26):
                print("\n\n\n\n\n")
                DefinaDiaToMinutes()
    
            elif (t == 27):
                print("\n\n\n\n\n")
                DefinaDiaToSegundos()
    
            elif (t == 28):
                print("\n\n\n\n\n")
                DefinaHorasToMinutes()
    
            elif (t == 29):
                print("\n\n\n\n\n")
                DefinaHorasToSegundos()
    
            elif (t == 30):
                print("\n\n\n\n\n")
                DefinaMinToSegundos()
    
            else:
                print("\n\n\n\n\n Digite um conversor válido\n\n\n\n\n\n\n\n\n")
                
                return Chamamento()
                        
        
        except(ValueError):
            print("\n\n\n Digite apenas números\n\n\n\n\n\n\n\n\n\n")
            return Chamamento()
            

Chamamento()
