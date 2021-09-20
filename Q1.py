from numpy import var, mean
from math import sqrt
from scipy.stats import mode
from functools import reduce

print('Questão 1')
print('Considere uma tabela de frequência para variável discreta. Calcule média, averagfea, moda, variância, desvio padrão e coeficiente de variação.')

# (a, b, v); a=min do intervalo; b=max do intervalo; v=freq. abs.
dataset = {  # classe: (Freq Abs, Freq. Rel.)
    2: (2, 0.1),
    5: (4, 0.2),
    6: (5, 0.25),
    8: (6, 0.3),
    9: (3, 0.15)
}

freqAbsAcc = 20


def variance(d, media):
    equations = list(
        map(lambda x: ((x ** 2) * d[x][0]) / freqAbsAcc, d.keys()))
    somatory = reduce(lambda a, b: a + b, equations)
    return somatory - (media ** 2)
#     freqValues = list(map(lambda x: x[0], d.values()))
#     nObservations = len(freqValues)
#     mediaArit = reduce(lambda a, b: a+b, freqValues) / nObservations
#     elements = list(map(lambda x: (x - mediaArit) ** 2, freqValues))
#     somatory = reduce(lambda a, b: a+b, elements)
#     return somatory / nObservations


classSpacing = 12
frequencySpacing = 12

freqTimes = list(map(lambda x: x * dataset[x][0], dataset.keys()))
totalSum = reduce(lambda a, b: a+b, freqTimes)

media = round(totalSum / freqAbsAcc, 2)
print(f'Media = {media}')

values = list(map(lambda x: x[0], list(dataset.values())))

mediana = mean(values)

print(f'Mediana = {mediana}')

spreadedValues = []

for key in dataset:
    times = dataset[key][0]
    for i in range(0, times - 1):
        spreadedValues.append(key)

modeResult = mode(spreadedValues)
moda = modeResult.mode[0]
modaFrequencia = modeResult.count[0]

print(f'Moda = {moda}, aparecendo {modaFrequencia} vezes')

variancia = variance(dataset, media)

print(f'Variancia = {variancia}')

desvioPad = sqrt(variancia)

print(f'Desvio Padrão = {desvioPad}')

print(f'Coeficiente de Variação = {desvioPad / media}')
