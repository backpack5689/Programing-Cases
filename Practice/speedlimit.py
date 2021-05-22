entries = int(input())
while entries != -1:
    miles = []
    hours = []
    for _ in range(entries):
        data = [int(a) for a in input().split()]
        miles.append(data[0])
        hours.append(data[1])
    runninghours = 0
    totalmiles = 0
    for index, time in enumerate(hours):
        milesdriven = miles[index]
        totalmiles += milesdriven * (time - runninghours)
        # print(str(totalmiles) + " = " + str(milesdriven) + " * " + str(time) + " - " + str(runninghours))
        runninghours = time
    print(str(totalmiles) + " miles")
    entries = int(input())