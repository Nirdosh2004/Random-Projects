# remove duplicate and insert in another list

li = [2,4,3,5,1,2,4,3,5,6,7,5,4]
i = 0
resu = []
for i in li:
          if i not in resu:
                  resu.append(i)
                  
                  
print(li)
print(resu)