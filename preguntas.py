"""
Laboratorio de Programación Básica en Python para Manejo de Datos
-----------------------------------------------------------------------------------------

Este archivo contiene las preguntas que se van a realizar en el laboratorio.

No puede utilizar pandas, numpy o scipy. Se debe utilizar solo las funciones de python
básicas.

Utilice el archivo `data.csv` para resolver las preguntas.


"""

def pregunta_01():
    """
    Retorne la suma de la segunda columna.

    Rta/
    214

    """
    suma_segunda_columna = 0
    with open('data.csv', 'r') as archivo:
        for linea in archivo:
            # Dividir la línea en columnas utilizando la tabulación como separador
            columnas = linea.strip().split('\t')
            
            # Sumar el valor de la segunda columna (asumiendo que las columnas están indexadas desde 0)
            suma_segunda_columna += int(columnas[1])

    return suma_segunda_columna




def pregunta_02():
    """
    Retorne la cantidad de registros por cada letra de la primera columna como la lista
    de tuplas (letra, cantidad), ordendas alfabéticamente.

    Rta/
    [
        ("A", 8),
        ("B", 7),
        ("C", 5),
        ("D", 6),
        ("E", 14),
    ]

    """
    contador_letras = {}
    with open('data.csv', 'r') as archivo:
        # Iterar sobre cada línea en el archivo
        for linea in archivo:
            # Dividir la línea en columnas utilizando la tabulación como separador
            columnas = linea.strip().split('\t')
            
            # Obtener la primera letra de la primera columna (asumiendo que las columnas están indexadas desde 0)
            primera_letra = columnas[0][0]

            # Actualizar el contador de la letra
            contador_letras[primera_letra] = contador_letras.get(primera_letra, 0) + 1

    # Crear la lista de tuplas ordenadas alfabéticamente
    resultado = sorted(contador_letras.items())

    return resultado



def pregunta_03():
    """
    Retorne la suma de la columna 2 por cada letra de la primera columna como una lista
    de tuplas (letra, suma) ordendas alfabeticamente.

    Rta/
    [
        ("A", 53),
        ("B", 36),
        ("C", 27),
        ("D", 31),
        ("E", 67),
    ]

    """
    suma_por_letra = {}
    with open('data.csv', 'r') as archivo:
        # Iterar sobre cada línea en el archivo
        for linea in archivo:
            # Dividir la línea en columnas utilizando la tabulación como separador
            columnas = linea.strip().split('\t')
            
            # Obtener la primera letra de la primera columna (asumiendo que las columnas están indexadas desde 0)
            primera_letra = columnas[0][0]

            # Obtener el valor de la segunda columna y sumarlo al total de la letra
            valor_segunda_columna = int(columnas[1])
            suma_por_letra[primera_letra] = suma_por_letra.get(primera_letra, 0) + valor_segunda_columna

    # Crear la lista de tuplas ordenadas alfabéticamente
    resultado = sorted(suma_por_letra.items())

    return resultado





def pregunta_04():
    """
    La columna 3 contiene una fecha en formato `YYYY-MM-DD`. Retorne la cantidad de
    registros por cada mes, tal como se muestra a continuación.

    Rta/
    [
        ("01", 3),
        ("02", 4),
        ("03", 2),
        ("04", 4),
        ("05", 3),
        ("06", 3),
        ("07", 5),
        ("08", 6),
        ("09", 3),
        ("10", 2),
        ("11", 2),
        ("12", 3),
    ]

    """
    registros_por_mes = {}
    with open('data.csv', 'r') as archivo:
        # Iterar sobre cada línea en el archivo
        for linea in archivo:
            # Dividir la línea en columnas utilizando la tabulación como separador
            columnas = linea.strip().split('\t')
            
            # Obtener el mes de la tercera columna (asumiendo que las columnas están indexadas desde 0)
            mes = columnas[2][5:7]

            # Incrementar el contador del mes
            if mes in registros_por_mes:
                registros_por_mes[mes] += 1
            else:
                registros_por_mes[mes] = 1

    # Crear la lista de tuplas ordenadas alfabéticamente por mes
    resultado = sorted(registros_por_mes.items())

    return resultado




