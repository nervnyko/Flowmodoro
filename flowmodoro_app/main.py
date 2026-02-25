from timer_logic import Flow_PersoTiming, Flow_DefTiming
import time
from datetime import timedelta


logica = Flow_PersoTiming()

print("--- FLOWMODORO DE TERMINAL ---")

print("Selecione o tipo de Flowmodoro que deseja: \n1 - Sessões personalizadas.\n2 - Sessão definida.")

Flow_type = input ("")

if Flow_type == "1":
    input ("Pressione ENTER para começar o seu Flooooooow...")

    logica.start()

    input ("Pressione ENTER para encerrar o seu FloOooOOOow...")

    logica.stop()

    tempo_pausa = logica.get_pause()
    print(f"Seu tempo de pausa merecido: {str(timedelta(minutes=tempo_pausa))}")
    
elif Flow_type == "2":
    timertotal = input ("Digite o número de HORAS que você tem disponível para o foco: (Formato: XX.X)")
    
