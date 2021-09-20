from numpy import mean
from math import sqrt
from functools import reduce

print('Questão 1')
print('Considere uma tabela de frequência para variável contínua. Calcule média, mediana, moda, variância, desvio padrão e coeficiente de variação.')

# (a, b, v, x); a=min do intervalo; b=max do intervalo; v=freq. abs.; x=Freq Rel
dataset = [(20.0, 21.8, 3, 0.15), (21.8, 23.6, 6, 0.3), (23.6, 25.4, 7, 0.35),
           (25.4, 27.2, 3, 0.15), (27.2, 29, 1, 0.05)]

tableIntervalExcludesLast = True

classSpacing = 15
frequencySpacing = 12

table = []

freqAbsAcc = 20


def getFrequencyClass(a, b, v):
    if v >= a and v < b:
        return 1
    return 0


def formatTable(cSpacing, fSpacing):
    return '{:<%d} {:<%d} {:<%d}' % (cSpacing, fSpacing, fSpacing)


def printTable(dataset):
    print(formatTable(classSpacing, frequencySpacing).format(
        "Intervalos", "Freq. Abs.", "Freq. Rel.(%)"))

    for a, b, v, x in dataset:
        table.append((a, b, v, x))
        print(formatTable(classSpacing, frequencySpacing).format(
            f'{a} {"|--" if tableIntervalExcludesLast else "--"} {b if tableIntervalExcludesLast else b - 1}', v, f'{x}'))


def applyCzuber(classeModal, i):
    l = classeModal[0]  # Limite inferior
    d1 = classeModal[2] - dataset[i - 1][2]  # Freq. Modal - Freq. anterior
    d2 = classeModal[2] - dataset[i + 1][2]  # Freq. Modal - Freq. Posterior
    h = classeModal[1] - l  # Amplitude
    return l + (d1 / (d1 + d2)) * h  # CZUBEK


def intervalMiddlePoint(classe):
    v1 = classe[0]
    v2 = classe[1]
    return (v1 + v2) / 2


printTable(dataset)

totalSum = 0
middlePointValues = []

for i in dataset:
    times = i[2]
    middlePoint = intervalMiddlePoint(i)
    totalSum += middlePoint * times
    middlePointValues.append((times, middlePoint))

print()
media = round(totalSum / freqAbsAcc, 2)
print(f'Media = {media}')

# ============= MEDIANA =============
# Pegaremos o indice médio do dataset,depois de feito o calculo dos middle points de cada intervalo
mediana = dataset[round(len(middlePointValues)/2)][1]
print(f'Mediana = {mediana}')

# ============= MODA ===============
# Olhando para o dataset, vemos que a classe modal é a de indice 2
indiceClasseModal = 2
classeModal = dataset[indiceClasseModal]
print(
    f'Moda, aplicando CZUBER = {applyCzuber(classeModal, indiceClasseModal)}')

# ========= VARIANCIA ==============
middlePointValuesWithFrequency = list(
    map(lambda x: (x[0] * x[1]), middlePointValues))
middlePointValuesWithFrequencySquared = list(
    map(lambda x: (x[0] * (x[1] ** 2)), middlePointValues))
sumSquared = reduce(lambda a, b: a+b, middlePointValuesWithFrequencySquared)
sumMiddlePoint = reduce(lambda a, b: a+b, middlePointValuesWithFrequency)

variancia = sqrt((sumSquared / freqAbsAcc) -
                 (sumMiddlePoint / freqAbsAcc) ** 2)
print(f'Variancia = {variancia}')

# ========= DESVIO PADRÃO ===========
print(f'Desvio Padrão = {sqrt(variancia)}')

# ========= Coeficiente de Variação =========
print(f'Coeficiente de Variação = {sqrt(variancia) / media}')
