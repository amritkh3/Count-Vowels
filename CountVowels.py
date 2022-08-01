"""wap to ask user to enter any word and return a number of vowels in  it.
1.declare a variable vowels and assiign it with thw value aeiou
2.ask user to input the word and assign it with the variable word
3.declare a variable total and asiign it withe value 0
4.run for loop on ever index of word
5. under for loop use if condition 
 if index in vowel
    total= total+1
6.print the value of total after the loop end which will be the total no of 
vowels inthe word
    
"""


vowels="aeiou"
word=input("enter any word ")
total=0
for index in word:
   if index in vowels:
      total=total+1
print("total no of vowels is ",total)    
   





   