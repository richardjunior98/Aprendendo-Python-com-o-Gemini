# Exemplo: Imprimir números de 1 a 5
print("Contando até 5:")
for numero in range(1, 6): # O range vai de 1 a 5 (o 6 não é incluído)
    print(numero)
    
print("\nContando até 5 com while:")
contador = 1
while contador <= 5:
    print(contador)
    contador = contador + 1 # ESSENCIAL: Atualizar o contador para não criar um loop infinito