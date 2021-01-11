import json


with open('BMI.json') as f:
    data = json.load(f)
print(data)
InterValues = []
TempList = []

for i in range(0, len(data[1])):

        if (i==0):
            InterValues = data[1][i]["BMIRange"].replace(" and below","")
            TempList.append(InterValues)
        elif (i==5):
            InterValues = data[1][i]["BMIRange"].replace(" and above","")
            TempList.append(InterValues)
        else:
            InterValues = data[1][i]["BMIRange"].replace(" ","")
            TempList.append(InterValues)


ListSplit = []

for i in range(0, len(TempList)):
    ListSplit.append(TempList[i].split("-"))
       
for i in ListSplit:
    if i==0:
        print(float(i[0]))
    if i==5:
        print(float(i[0]))
    else:
        print(i)

WeightConclusion = []
RiskConclusion = []
final = []

for i in range(0, len(data[1])):
    TempBMI = data[0][i]["WeightKg"]/(data[0][i]["HeightCm"]/100)
    if (TempBMI < float(ListSplit[0][0])):
        final.append(TempBMI)
        final.append(data[1][0]["BMI Category"])
        final.append(data[1][0]["HealthRisk"])
    elif(TempBMI>float(ListSplit[5][0])):
        final.append(TempBMI)
        final.append(data[1][5]["BMI Category"])
        final.append(data[1][5]["HealthRisk"])
    elif (TempBMI>=float(ListSplit[i][0]) and TempBMI<=float(ListSplit[i][1])):
        final.append(TempBMI)
        final.append(data[1][i]["BMI Category"])
        final.append(data[1][i]["HealthRisk"])



columnsToBeAdded = []
temp = []
dictionary = {}
for i in range(0,len(final)-2):
    temp.append("{")
    temp.append("BMI")
    temp.append(" :")
    temp.append(final[i])
    temp.append(",")
    temp.append("BMICategory")
    temp.append(" :")
    temp.append(final[i+1])
    temp.append(",")
    temp.append("HealthRisk")
    temp.append(" :")
    temp.append(final[i+2])
    temp.append("}")


for i in range(0,len(data)):
    data.append(temp)

print(data)


count = 0
for i in range(0,len(data) -2,3):
    if (final[i]>=25 and final[i]<=29.9):
        count = count+1
print("Total Number of overweight")
print(count)
