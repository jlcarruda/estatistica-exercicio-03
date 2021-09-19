from numpy import var, mean
from math import sqrt
from scipy.stats import mode

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

table = []

total = 20

classSpacing = 12
frequencySpacing = 12

media = 20 / len(dataset)
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

print(f'Variancia = {var(values)}')

desvioPad = sqrt(var(values))

print(f'Desvio Padrão = {desvioPad}')

print(f'Coeficiente de Variação = {round((desvioPad / media) * 100, 2)}%')
