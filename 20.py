arr = [3, -1, -7, -4, -5, 9, 10]

for i in range(0, 6):
    firstnumber = arr[i]
    for j in range(i+1, 6):
        secondnumber = arr[j]
        for k in range(j+1, 6):
            thirdnumber = arr[k]

            sum = firstnumber+secondnumber+thirdnumber
            if sum == 0:
                print(firstnumber, "+", secondnumber,
                      "+", thirdnumber, "=", sum)
