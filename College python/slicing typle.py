t = (10,20,40,33)
# i = 0
# while (i<len(t)):
#           print(t[i] , "->" , t[i]**2)

#           i += 1

# for i in t:
#         print(i**2)

# a = 2,4,3
# b = 6,5,2

# c = a+b
# print(c)

t = t + (0,30,49,40)
print(t)

k = len(t)
print("Length of the tuple : " , k)
print("Maximum numbber : " , max(t))
print("Lowest elements : " , min(t))
print("Sorted elements : " , sorted(t))
print("total sum of all elements are : " , sum(t))
print("Element 30 found at : " , t.index(30))
print("Element 40 appear for : " , t.count(40) , " times")
