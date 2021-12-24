"""Algoritmo"""

from itertools import chain, combinations
from num.models import Num
import json

def powerset(list_name):
    s = list(list_name)
    return chain.from_iterable(combinations(s, r) for r in range(len(s)+1))

def delete(power):
    posible_vector = [sub for sub in power if sum(list(sub)) == 52]

    sin_repetidos = []
    for i in posible_vector:
        for j in posible_vector:
            if(i!=j) and (i<=j):
                sin_repetidos.append(j)
    
    # Elimina los valores repetidos
    return set(sin_repetidos)

def main(lista):
    power = powerset(lista)
    values = delete(power)
    return values



valore = [22,30,10,12,30]
a=main(valore)
for i in a:

    Num.objects.create(the_json= i)
    
    


