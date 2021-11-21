def customSplit(word) -> list:

    # Ejemplo del valor retornado:
    # 'hola mundo :D' -> ['h', 'o', 'l', 'a', ' ', 'm', 'u', 'n', 'd', 'o', ' ', ':', 'D']
    return [char for char in word]


def customList2String(s: str) -> str:
    str1 = ""

    for ele in s:
        str1 += ele

    # Ejemplo del valor retornado:
    # ['h', 'o', 'l', 'a', ' ', 'm', 'u', 'n', 'd', 'o', ' ', ':', 'D'] -> 'hola mundo :D'
    return str1


def customContain(text: str, target: str) -> bool:
    if target not in text:
        return False
    else:
        return True


# Es necesaria esta funcion debido que al convertir un valor de tipo String
# a un valor tipo Integer, este pierde todos los ceros que hayan al lado izquierdo.
# Para nuestra logica de negocio, necesitamos un formato estandar que tenga
# una longitud fija de 3 digitos.
# Ejemplo: convertir el valor 'h' a Integer dará como resultado 72
def chart2ASCIICon3Digitos(chart: str) -> str:

    tempChart = f'{ord(chart)}'

    chart3Digit = formatNumber(chart, '000')

    # chart3Digit = ''
    # if len(tempChart) == 1:
    #     chart3Digit = f'00{tempChart}'
    # elif len(tempChart) == 2:
    #     chart3Digit = f'0{tempChart}'
    # else:
    #     chart3Digit = tempChart

    # Ejemplos de valores retornados
    # ej:1 -> '009'
    # ej:2 -> '029'
    # ej:3 -> '329'
    return chart3Digit


# Es necesaria esta funcion porque queremos que los datos tengan un formato
# ejemplo de parametros recibidos
# string -> '75'
# format -> '000'
# return -> '075'
def formatNumber(string: str, formatOfValue: str) -> str:

    formatList = customSplit(formatOfValue)

    tempDigits = ''
    i = 0
    print('string: ', len(string))
    print('formatOfValue: ', len(formatOfValue))
    while i < (len(formatList) - len(string)):
        tempDigits += '0'
        i += 1

    # Ejemplo de valores retornados
    # ej:1 -> '009'
    # ej:2 -> '029'
    # ej:3 -> '329'
    return f'{tempDigits}{string}'


print(
    formatNumber('75', '000')
)
