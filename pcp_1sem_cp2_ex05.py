def informaçãoes_do_usuario():
    nome = input("Digite seu nome: ")
    idade = int(input("Digite sua idade: "))
    renda = float(input("Digite sua renda mensal: "))
    valor_emprestimo = float(input("Digite o valor do empréstimo: "))
    num_parcelas = int(input("Digite o número de parcelas: "))
    return nome, idade, renda, valor_emprestimo, num_parcelas

nome, idade, renda, valor_emprestimo, num_parcelas = informaçãoes_do_usuario()

def verificar_emprestimo(nome, idade, renda, valor_emprestimo):
    if idade < 18:
        print("Empréstimo negado. Idade mínima é 18 anos.")
    elif valor_emprestimo > 20 * renda:
        print("Empréstimo negado. O valor do financiamento deve ser no máximo 20 vezes maior que o valor da renda.")
    else:
        print(f"{nome}, seu empréstimo foi aprovado.")

verificar_emprestimo(nome, idade, renda, valor_emprestimo)

'''
valor dos empréstimos:
- Até 6 parcelas: 5% de juros
- De 7 a 12 parcelas: 8% de juros
- De 13 a 24 parcelas: 10% de juros
'''

def calcular_financiamento(valor_emprestimo, num_parcelas):
    if num_parcelas <= 6:
        juros = valor_emprestimo * 0.05
    elif num_parcelas <= 12:
        juros = valor_emprestimo * 0.08
    else:
        juros = valor_emprestimo * 0.10

    print(f"Valor dos juros: R$ {juros:.2f}")
    return juros

def calcular_parcela(valor_emprestimo, valor_financiamento, num_parcelas):
    valor_total = valor_emprestimo + valor_financiamento
    value_parcela = valor_total / num_parcelas
    print(f"Valor de cada parcela: R$ {value_parcela:.2f}")
    print(f"valor total pago: R$ {valor_total:.2f}")
    print(f"total de juros pagos: R$ {valor_financiamento:.2f}")

valor_financiamento = calcular_financiamento(valor_emprestimo, num_parcelas)
calcular_parcela(valor_emprestimo, valor_financiamento, num_parcelas)

'''
saida do programa:
Digite seu nome: João
Digite sua idade: 25
Digite sua renda mensal: 3000
Digite o valor do empréstimo: 15000
Digite o número de parcelas: 12

Empréstimo aprovado.
Valor total do empréstimo: R$ 16200.00
Valor do financiamento: R$ 1200.00
valor dos juros aplicados: R$ 1200.00
Valor de cada parcela: R$ 1350.00
valor total pago: R$ 16200.00
total de juros pagos: R$ 1200.00
'''