#interface

nome_funcionario = input('Digite o nome do funcionario: ')

while True:
    print('Escolha o cargo: \n')
    print('1 - Gerente')
    print('2 - Analista')
    print('3 - Assistente')
    print('4 - Estagiario')

    try:
        cargo_funcionario = int(input('Digite o numero do funcionario cargo(1 a 4): '))
        if cargo_funcionario in [1, 2, 3, 4]:
            break
        else:
            print('Opcao invalida apenas sao aceitos numero de 1 a 4 ')
    except ValueError:
            print('Caractere invalido')

salario_base = float(input('Digite o Salario Base: '))
horas_extras = float(input('Digite a quantidade de horas extras: '))
faltas = int(input('Faltas Totais: '))
bonus_recebido = input('Bonus Recebido(Sim ou Nao): ')


#definir variaveis

def calcular_horas_extras(salario_base, horas_extras):
    valor_hora_extra = salario_base * 0.015
    return valor_hora_extra * horas_extras

def calcular_descontos_faltas(salario_base, faltas):
    desconto_por_falta = salario_base * 0.02
    return desconto_por_falta * faltas

def calcular_bonus(cargo_funcionario, bonus_recebido):
    if bonus_recebido.lower() != 'Sim':
        return 0

    if cargo_funcionario == 1:
        return 1000
    elif cargo_funcionario == 2:
        return 500
    elif cargo_funcionario == 3:
        return 300
    elif cargo_funcionario == 4:
        return 100

    return 0

#calculos

valor_horas_extras = calcular_horas_extras(salario_base, horas_extras)
valor_descontos = calcular_descontos_faltas(salario_base, faltas)
valor_bonus = calcular_bonus(cargo_funcionario, bonus_recebido)


salario_bruto = salario_base
total_acrescimos = valor_horas_extras + valor_bonus
total_descontos = valor_descontos
salario_final = salario_bruto + total_acrescimos - total_descontos


#interface para resultados
print("\n Resultado ")
print(f'Funcionario: {nome_funcionario}')
print(f'Salario bruto: R$ {salario_bruto:.3f}')
print(f'Total acrescimos: R$ {total_acrescimos:.2f}')
print(f'Total descontos: R$ {total_descontos}')
print(f'Salario final: R$ {salario_final:.3f}')
