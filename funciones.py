from utils import split, listToString, contain, chart2ASCIICon3Digitos

def codificarASCII(textoParaCodificar: str) -> str:
    
    # Se separa el texto en una lista de caracteres
    listaDeCaracteres = split(textoParaCodificar) 
    
    # Se genera una lista de caracteres codificados
    listaDeCaracteresCodificados = []
    for chart in listaDeCaracteres:
        
        # Se codifica un caracte a su equivalente al formato ASCII pero en un numero de 3 cifras
        tempChart = chart2ASCIICon3Digitos(chart)
        # Se añade el caracter codificado a la lista de caracteres codificados
        listaDeCaracteresCodificados.append(tempChart)

    # Se crea un texto codificado a partir de la lista de caracteres codificados
    caracteresCodificados = listToString(listaDeCaracteresCodificados) 
    return caracteresCodificados


def decodificarASCII(textoParaDecoficar: str) -> str:

    listaDeCaracteres = split(textoParaDecoficar)

    contador = 0
    for caracter in listaDeCaracteres: 
        
        if contador % 3:
            
            # Conjunto de 3 numeros que representan un caracter en la tabla ASCII
            conjuntoDe3Numeros = listaDeCaracteres[0]
        # print(caracter)
        contador +=1
        print(contador)
    
    # print(listaDeCaracteres)
    return listaDeCaracteres

decodificarASCII('1001106111106111106111106111106')


def crearMensajeCodificado(
    path: str, 
    operacion: str, 
    posicionInicial: str, 
    textoDecodificado: str, 
    paso: str = '01' 
):
    # Se crea el objeto 'tempFile' que hace referencia al archivo de texto con extension .txt
    tempFile = open(path, 'w')

    # Se crea el mensaje codificado
    tempTextoCodificado = codificarASCII(textoDecodificado)
    
    tempContentFile = ''
    # Si el texto '999' no exist en el mensaje, se añadirá para marcar el cierre del texto codificado
    if contain(tempTextoCodificado, '999'): 
        tempContentFile = F'{operacion}{posicionInicial}{paso}{tempTextoCodificado}'
    else: 
        tempContentFile = F'{operacion}{posicionInicial}{paso}{tempTextoCodificado}999'

    print(tempContentFile)

    # Se modifica el contenido del archivo de texto 
    tempFile.write(tempContentFile)
    return tempContentFile
