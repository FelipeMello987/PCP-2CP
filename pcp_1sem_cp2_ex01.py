codigo_estado = int(float(input("Digite o codigo do estado de origem: ")))
peso = float(input("Digite o peso do caminhao em toneladas: "))
codigo_carga = int(float(input("Digite o codigo da carga: ")))

if codigo_estado < 1:
    codigo_estado = 1
elif codigo_estado > 5:
    codigo_estado = 5

if codigo_carga < 10:
    codigo_carga = 10
elif codigo_carga > 40:
    codigo_carga = 40

pesokg = peso*1000
preco = 0
imposto = 0

if 10 <= codigo_carga <= 20:
    preco = pesokg*100
elif 21 <= codigo_carga <= 30:
    preco = pesokg*250
elif 31 <= codigo_carga <= 40:
    preco = pesokg*340

if codigo_estado == 1:
    imposto = 35
elif codigo_estado == 2:
    imposto = 25
elif codigo_estado == 3:
    imposto = 15
elif codigo_estado == 4:
    imposto = 5
elif codigo_estado == 5:
    imposto = "isento"

valor_final = preco - (preco * (imposto/100))

print(f"peso em quilos: {pesokg}kg")
print(f"preco da carga:  R${preco}")
print(f"imposto:  {imposto}%")
print(f"valor do imposto: R${preco * (imposto/100)}")
print(f"valor apos pagamento do imposto: R${valor_final}")