def pregunta_05():
    """
    Retorne una lista de tuplas con el valor maximo y minimo de la columna 2 por cada
    letra de la columa 1.

    Rta/
    [
        ("A", 9, 2),
        ("B", 9, 1),
        ("C", 9, 0),
        ("D", 8, 3),
        ("E", 9, 1),
    ]

    """
    valores_por_letra = {}
    with open('data.csv', 'r') as archivo:
        # Iterar sobre cada línea en el archivo
        for linea in archivo:
            # Dividir la línea en columnas utilizando la tabulación como separador
            columnas = linea.strip().split('\t')
            
            # Obtener la letra de la primera columna y el valor de la segunda columna
            letra = columnas[0][0]
            valor = int(columnas[1])

            # Actualizar la lista de valores para cada letra
            if letra in valores_por_letra:
                valores_por_letra[letra].append(valor)
            else:
                valores_por_letra[letra] = [valor]

    # Crear la lista de tuplas con el valor máximo y mínimo por letra y ordenar alfabéticamente
    resultado = sorted((letra, max(valores), min(valores)) for letra, valores in valores_por_letra.items())

    return resultado



def pregunta_06():
    """
    La columna 5 codifica un diccionario donde cada cadena de tres letras corresponde a
    una clave y el valor despues del caracter `:` corresponde al valor asociado a la
    clave. Por cada clave, obtenga el valor asociado mas pequeño y el valor asociado mas
    grande computados sobre todo el archivo.

    Rta/
    [
        ("aaa", 1, 9),
        ("bbb", 1, 9),
        ("ccc", 1, 10),
        ("ddd", 0, 9),
        ("eee", 1, 7),
        ("fff", 0, 9),
        ("ggg", 3, 10),
        ("hhh", 0, 9),
        ("iii", 0, 9),
        ("jjj", 5, 17),
    ]

    """
    valores_por_clave = {}
    with open('data.csv', 'r') as archivo:
        # Iterar sobre cada línea en el archivo
        for linea in archivo:
            # Dividir la línea en columnas utilizando la tabulación como separador
            columnas = linea.strip().split('\t')
            
            # Obtener la cadena de tres letras de la quinta columna (asumiendo que las columnas están indexadas desde 0)
            clave_valor_str = columnas[4].split('\t')[-1]

            # Obtener los valores asociados a la clave
            pares_clave_valor = [par.split(':') for par in clave_valor_str.split(',')]

            for par in pares_clave_valor:
                clave = par[0]
                valor_asociado = int(par[1])
                
                # Actualizar los valores mínimo y máximo asociados a la clave
                if clave in valores_por_clave:
                    valores_por_clave[clave] = (min(valores_por_clave[clave][0], valor_asociado), max(valores_por_clave[clave][1], valor_asociado))
                else:
                    valores_por_clave[clave] = (valor_asociado, valor_asociado)

    # Crear la lista de tuplas ordenadas alfabéticamente por clave
    resultado = sorted((clave, min_max[0], min_max[1]) for clave, min_max in valores_por_clave.items())

    return resultado




def pregunta_07():
    """
    Retorne una lista de tuplas que asocien las columnas 0 y 1. Cada tupla contiene un
    valor posible de la columna 2 y una lista con todas las letras asociadas (columna 1)
    a dicho valor de la columna 2.

    Rta/
    [
        (0, ["C"]),
        (1, ["E", "B", "E"]),
        (2, ["A", "E"]),
        (3, ["A", "B", "D", "E", "E", "D"]),
        (4, ["E", "B"]),
        (5, ["B", "C", "D", "D", "E", "E", "E"]),
        (6, ["C", "E", "A", "B"]),
        (7, ["A", "C", "E", "D"]),
        (8, ["E", "D", "E", "A", "B"]),
        (9, ["A", "B", "E", "A", "A", "C"]),
    ]

    """
    valores_letras_asociadas = {}
    with open('data.csv', 'r') as archivo:
        # Iterar sobre cada línea en el archivo
        for linea in archivo:
            # Dividir la línea en columnas utilizando la tabulación como separador
            columnas = linea.strip().split('\t')
            
            # Obtener el valor de la columna 2 y la letra de la columna 1
            valor_columna_2 = int(columnas[1])
            letra_columna_1 = columnas[0][0]

            # Actualizar la lista de letras asociadas al valor de la columna 2
            if valor_columna_2 in valores_letras_asociadas:
                valores_letras_asociadas[valor_columna_2].append(letra_columna_1)
            else:
                valores_letras_asociadas[valor_columna_2] = [letra_columna_1]

    # Crear la lista de tuplas y ordenarla
    resultado = sorted([(valor, letras) for valor, letras in valores_letras_asociadas.items()])

    return resultado




