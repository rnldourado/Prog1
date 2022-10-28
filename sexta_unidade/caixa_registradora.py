def comissoes(lista):
    comissoes = 0
    for venda in lista:
        if venda < 1000:
            comissoes += 0.05 * venda
        elif 1000 <= venda < 5000:
            comissoes += 0.1 * venda
        elif venda >= 5000:
            comissoes += 0.15 * venda

    return comissoes


def soma(lista):
    soma = 0
    for venda in lista:
        soma += venda
    
    return soma


def caixa_registradora(lista, meta):
    total_comissoes = comissoes(lista)
    total_vendas = soma(lista)

    if total_vendas - total_comissoes < meta: 
        situacao = 'Prejuizo'
    else:
        situacao = 'Lucro'

    return [total_vendas, total_comissoes, situacao]
