



def concat(alist: list) ->str:
    assert isinstance(alist, list), "No es una lista"
    assert all(isinstance(x, str) for x in alist), "No todos son strings"

    concated = ""
    for i in alist:
        concated = concated+i 
    return concated



mi_lista = ["a","b"]
mi_lista.sort(reverse=True)
print(mi_lista)


mi_lista[0] = "s"



# Deep and shallow copies
mi_lista = [1,2,3,4]

nueva_lista  =Ñ[]