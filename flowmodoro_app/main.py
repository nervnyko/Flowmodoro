from timer_logic import FlowmodoroTimer
import time
from datetime import timedelta


logica = FlowmodoroTimer()

print("--- FLOWMODORO DE TERMINAL ---")

input ("Pressione ENTER para começar o seu Flooooooow...")

logica.start()

input ("Pressione ENTER para encerrar o seu FloOooOOOow...")

logica.stop()

tempo_pausa = logica.get_pause()
print(f"Seu tempo de pausa merecido: {str(timedelta(seconds=tempo_pausa))}")