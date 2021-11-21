from utils import customSplit, customList2String, customContain, chart2ASCIICon3Digitos, contarVocales, contarConsonantes


def codificarASCII(textoParaCodificar: str) -> str:

    # Se separa el texto en una lista de caracteres
    listaDeCaracteres = customSplit(textoParaCodificar)

    # Se genera una lista de caracteres codificados
    listaDeCaracteresCodificados = []
    for chart in listaDeCaracteres:
        # print('chart: ', chart)

        # Se codifica un caracte a su equivalente al formato ASCII pero en un numero de 3 cifras
        tempChart = chart2ASCIICon3Digitos(chart)
        # Se añade el caracter codificado a la lista de caracteres codificados
        listaDeCaracteresCodificados.append(tempChart)

    # Se crea un texto codificado a partir de la lista de caracteres codificados
    caracteresCodificados = customList2String(listaDeCaracteresCodificados)
    return caracteresCodificados


def convertirStringAListaConElementosDe3Digitos(string: str) -> list:
    # Numero de digitos por elemento del Array
    # Se escoge el numero 3, porque son necesarios 3 digitos para convertir un
    # un numero en una letra utilizando la
    d = 3

    # Crea una lista con una longitud de 3 elementos
    customRange = range(0, len(string), d)

    # [listOfListNumber] es un Array de 2 dimensiones, la 1ra dimension del array
    # representa toda la oracion, la segunda dimension del array representa la letra
    listOfListNumber = [string[i:i + d] for i in customRange]

    listOfStringNumber = []
    for listOfNumber in listOfListNumber:

        # Se transforma la lista a string
        stringOfNumber = customList2String(listOfNumber)

        listOfStringNumber.append(stringOfNumber)

    return listOfStringNumber


def decodificarASCII(textoParaDecoficar: str) -> list:

    listaDeCaracteresCodificados = convertirStringAListaConElementosDe3Digitos(
        textoParaDecoficar
    )

    listaDeCaracterDecodificado = []
    for caracterCodificado in listaDeCaracteresCodificados:

        # La secuencia de caracteres '999' se identificara
        # como indicador para que la funcion deje de decodificar
        # números a letras en el formato ASCII
        if caracterCodificado == '999':
            return listaDeCaracterDecodificado

        # Es necesario transformar el valor de tipo String a valor de tipo Int,
        # en caso de no hacerse, el programa soltara una excepcion
        number = int(caracterCodificado)

        caracterDecodificado = chr(number)
        listaDeCaracterDecodificado.append(caracterDecodificado)

    return listaDeCaracterDecodificado


def crearMensajeCodificado(
    path: str,
    operacion: str,
    posicionInicial: str,
    textoDecodificado: str,
    textoOriginal: str,
    resultado: str,
    paso: str = '01'
):
    # Se crea el objeto 'tempFile' que hace referencia al archivo de texto con extension .txt
    tempFile = open('./archivoSalida.txt', 'w')
    # tempFile = open(path, 'w')

    # Se crea el mensaje codificado
    tempTextoCodificado = codificarASCII(textoDecodificado)

    tempContentFile = ''
    # Si el texto '999' no exist en el mensaje, se añadirá para marcar el cierre del texto codificado
    if customContain(tempTextoCodificado, '999'):
        tempContentFile = F'{operacion}{posicionInicial}{paso}{tempTextoCodificado}'
    else:
        tempContentFile = F'{operacion}{posicionInicial}{paso}{tempTextoCodificado}999'

    data = f"""
Cadena de texto original: {textoOriginal}
Mensaje decodificado: {textoDecodificado}
Resultado de la operacion: {resultado}
Cantidad de letras del mensaje: {len(textoDecodificado)}
Cantidad de vocales en el mensaje: {contarVocales(textoDecodificado)}
Cantidad de consonantes en el mensaje: {contarConsonantes(textoDecodificado)}

    """
    # Se modifica el contenido del archivo de texto
    tempFile.write(data)
    # tempFile.write(tempContentFile)
    return tempContentFile


