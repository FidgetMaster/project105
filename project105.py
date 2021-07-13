import csv
import math
file = open("project105.csv", newline = "")
reader = csv.reader(file)
filedata = list(reader)
data = filedata[0]
def mean(data):
    total = 0
    number = len(data)
    for i in data:
        total = total + int(i)
    mean = total/number
    return mean
squaredlist = []
for number in data:
    a = int(number)-mean(data)
    a = a**2
    squaredlist.append(a)
sum = 0
for i in squaredlist:
    sum = sum+i
result = sum/(len(data)-1)
standarddeviation = math.sqrt(result)
print(standarddeviation)