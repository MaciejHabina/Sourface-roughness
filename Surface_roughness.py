import functions

nameOfFile = input("Enter the full file name to surface roughness analysis: ")


data = functions.OpeningFile(nameOfFile)
# data2 = functions.OpeningFile2(nameOfFile)
# data3 = functions.OpeningFile3(nameOfFile)

Ra = functions.Ra(data)
Rq = functions.Rq(data)
Rsk = functions.Rsk(Rq, data)
Rku = functions.Rku(Rq, data)
AverageLine = functions.AverageLine(data)           # strasznie długo liczy  tę linię średnią 
# Rsm = functions.Rsm(data3)
Rp = functions.Rp(AverageLine, data)


# print("Value of an average line is: ", AverageLine)

print("Ra: ", Ra)
print("Rq: ", Rq)
print("Rsk: ", Rsk)
print("Rp: ", Rp)

input()
