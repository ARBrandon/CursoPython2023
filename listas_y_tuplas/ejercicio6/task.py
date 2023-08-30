# Crear una lista con el abecedario
abecedario = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "ñ", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

# Eliminar las letras que ocupen posiciones múltiplos de 3
for i in range(len(abecedario)-1, -1, -1): # Recorrer la lista al revés
  if (i+1) % 3 == 0: # Si la posición es múltiplo de 3
    abecedario.pop(i) # Eliminar la letra

# Mostrar la lista resultante
print(abecedario)
