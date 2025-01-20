# -----------------------------------------------------
# 1. String methods
# -----------------------------------------------------

## 1.1. Spliting
"Hola".split("l")

## 1.2. Counting
"Hola".count("a")

## 1.3. Indexing
"Hola".index("a")
"Hola"[3]


# -----------------------------------------------------
# 2. Listas
# -----------------------------------------------------


## 2.1 Crear listas com list()
# List crea listas separando cada elemento elemento como un
#   elemento individual de la lista
list()

## 2.1. Crear lista con "[]"
# "[]" Esto crea una lista con un eleménto unico definido, o con los
#   elementos que se definan en ella.
[]

## 2.3. Diferencias:

# La diferencia principal se ve en los strings:
list("hola")  # Cada letra es un elemento
["hola"]  # "hola" es el unico elemento

# En los números con range esto es util, pues cada elemento del rango
#   es un elemento de la lista
list(range(1, 11))


# -----------------------------------------------------
# 3. Expresiones boolenadas
# -----------------------------------------------------


## 3.1. Literales
True
False

## 3.2. Logical
2 in ([2, 3, 4] or [1, 4, 5])
2 in ([2, 3, 4] and [1, 4, 5])

not True
not False

## 3.3. Comparision
2 != 2
2 == 2
2 >= 0
2 <= 2
2 > 2
2 < 2

## 3.4. Assert
#   Genera un error cuando una expresión es falsa
assert 2 < 0


# 4. Conditional execution


def mi_funcion(x):
    # Agregar un supuesto funcional
    assert isinstance(x, (int, float))
    if x > 0:
        print(str(x) + " es positivo")
    elif x < 0:
        print(str(x) + " es negativo")
    elif x == 0:
        print(str(x) + " es cero")
    else:
        print(str(x), "no es un número")


mi_funcion("-0")


# -----------------------------------------------------
# 5. Mutabilidad e inmutabilidad en LISTAS
# -----------------------------------------------------


## 5.1. Las listas son mutables
#   Nota: las variables referencian objetos pero no son objetos
#   esto implica que b=a, entonces b y a serán referencias al mismo
#   objeto que se puede editar tanto cambiando a como b. Ahora, este
#   nuevo objeto tendrá dos formas de referenciarse: "a" y "b" .

a = [1, 2, 3]
a[0]

b = a
b[0] = "Hola"

a
b

a[0] = "superduper"
b

## 5.2. Slicing como método de mutación de listas

### 5.2.1. Eliminar por asignación vacia
a = list(range(1, 11))
print(a)
a[1:-1] = []
print(a)

### 5.2.2. Insertar
# Remplazamos el 1er elemento por "a"
a = list(range(1, 11))
print(a)
a[0] = "a"
print(a)

# Tambien se puede insertar toda una lista alargando la 1ra
b = [0, 0, 0]
a[1:1] = b
print(a)

### 5.2.3. Eliminar con del
del a[:5]
print(a)

### 5.2.3. Clonación (ver nota 1)
a = [1, 2, 3, 4]
b = a[:]  # Se puede hacer con "a[:]"
b = a * 1  # o tambien con "a*1"

print(a is b)
print("id_a = " + str(id(a)) + " | id_b = " + str(id(b)))


## 5.3. Otros métodos con listas
a = [3, 2, 12, 4, 25, 23, 12]

### 5.3.1. Agregar elementos al final de la lista
a.append(2)
a += ["1"]

### 5.3.2. Eliminar elementos al final de la lista
a.pop()

### 5.3.3. Reordenar
a.sort()

### 5.3.4. Eliminar por valor (no por posición)
a.remove(12)

### 5.3.5. Insertar en medio de una lista (sin remplazo)
a.insert(2, "s10")


# -----------------------------------------------------
# 6. Mutabilidad en lista
# -----------------------------------------------------


#### NOTAS #####

# NOTA 1:

"=="  # Marca si el contenido es igual
"is"  # Marca si son el mismo objeto en memoria

## Mismo objeto
a = [1, 2, 3]
b = a
a is b
print("id_a = " + str(id(a)) + " | id_b = " + str(id(b)))

# Mismo contenido
a = [1, 2, 3]
b = [1, 2, 3]
a is b
a == b
print("id_a = " + str(id(a)) + " | id_b = " + str(id(b)))
