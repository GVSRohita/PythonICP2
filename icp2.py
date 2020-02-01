# converting lbs to kgs
N = int(input("Enter the number of students:"))
ListofWeights = []
convertedweightList = []
for person in range(N):
    weight = int(input("Enter the weight in Kgs: "))
    ListofWeights.append(weight)
    convertedweight = weight*0.454
    convertedweightList.append(convertedweight)
print("The weights students in Kgs: ", ListofWeights)
print("The weights of students in LBs: ", convertedweightList)



