palabra = input("Introduce una palabra:")
vocales = "aeiou"
for vocal in vocales:
  n = palabra.count(vocal)
  if n == 1:
    print(f"La vocal {vocal} aparece {n} veces")
  else:
    print(f"La vocal {vocal} aparece {n} veces")
