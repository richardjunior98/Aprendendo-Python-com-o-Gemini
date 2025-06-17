lista_de_compras = ["maçã", "banana", "leite"]
numeros_primos = [2, 3, 5, 7, 11]
lista_vazia = []

print(lista_de_compras[0]) # Saída: "maçã"
print(numeros_primos[2])   # Saída: 5
print(lista_de_compras[-1]) # O índice -1 pega o ÚLTIMO item

lista_de_compras.append("pão") # ["maçã", "banana", "leite", "pão"]
item_removido = lista_de_compras.pop(1) # Remove "banana"
print(f"Item removido: {item_removido}")
print(f"A lista agora tem {len(lista_de_compras)} itens.")

for item in lista_de_compras:
    print(f"- {item}")