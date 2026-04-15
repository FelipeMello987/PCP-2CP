#solicitando as notas
cp1 = float(input("A nota do checkpoint 1 é: "))
cp2 = float(input("A nota do checkpoint 2 é: "))
cp3 = float(input("A nota do checkpoint 3 é: "))
sprint1 = float(input("A nota do sprint 1 é: "))
sprint2 = float(input("A nota do sprint 2 é: "))
globals = float(input("A nota do global solutions é: "))

#limitando para não ser maior que 10 nem menor que 0
notas = [cp1, cp2, cp3, sprint1, sprint2, globals]
notas_corrigidas = []
for nota in notas:
    if nota > 10:
        nota = 10
    elif nota < 0:
        nota = 0
    notas_corrigidas.append(nota)
cp1, cp2, cp3, sprint1, sprint2, globals = notas_corrigidas


#escolhendo as 2 maiores notas de CP
notas_cp = [cp1, cp2, cp3]
menor = notas_cp[0]
if notas_cp[1] < menor:
    menor = notas_cp[1]
if notas_cp[2] < menor:
    menor = notas_cp[2]
notas_cp.remove(menor)
maior1, maior2 = notas_cp


media_cp = sum(notas_cp)/2

media_final = ((maior1 + maior2 + sprint1 + sprint2)/4)*0.4 + globals*0.6

print(f"media com peso é: {media_final*0.4:.1f}")
print(f"media sem peso é: {media_final:.1f}")