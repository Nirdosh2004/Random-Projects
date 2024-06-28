# isalpha()
# isdigit()
# isalnum()
# islower()
# isupper()
# startwith()
# endwith()

# names = "SARFARAJ ANSARI"
# print(names.lower())
# print(names.upper())
# import string

sentence = input("Enter your name: ")
checker = sentence.startswith(('a' , 'e' , 'i' , 'o' , 'u')) 
print(checker)
if(checker == True):
          print(sentence + "'s first letter is Vowel")
else:
        print( sentence + "'s first letter is Consonent")
