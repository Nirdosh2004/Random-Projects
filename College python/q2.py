# q4
n = int(input("Enter value of n :"))
li = []
i = 0
li.append(1)
li.append(2)
li.append(3)
for i in range(3,n):
          if(i % 2 != 0 and i%3 != 0):
                  li.append(i)
          #         i += 1


print(li)