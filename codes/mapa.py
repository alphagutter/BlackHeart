import matplotlib.pyplot as plt
from matplotlib import colors
import numpy


#matriz original
mapa = [
    ['S', 'K', 'K', ' ', ' ', 'S', 'S', 'S'],
    ['K', 'K', ' ', ' ', ' ', ' ', ' ', 'S'],
    [' ', ' ', 'D', 'D', 'D', ' ', ' ', ' '],
    ['C', ' ', 'D', 'D', 'D', ' ', 'C', ' '],
    ['S', ' ', ' ', ' ', ' ', ' ', 'C', ' '],
    ['S', 'C', 'M', 'M', ' ', ' ', 'M', ' '],
    [' ', ' ', 'M', 'M', ' ', ' ', ' ', 'C'],
    ['M', ' ', ' ', ' ', ' ', ' ', 'M', ' '],
    ['M', ' ', 'M', 'M', ' ', ' ', ' ', ' '],
    ['M', ' ', ' ', ' ', ' ', 'P', ' ', 'M'],
]

colors = numpy.zeros((len(mapa), len(mapa[0])), dtype=int)

char_to_value = {
    'K': 2,
    'C': 3,
    'D': 4,
    'S': 5,
    'M': 6,
    'P': 0,

    ' ': -1
}

for i in range(len(mapa)):
    for j in range(len(mapa[i])):
        if mapa[i][j] in char_to_value:
            colors[i][j] = char_to_value[mapa[i][j]]
        else:
            colors[i][j] = 99

print(colors)


# P = puerta(infinitos objetos pueden estar en ella)    value=0     (black)
# K = cocina(kitchen)                                   value=2     (gray)
# D = Caja(dinero)                                      value=3     (green)
# C = Consola                                           value=4     (aquamarine)
# S = Sofa                                              value=5     (violet)
# M = Mesa                                              value=6     (crimson)

# H = humano                                            value=1
# X = Lugar recorrible                                  value=99    (white)
