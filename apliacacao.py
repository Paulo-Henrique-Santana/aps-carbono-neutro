import math

# nome = input('Nome da empresa: ')
ano = int(input('Ano inventariado: '))
# qtdCarros = int(input('Quantidade de carros da frota: '))
kmPorLitro = float(input('Média de km/litro dos carros da frota: '))
opcao = ''
kmRodados = 0.0

while opcao != 'mes' and opcao != 'mês' and opcao != 'ano':
    opcao = input(
        'Inserir a quantidade total de kilômetros rodados pelos carros da frota por mês ou no ano? ').lower()

    if opcao == 'mes' or opcao == 'mês':
        for i in range(1, 13):
            if i == 1:
                kmRodados += float(input('Janeiro(km): '))
            elif i == 2:
                kmRodados += float(input('Fevereiro(km): '))
            elif i == 3:
                kmRodados += float(input('Março(km): '))
            elif i == 4:
                kmRodados += float(input('Abril(km): '))
            elif i == 5:
                kmRodados += float(input('Maio(km): '))
            elif i == 6:
                kmRodados += float(input('Junho(km): '))
            elif i == 7:
                kmRodados += float(input('Julho(km): '))
            elif i == 8:
                kmRodados += float(input('Agosto(km): '))
            elif i == 9:
                kmRodados += float(input('Setembro(km): '))
            elif i == 10:
                kmRodados += float(input('Outubro(km): '))
            elif i == 11:
                kmRodados += float(input('Novembro(km): '))
            elif i == 12:
                kmRodados += float(input('Dezembro(km): '))
    elif opcao == 'ano':
        kmRodados = float(input(f'{ano}(km): '))
    else:
        print('Opção Inválida!')

valorCredito = float(input('Informe o valor atual do crédito de carbono em R$: '))

def calcularLitrosGastos():
    return kmRodados / kmPorLitro

def calcularCarbonoEmitido():
    return calcularLitrosGastos() * 0.82 * 0.75 * 3.7

def calcularCompensacao():
    return math.ceil(calcularCarbonoEmitido() / 1000 * 7)

def calcularCredito():
    return math.floor(calcularCarbonoEmitido() / 1000)

def calcularLucroCredito():
    return calcularCredito() * valorCredito

def formatarValor(valor):
    return str(round(valor, 2)).replace('.',',')

litrosGastos = formatarValor(calcularLitrosGastos())
kgCarbonoEmitido = formatarValor(calcularCarbonoEmitido())
qtdArvoresCompensacao = calcularCompensacao()
lucroCredito = formatarValor(calcularLucroCredito())

print()
print(f'Consumo de gasolina em {ano}: {litrosGastos} litros')
print(f'Carbono emitido: {kgCarbonoEmitido} kg CO₂')
print(f'Nº de Árvores necessárias para compensar a emissão de {kgCarbonoEmitido} kg CO₂ ao longo de 20 anos: {qtdArvoresCompensacao}')
print(f'Créditos de carbono ganhos com a neutralização R$: {lucroCredito}')