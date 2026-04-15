lado1 = float(input("Digite o lado 1: "))
lado2 = float(input("Digite o lado 2: "))
lado3 = float(input("Digite o lado 3: "))

lados = sorted([lado1, lado2, lado3])
a, b, c = lados  # a is smallest, c is largest

if a + b <= c:
    print("NAO FORMA TRIANGULO")
else:
    if c**2 == a**2 + b**2:
        print("TRIANGULO RETANGULO")
    elif c**2 > a**2 + b**2:
            print("TRIANGULO OBTUSANGULO")
    else:
        print("TRIANGULO ACUTANGULO")

    if a == b == c:
        print("TRIANGULO EQUILATERO")
    elif a == b or b == c or a == c:
        print("TRIANGULO ISOSCELES")