def pregunta_08():
    """
    Genere una lista de tuplas, donde el primer elemento de cada tupla contiene  el valor
    de la segunda columna; la segunda parte de la tupla es una lista con las letras
    (ordenadas y sin repetir letra) de la primera  columna que aparecen asociadas a dicho
    valor de la segunda columna.

    Rta/
    [
        (0, ["C"]),
        (1, ["B", "E"]),
        (2, ["A", "E"]),
        (3, ["A", "B", "D", "E"]),
        (4, ["B", "E"]),
        (5, ["B", "C", "D", "E"]),
        (6, ["A", "B", "C", "E"]),
        (7, ["A", "C", "D", "E"]),
        (8, ["A", "B", "D", "E"]),
        (9, ["A", "B", "C", "E"]),
    ]
    
    """
    valores_letras_asociadas = {}
    with open('data.csv', 'r') as archivo:
        # Iterar sobre cada línea en el archivo
        for linea in archivo:
            # Dividir la línea en columnas utilizando la tabulación como separador
            columnas = linea.strip().split('\t')
            
            # Obtener el valor de la columna 2 y la letra de la columna 1
            valor_columna_2 = int(columnas[1])
            letra_columna_1 = columnas[0][0]

            # Actualizar la lista de letras asociadas al valor de la columna 2
            if valor_columna_2 in valores_letras_asociadas:
                valores_letras_asociadas[valor_columna_2].add(letra_columna_1)
            else:
                valores_letras_asociadas[valor_columna_2] = {letra_columna_1}

    # Crear la lista de tuplas y ordenarla
    resultado = sorted([(valor, sorted(list(letras))) for valor, letras in valores_letras_asociadas.items()])

    return resultado





def pregunta_09():
    """
    Retorne un diccionario que contenga la cantidad de registros en que aparece cada
    clave de la columna 5.

    Rta/
    {
        "aaa": 13,
        "bbb": 16,
        "ccc": 23,
        "ddd": 23,
        "eee": 15,
        "fff": 20,
        "ggg": 13,
        "hhh": 16,
        "iii": 18,
        "jjj": 18,
    }

    """
    conteo_claves = {}
    with open('data.csv', 'r') as archivo:
        # Iterar sobre cada línea en el archivo
        for linea in archivo:
            # Dividir la línea en columnas utilizando la tabulación como separador
            columnas = linea.strip().split('\t')
            
            # Obtener la cadena de la quinta columna (asumiendo que las columnas están indexadas desde 0)
            cadena_columna_5 = columnas[4]

            # Dividir la cadena en pares clave-valor y contar la aparición de cada clave
            pares_clave_valor = cadena_columna_5.split(',')
            for par in pares_clave_valor:
                clave = par.split(':')[0]
                if clave in conteo_claves:
                    conteo_claves[clave] += 1
                else:
                    conteo_claves[clave] = 1

    # Ordenar el diccionario por las claves
    resultado_ordenado = dict(sorted(conteo_claves.items()))

    return resultado_ordenado



