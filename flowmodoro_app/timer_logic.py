import time, csv
from datetime import timedelta, date

class Flow_PersoTiming:
    
    #Definindo as variáveis que vou precisar no código
    def __init__(self):
        self.start_time = None
        self.stop_time = None
        self.pause_time = None
        
        #Tempo startou
    def start (self):
        self.start_time = time.time()
        self.stop_time = None
        self.running = True
            
        print (f"Relóginho funcionando desde {self.start_time}")
        
        #Tempo parou
    def stop (self):
        self.stop_time = time.time()
        self.elapsed_time = round(self.stop_time - self.start_time)
        self.running = False
        self.save_session ()
        
        print (f"Relóginho parou de funcionar depois de: {str(timedelta(minutes=self.elapsed_time))}")
    
    def get_pause (self):
            
        self.pause_time = int(self.elapsed_time / 5)
            
        return self.pause_time
    
    def save_session(self):
        
        filename = "flow_history.csv"
        hoje = date.today()
        with open(filename, mode='a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([hoje, self.elapsed_time])
            
class Flow_DefTiming:
    
    #Variáveis iniciais da classe: Tempo total disponível, tempo de cada sessão individual e intervalo entre as sessões
    def __init__(self):
        self.timertotal = None
        self.indsession = None
        self.intervaltime = None
    
    #Classe de tempo total.
    def TotalTime (self):
        self.timertotal = None
        self.indsession = None
        self.intervaltime = None
        
