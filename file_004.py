
def getStrNoExp(num):
    return str('{:f}'.format(num)).rstrip('0')

def getFractionalSymbolsAmount(num):
    return len(getStrNoExp(num).rstrip('0').split('.')[1])




def getPrimeFactors(num):
    factors = []
    divider = 2
    while divider ** divider <= num:
        if num % divider == 0:
            factors.append(divider)
            num //= divider
        else:
            divider += 1
    if num > 1:
        factors.append(num)
    return factors





def countValueInList(lst, value):
    counter = 0
    for i in range(len(lst)):
        if lst[i] == value:
            counter += 1
    return counter


def getDistinctValues(lst):
    distinctLst = []
    for i in range(len(lst)):
        if countValueInList(lst, lst[i]) == 1:
            distinctLst.append(lst[i])
    return distinctLst