def pregunta_10():
    """
    Retorne una lista de tuplas contengan por cada tupla, la letra de la columna 1 y la
    cantidad de elementos de las columnas 4 y 5.

    Rta/
    [
        ("E", 3, 5),
        ("A", 3, 4),
        ("B", 4, 4),
        ...
        ("C", 4, 3),
        ("E", 2, 3),
        ("E", 3, 3),
    ]


    """
    resultados = []
    with open('data.csv', 'r') as archivo:
        # Iterar sobre cada línea en el archivo
        for linea in archivo:
            # Dividir la línea en columnas utilizando la tabulación como separador
            columnas = linea.strip().split('\t')

            # Obtener la letra de la columna 1
            letra_columna_1 = columnas[0][0]

            # Obtener la cantidad de elementos de las columnas 4 y 5
            cantidad_columna_4 = len(columnas[3].split(','))
            cantidad_columna_5 = len(columnas[4].split(','))

            # Agregar la tupla a la lista de resultados
            resultados.append((letra_columna_1, cantidad_columna_4, cantidad_columna_5))

    return resultados


def pregunta_11():
    """
    Retorne un diccionario que contengan la suma de la columna 2 para cada letra de la
    columna 4, ordenadas alfabeticamente.

    Rta/
    {
        "a": 122,
        "b": 49,
        "c": 91,
        "d": 73,
        "e": 86,
        "f": 134,
        "g": 35,
    }


    """
    suma_letras = {}
    with open('data.csv', 'r') as archivo:
        # Iterar sobre cada línea en el archivo
        for linea in archivo:
            # Dividir la línea en columnas utilizando la tabulación como separador
            columnas = linea.strip().split('\t')

            # Obtener la letra de la columna 4
            letras_columna_4 = columnas[3].split(',')

            # Obtener la suma de la columna 2 para cada letra de la columna 4
            for letra in letras_columna_4:
                if letra in suma_letras:
                    suma_letras[letra] += int(columnas[1])
                else:
                    suma_letras[letra] = int(columnas[1])

    # Ordenar el diccionario por las claves alfabéticamente
    resultado_ordenado = dict(sorted(suma_letras.items()))

    return resultado_ordenado





def pregunta_12():
    """
    Genere un diccionario que contengan como clave la columna 1 y como valor la suma de
    los valores de la columna 5 sobre todo el archivo.

    Rta/
    {
        'A': 177,
        'B': 187,
        'C': 114,
        'D': 136,
        'E': 324
    }

    """
    suma_columna_5 = {}
    with open('data.csv', 'r') as archivo:
        # Iterar sobre cada línea en el archivo
        for linea in archivo:
            # Dividir la línea en columnas utilizando la tabulación como separador
            columnas = linea.strip().split('\t')

            # Obtener la letra de la columna 1
            letra_columna_1 = columnas[0][0]

            # Obtener la suma de los valores de la columna 5 para cada letra de la columna 1
            valor_columna_5 = columnas[4].split(',')
            for par in valor_columna_5:
                _, valor = par.split(':')
                if letra_columna_1 in suma_columna_5:
                    suma_columna_5[letra_columna_1] += int(valor)
                else:
                    suma_columna_5[letra_columna_1] = int(valor)

    # Ordenar el diccionario por las claves alfabéticamente
    resultado_ordenado = dict(sorted(suma_columna_5.items()))

    return resultado_ordenado



resultado_pregunta_01 = pregunta_01()
print(resultado_pregunta_01)
resultado_pregunta_02 = pregunta_02()
print(resultado_pregunta_02)
resultado_pregunta_03 = pregunta_03()
print(resultado_pregunta_03)
resultado_pregunta_04 = pregunta_04()
print(resultado_pregunta_04)
resultado_pregunta_05 = pregunta_05()
print(resultado_pregunta_05)
resultado_pregunta_06 = pregunta_06()
print(resultado_pregunta_06)
resultado_pregunta_07 = pregunta_07()
print(resultado_pregunta_07)
resultado_pregunta_08 = pregunta_08()
print(resultado_pregunta_08)
resultado_pregunta_09 = pregunta_09()
print(resultado_pregunta_09)
resultado_pregunta_10 = pregunta_10()
print(resultado_pregunta_10)
resultado_pregunta_11 = pregunta_11()
print(resultado_pregunta_11)
resultado_pregunta_12 = pregunta_12()
print(resultado_pregunta_12)
