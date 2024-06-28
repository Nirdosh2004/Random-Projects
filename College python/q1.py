# q1
userLi = []
i = 0
for i in range(0,10):
          num = int(input("Enter any value : "))
          userLi.append(num)
          i += 1

print(userLi)
# q2
print("Max number is : " , max(userLi))
# q3
sum = 0
j = 0
for j in userLi:
        sum += userLi[j]
        j += 1
print("Sum : " , sum)
        