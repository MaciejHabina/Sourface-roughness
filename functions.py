import math

def OpeningFile(name):  # returns the input data as a tuple of height of roughness profile
    data = []
    with open(name, 'r') as file:
        for line in file:
            NewList = line.rstrip('\n').split(',')
            if len(NewList) == 2:
                data.append(float(NewList[1]))

    del NewList
    return tuple(data)


def OpeningFileLength(name):  # returns the length of measure distance
    data = []
    with open(name, 'r') as file:
        for line in file:
            NewList = line.rstrip('\n').split(',')
            if len(NewList) == 2:
                data.append(float(NewList[0]))

    del NewList
    MaxValue = max(data)
    MinValue = min(data)
    del data
    DistanceLength = MaxValue - MinValue
    return DistanceLength

def OpeningFile3(name):  # returns the input data as a list of the lists
    data3 = []
    with open(name, 'r') as file:
        for line in file:
            NewList = line.rstrip('\n').split(',')
            if len(NewList) == 2:
                NewList[0] = float(NewList[0])
                NewList[1] = float(NewList[1])
                data3.append(NewList)
    del NewList
    return data3


"""
def OpeningFile2(name):  # returns the input data as a dictionary: horizontal coordinate and height of roughness
    data2 = {}
    with open(name, "r") as file:
        for line in file:
            NewList = line.rstrip('\n').split(',')
            if len(NewList) == 2:
                data2[float(NewList[0])] = float(NewList[1])
    del NewList
    return data2
"""


def Ra(data):   # calculate value of Ra parameter for the chosen file
    sum = 0
    for value in data:
        sum = sum + abs(value)

    Ra = sum / len(data)

    return round(Ra, 4)


def Rq(data):   # calculate value of Rq parameter for the chosen file
    sum = 0
    for value in data:
        sum = sum + (value)**2
    Rq = math.sqrt(sum / len(data))

    return round(Rq, 4)


def Rsk(Rq, data):  # calculate value of Rsk parameter for the chosen file
    sum = 0
    for value in data:
        sum = sum + (value)**3
    Rsk = (1 / Rq**3) * (sum / len(data))

    return round(Rsk, 4)


def Rku(Rq, data):  # calculate value of Rku parameter for the chosen file
    sum = 0
    for value in data:
        sum = sum + (value)**4
    Rku = (1 / Rq**4) * (sum / len(data))

    return round(Rku, 4)


def AverageLine(data):              # calculate the height of average line for the chosen roughness profile
    MinimalValue = min(data)
    MaximalValue = max(data)
    i = MinimalValue
    Values = {}
    while i <= MaximalValue:            # make the dictionary: i : sum of squares of distance from average line to analyzed point
        Sum = 0
        for value in data:
            Sum = Sum + (i - value)**2
        Values[i] = Sum
        i += 0.0001

    temp = []
    NewList = []
    NewList2 = []
    NewList3 = []

    for key, value in Values.items():     # make the list of list based dictionary "Values"
        temp = [key, value]
        NewList.append(temp)

    for element in NewList:                   # make the list of sum of squares of distance from average line to analyzed point
        NewList2.append(element[1])
        NewList3.append(element[0])

    Minimum = min(NewList2)
    IndexValue = NewList2.index(Minimum)
    SearchedValue = NewList3[IndexValue]

    return SearchedValue                        # searched value of average line


def Rp(AverageLine, data):      # calculate value of Rp parameter for the chosen file
    MaximalValue = max(data)
    Rp = MaximalValue - AverageLine

    return round(Rp, 4)


def Rv(AverageLine, data):      # calculate value of Rv parameter for the chosen file
    MinimalValue = min(data)
    Rv = AverageLine - MinimalValue

    return round(Rv, 4)


def Rt(data):                   # calculate value of Rt parameter for the chosen file

    MinimalValue = abs(min(data))
    MaximalValue = abs(max(data))
    Rt = MinimalValue + MaximalValue

    return round(Rt, 4)


def Rz(AverageLine, data):      # calculate value of Rz parameter for the chosen file
    NewList = []
    Sum = 0

    Values = sorted(data)
    MinList = Values[0:5]
    MaxList = Values[-6:-1]
    NewList.extend(MinList)
    NewList.extend(MaxList)

    for value in NewList:
        Sum = Sum + abs(value - AverageLine)

    Rz = Sum / 5

    return round(Rz, 4)


def Rsm(AverageLine, Rz, DistanceLength, data):  # calculate value of Rsm parameter for the chosen file
 