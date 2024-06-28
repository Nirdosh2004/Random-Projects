marks = [4,7,2,44,11]
# for i in range(0,5):
#           print(marks[i])
print()
marks.append(99)   #add at last of the list 
marks.insert(1,400)  #insert in between list 
# for i in range(0,7):
#         print(marks[i] ," at index ----> " ,  i)

print(marks)
marks.remove(2)   #for remove element 
print(marks)
marks.pop()   #remove from the last 
print(marks)
marks.pop(3)  #haha removed at desired index #python
print(marks)
marks.sort()
print(marks)
marks.sort(reverse=True)    #sort in descending order 
print(marks)  
marks.append(11)
print(marks.count(11))
