value = int(input("Enter value : "))
sum = 0
digit = value % 10
sum += digit

# rev = 0

# while(value>0):
#           dig = value%10
#           rev = (rev *10) + dig
#           value = value//10

# di = rev%10
while(value>10):
          di = value%10
          
sum += di
print("sum is : " , sum)   