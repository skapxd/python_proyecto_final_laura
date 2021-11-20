def split(word):
    return [char for char in word]



def listToString(s): 
    str1 = "" 

    for ele in s: 
        str1 += ele  

    return str1 

def contain(text: str, target: str) -> bool: 
    if target not in text: 
        return False
    else:
        return True


def chart2ASCIICon3Digitos(chart: str) -> str:

    tempChart = f'{ord(chart)}'

    chart3Digit = ''
    if len(tempChart) == 1:
        chart3Digit = f'00{tempChart}'
    elif len(tempChart) == 2:
        chart3Digit = f'0{tempChart}'

    return chart3Digit  