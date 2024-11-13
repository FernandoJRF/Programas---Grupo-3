#Este Programa es para hacer un sorteo 

import random

#lista de participantes
participants = ["Jenni", "Fernando_Jose", "Alex", "Danna", "Jose", "Ovalle", "Karina"]

# elegir un ganador al azar
winner = random.choice(participants)
print(f"El ganador del sorteo es: {winner}")


