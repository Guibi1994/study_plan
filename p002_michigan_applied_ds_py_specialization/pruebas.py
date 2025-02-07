# 0. Ejercicios prácticos

alist = [1, 2, 4, 8, 16, 32, 64]

## 0.1. Ejercicios con MAP:

### 0.1.1. Devuelve el valor más "a"
# Map no edita el valor original de la lista
list(map(lambda x: str(x) + "a", alist))

### 0.1.2. Devuleve el indice del valor dentro de una lista


def return_letter(x: int) -> str:
    letters = "abcdef"
    try:
        return letters[x]
    except IndexError:
        return "sin letra"


list(map(return_letter, alist))

### 0.1.3. Devuelve la misma aleatoriamente negativa o positivamente
from random import choice

list(map(lambda x: x * choice([-1, 1]), alist))

### 0.1.4. Convierte cada elemento en una lista junto a su valo cuadrático
list(map(lambda x: [x, x**2], alist))

### 0.1.5. Cada objeto en un diccionario con su valor negativo aleatori y su cuadrado y raiz
from math import sqrt

list(
    map(
        lambda x: {
            "valor": x * choice([-1, 1]),
            "cuadrado": x**2,
            "cuadratico medio": sqrt(x**2),
        },
        alist,
    )
)

## 0.2. Ejercicios con list comprehension
1 + 1


# 1.
import numpy as np

data = np.array(
    [
        # Variabl 1
        [1, 2, 3],
        # Variable 2
        [2, "", 2],
    ]
)

data[:, 0] = 2
data
