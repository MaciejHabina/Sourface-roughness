import functions

nameOfFile = input("Enter the full file name to surface roughness analysis: ")


data = functions.OpeningFile(nameOfFile)
# data2 = functions.OpeningFile2(nameOfFile)
# data3 = functions.OpeningFile3(nameOfFile)
DistanceLength = functions.OpeningFileLength(nameOfFile)

Ra = functions.Ra(data)
Rq = functions.Rq(data)
Rsk = functions.Rsk(Rq, data)
Rku = functions.Rku(Rq, data)
AverageLine = functions.AverageLine(data)
# Rsm = functions.Rsm(data3)
Rp = functions.Rp(AverageLine, data)
Rv = functions.Rv(AverageLine, data)
Rt = functions.Rt(data)
Rz = functions.Rz(AverageLine, data)


print("Ra: ", Ra)
print("Rq: ", Rq)
print("Rsk: ", Rsk)
print("Rp: ", Rp)
print("Rv: ", Rv)
print("Rt: ", Rt)
print("Rku: ", Rku)
print("Rz: ", Rz)
