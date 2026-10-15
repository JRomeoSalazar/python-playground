contador = 0

while contador < 3:
    print(f"El contador es: {contador}")
    contador += 1

for i in range(3):
    print(f"Ahora i vale: {i}")

for i in range(1, 6):
    if i%2 != 0:
        continue
    
    print(f"{i} es un número par")