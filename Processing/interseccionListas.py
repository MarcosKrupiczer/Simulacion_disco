#Funcion que determina la interseccion entre dos listas ingresadas
#En caso de que un elemento pertenezca a las superficies Sq o Sc, se usa esta funcion para determinar cuales son los nodos que pertenecen a
#dichas superficies. De esa forma, se determina el plano del elemento que pertenece a cada superficie.
def intersection(lst1, lst2):
    lst3 = [value for value in lst1 if value in lst2]
    return lst3
