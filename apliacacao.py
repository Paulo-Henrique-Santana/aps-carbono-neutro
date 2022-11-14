import math

def calcularLitrosGastos():
    return km_rodados / km_por_litro

def calcularCarbonoEmitido():
    return calcularLitrosGastos() * 0.82 * 0.75 * 3.7

def calcularCompensacao():
    return math.ceil(calcularCarbonoEmitido() / 1000 * 7)

def calcularCredito():
    return math.floor(calcularCarbonoEmitido() / 1000)

def calcularLucroCredito():
    return calcularCredito() * valor_credito

# Retorna o valor com duas casas decimais e subtitui a vírgula por ponto
def formatarValor(valor):
    return str(round(valor, 2)).replace('.', ',')

print('----- PROGRAMA DE CÁLCULO DE EMISSÃO E COMPENSAÇÃO DE CARBONO PARA EMPRESAS DE LOCAÇÃO DE AUTOMÓVEIS -----\n')
empresa = input('Nome da empresa: ')
ano = int(input('Ano inventariado: '))
km_por_litro = float(input('Média de km/litro dos carros da frota: '))
opcao = ''
km_rodados = 0.0

while opcao != 'mes' and opcao != 'mês' and opcao != 'ano':
    opcao = input(
        'Inserir a quantidade total de kilômetros rodados pelos carros da frota por mês ou no ano? ').lower()

    if opcao == 'mes' or opcao == 'mês':
        for i in range(1, 13):
            if i == 1:
                km_rodados += float(input('Janeiro(km): '))
            elif i == 2:
                km_rodados += float(input('Fevereiro(km): '))
            elif i == 3:
                km_rodados += float(input('Março(km): '))
            elif i == 4:
                km_rodados += float(input('Abril(km): '))
            elif i == 5:
                km_rodados += float(input('Maio(km): '))
            elif i == 6:
                km_rodados += float(input('Junho(km): '))
            elif i == 7:
                km_rodados += float(input('Julho(km): '))
            elif i == 8:
                km_rodados += float(input('Agosto(km): '))
            elif i == 9:
                km_rodados += float(input('Setembro(km): '))
            elif i == 10:
                km_rodados += float(input('Outubro(km): '))
            elif i == 11:
                km_rodados += float(input('Novembro(km): '))
            elif i == 12:
                km_rodados += float(input('Dezembro(km): '))
    elif opcao == 'ano':
        km_rodados = float(input(f'{ano}(km): '))
    else:
        print('Opção Inválida!')

valor_credito = float(
    input('Informe o valor atual do crédito de carbono em R$: '))

litros_gastos = formatarValor(calcularLitrosGastos())
kg_carbono_emitido = formatarValor(calcularCarbonoEmitido())
qtd_arvores_compensacao = calcularCompensacao()
lucro_credito = formatarValor(calcularLucroCredito())

resultado = []
resultado.append(f'-------------------- CÁLCULO DA EMPRESA {empresa.upper()} --------------------')
resultado.append(f'Consumo de gasolina em {ano}: {litros_gastos} litros')
resultado.append(f'Carbono emitido: {kg_carbono_emitido} kg CO₂')
resultado.append(f'Nº de Árvores necessárias para compensar a emissão de {kg_carbono_emitido} kg CO₂ ao longo de 20 anos: {qtd_arvores_compensacao}')
resultado.append(f'Créditos de carbono ganhos com a neutralização R$: {lucro_credito}')

arquivo = open(f'./resultado-{empresa}.txt', 'w', encoding='utf-8')

for i in range(0, len(resultado)):
    if i == 0:
        arquivo.write(f'{resultado[i]}\n')
        print(f'\n{resultado[i]}\n')
    else:
        arquivo.write(f'\n{resultado[i]}')
        print(resultado[i])
