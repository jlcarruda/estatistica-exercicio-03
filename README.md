# Exercicio 03 - João Lucas de Carvalho Arruda
Desenvolvi todas as soluções do exercicio utilizando Python, com as seguintes dependencias:
- Python 3.9
- Scipy

**As soluções estão compiladas neste README, não necessitando ser feita a execução do código.**

## Como Executar (opcional)
As soluçöes estão separadas por arquivo, onde `Q1.py` se refere as resoluções da Questão 1, e assim por diante.

Para executar o código, se faz necessário apenas a instalação das dependencias e a execução de cada arquivo via terminal
```shell
> pip install -U scipy # Instalar a dependencia

> python ./Q1.py
```

----------

## [Questão 1](./Q1.py)
### Considere uma tabela de frequência para variável discreta:
| xi |   Freq. Abs. |   Freq. Rel. |
|:---- | :----: | ----: |
2   | 2 |    0.1
5   |   4 |   0.2
6  |   4 |   0.25
8 |   6 |   0.3
9 |   3 |   0.15

## Calcule média, mediana, moda, variância, desvio padrão e coeficiente de variação.
***Os calculos desta questão foram feitos via Python***

| Variavel Calculada| Valor |
|:--|---:|
Media | 6.45
Mediana | 4.0
Moda | 8, aparecendo 5 vezes
Variancia | 2
Desvio Padrão | 1.4142135623730951
Coeficiente de Var. | 0.3536
----------

## [Questão 2](./Q2.py)
### Considere uma tabela de frequência para variável contínua:
| Classes |   Freq. Abs. |   Freq. Abs. Acumulada | Freq. Rel | Freq. Rel. Acumulada |
|:---- | :----: | :----: | :----: |   ----: |
20 \|-- 21,8   | 3 |    3 | 0,15 | 0,15
21,8 \|-- 23,6   |   6 |  9| 0,30| 0,45
23,6 \|-- 25,4  |   7 |   16| 0,35 | 0,80
25,4 \|-- 27,2 |   3 |  19| 0,15 | 0,95
27,2 \|-- 29 |   1 |   20| 0,05 | 1,0

## Calcule média, mediana, moda, variância, desvio padrão e coeficiente de variação.

| Variavel Calculada| Valor |
|:--|---:|
Media | 23.87
Mediana | 25.4
Moda | 23.96
Variancia | 1.9113084523436352
Desvio Padrão | 1.3825007965074143
Coeficiente de Var. | 0.05791792193160512
