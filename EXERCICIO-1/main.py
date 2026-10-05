import conversor

print("=== Conversor de medidas ===")

origem = input("Digite a unidade de origem (pe, metro ou jarda): ").lower()
valor = float(input("Digite o valor: "))
destino = input("Digite a unidade de destino (pe, metro ou jarda): ").lower()

resultado = conversor.converter(valor, origem, destino)

if resultado == None:
    print("Unidade inválida!")
else:
    print("Resultado:", round(resultado, 4))