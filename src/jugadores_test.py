from jugadores import *
def test_mejores_jugadores(jugadores, año, n):
    print(mejores_jugadores(jugadores, año, n))

def test_jugadores_por_golpes(jugadores):
    res=jugadores_por_golpes(jugadores)
    print("Los dos primeros elementos de la lista son:")
    print(res[0])
    print(res[1])
    print("\nLos dos últimos elementos de la lista son:")
    print(res[-2])
    print(res[-1])

def  test_promedio_ultimos_resultados(jugadores, f1=None, f2=None):
    print(promedio_ultimos_resultados(jugadores, f1, f2))

def test_jugador_menor_handicap_por_federacion(jugadores):
    d=jugador_menor_handicap_por_federacion(jugadores)
    for itm in d.items():
        print(itm)

def test_comparativa_de_mejores_resultados_segun_handicap(jugadores):
    res=comparativa_de_mejores_resultados_segun_handicap(jugadores)
    print("Los dos primeros elementos de la lista son:")
    print(res[0])
    print(res[1])
    print("\nLos dos últimos elementos de la lista son:")
    print(res[-2])
    print(res[-1])
if __name__ == "__main__":
    jugadores=lee_jugadores('data/jugadores.csv')

    print("Registros leídos: ", len(jugadores))
    print("Los dos primeros registros:")
    for j in jugadores[:2]:
        print(j)
    print("\nLos dos últimos registros:")
    for j in jugadores[-2:]:
        print(j)
    

######################### Ejercicio 2 #########################
print("Los 4 mejores jugadores en 1969 son:")
test_mejores_jugadores(jugadores, 1969, 4)

######################### Ejercicio 3 #########################
print("\nLos jugadores ordenados por número de golpes:")
test_jugadores_por_golpes(jugadores)

######################### Ejercicio 4 #########################
print("\nPromedio de los últimos resultados de los jugadores cuya fecha de actuazación está comprendidia entre 1-3-2020 y 31-5-2020:")
test_promedio_ultimos_resultados(jugadores, date(2020,3,1), date(2020,5,31))

######################### Ejercicio 5 #########################
print("\nJugador con menor handicap de cada federación:")
test_jugador_menor_handicap_por_federacion(jugadores)

######################### Ejercicio 6 #########################
print("\nComparativa de los mejores resultados de los jugadores según su handicap:")
test_comparativa_de_mejores_resultados_segun_handicap(jugadores)

   