def promedioAritmetico(valores: str) -> int:
    tempIntList = []
    for e in valores:
        tempString = chart2ASCIICon3Digitos(e)
        tempNumber = int(tempString)
        tempIntList.append(tempNumber)

    sumaDeLosElementos = 0

    for valor in tempIntList:
        sumaDeLosElementos += valor

    devisionDeLosElementos = sumaDeLosElementos / len(valores)

    return devisionDeLosElementos


def ordenarDeMayorAMenor(valores: str) -> list:

    tempIntList = []
    for e in valores:
        tempString = chart2ASCIICon3Digitos(e)
        tempNumber = int(tempString)
        tempIntList.append(tempNumber)

    tempValoresOrdenados = []
    for value in tempIntList:
        tempValue = int(value)
        tempValoresOrdenados.append(tempValue)

    tempValoresOrdenados.sort()
    ValoresOrdenados = [num for num in reversed(tempValoresOrdenados)]

    valoresASCIIOrdenados = ''
    for e in ValoresOrdenados:
        string = chr(e)
        valoresASCIIOrdenados += string

    return valoresASCIIOrdenados


def ordenarDeMenorAMayor(valores: str) -> list:
    tempIntList = []
    for e in valores:
        tempString = chart2ASCIICon3Digitos(e)
        tempNumber = int(tempString)
        tempIntList.append(tempNumber)

    tempValoresOrdenados = []
    for value in tempIntList:
        tempValue = int(value)
        tempValoresOrdenados.append(tempValue)

    tempValoresOrdenados.sort()

    valoresASCIIOrdenados = ''
    for e in tempValoresOrdenados:
        string = chr(e)
        valoresASCIIOrdenados += string

    return valoresASCIIOrdenados


def obtenerValorOperacion(operacion: str, datos):

    # Retorna el promedio aritmetico
    if operacion == '+':
        return promedioAritmetico(datos)

    # Retorna los caracteres ASCII Ordenados de mayor a menor
    elif operacion == '-':
        return ordenarDeMayorAMenor(datos)

    # Retorna los caracteres ASCII Ordenados de menor a mayor
    elif operacion == '*':
        return ordenarDeMenorAMayor(datos)

    # Retorna la productoria de los valores
    elif operacion == '/':
        return 'falta por implementar'

    return {
        mensaje: 'La operación no es válida'
    }


def crearMensajeDecodificado(texto: str):

    # Extrayendo los datos del texto
    operacion = texto[0]

    # Se genera una variable temp porque es necesario devidir el valor
    # entre 3, debido a que se generara un Array del texto con elementos
    # que tienen una longitud de 3 digitos
    tempPosicionInicial = int(texto[1:3])  # ((int(texto[1:3]) - 5) / 3)
    tempPosicionInicial_2 = tempPosicionInicial - 5
    tempPosicionInicial_3 = tempPosicionInicial_2 / 3
    posicionInicial = int(tempPosicionInicial_3)
    paso = int(texto[3:5])
    mensaje = texto[5:]

    # Convierte el mensaje en un Array con elementos de longitud de 3 digitos
    mensajeCodificado = convertirStringAListaConElementosDe3Digitos(mensaje)

    # Se extraen los datos del mensaje de acuerdo con el [paso] especificado
    elementosDeseados = mensajeCodificado[posicionInicial::paso]

    tempMensajeDecodificado = customList2String(elementosDeseados)
    mensajeDecodificado = decodificarASCII(tempMensajeDecodificado)

    valorOperacion = obtenerValorOperacion(operacion, mensajeDecodificado)

    data = {
        "operacion": operacion,
        "posicionInicial": f'{tempPosicionInicial}',
        "mensaje": customList2String(mensajeDecodificado),
        "valorOperacion": f'{valorOperacion}'
    }
    return data


texto = '+1202450789072112111108108497097099999795'
mensaje = crearMensajeDecodificado(texto)

print('mensaje["mensaje"]: ', mensaje['mensaje'])
print('mensaje["operacion"]: ', mensaje['operacion'])
print('mensaje["posicionInicial"]: ', mensaje['posicionInicial'])
print('mensaje["valorOperacion"]: ', mensaje['valorOperacion'])
