value  = int(input("Enter value : "))
ans = 0
while(value>0):
          digit = value % 10
          ans = ans + digit
          value = value // 10

print("answer is : " , ans)          