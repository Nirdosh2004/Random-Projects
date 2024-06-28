# reverse integer 

value = int(input("Enter value : "))
# print(type(value))
co = value
ans = 0 
while(value>0):
          digit = value % 10
          ans  = ans * 10 + digit
          value = value // 10
print("reversed answer is : " ,ans)          

if(co == ans):
        print("Given code is palindrome")
else:
        print("Given value is not Palindrome")