"""

*** You must write a comment for every chunk of code you write from now on along with your author tag***
4-6
Create a Python file named lab_4-6.py
Write a program that asks for user input for an animal and a dish. 
Your program should print true or false to indicate whether the beast is allowed to bring the dish to the feast 
(the first letter of the animal is the same as the first and last letter of the dish).
Assume that beast and dish are always lowercase strings, and that each has at least two letters. 
beast and dish may contain hyphens and spaces, but these will not appear at the beginning or end of the string. They will not contain numbers.

"""


#author: Jon Morris
animal - input("What animal are you?") dish - input("What dish would you like?")
if animal [0] - dish[0]
print("true")
else:
print("false") 


_________________________________________________
"""
4-7
Create a Python file named lab_4-7.py
Write a program that prompts a uses 5 inputs to prompt a user for a number. 
Store all numbers as a single string with a space in between each numbers 
(i.e num_string = ‘1 2 3 4 5’). Print this string. Using string methods, 
extract the smallest and largest number from the string & print them, 
with a label (i.e smallest num given was 1). 
Print the product of the two numbers you have extracted, with a label (i.e. the product of the two numbers extracted was 5).
"""


num1 = int (input ("what is your first numnber?"))
num2 = int (input ("what is your second numnber?"))
num3 = int (input ("what is your third numnber?"))
num4 = int (input ("what is your fourth numnber?"))
num5 = int (input ("what is your fifth numnber?"))
num_string = "{0}, {1}, {2}, {3}, {4}".format(num1, num2, num3, num4, num5)
print (num_string)

num_list + [num1, num2, num3, num4, num5]
num_list.sort()
lownum = numlist[0]
highnum = numlist[4]
multnum = lownum + highnum
print ("the lowest number given was " + str(lownum))
print ("the highest number given was " + str(highnum))
print ("the product of the highest and lowest number was " + str(multnum))



___________________________________________________
"""
4-8
Create a Python file named lab_4-8.py
Write a program that prompts a use to enter a 6 letter sequence of DNA. (a series of a,c,t,g) 
Print out the complementary DNA sequence (a – t, c – g). 
You can assume all inputs are valid and lowercase



"""

#author: Jon Morris
dna0 = input("what is the first in the sequence?")
dna1 = input("what is the second in the sequence?")
dna2 = input("what is the third in the sequence?")
dna3 = input("what is the fourth in the sequence?")
dna4 = input("what is the fifth in the sequence?")
dna5 = input("what is the last in the sequence?")
             
if dna0 == "a":
    dna0 = "a-t"
elif dna0 == "c":
    fdna0 = "c-g"
elif dna0 == "t":
    fnda0 = "a-t"
elif dna0 == "g":
    fnda0 = "c-g"

if dna1 == "a":
    dna1 = "a-t"
elif dna1 == "c":
    fdna1= "c-g"
elif dna1 == "t":
    fnda1 = "a-t"
elif dna1 == "g":
    fnda1 = "c-g"

if dna2 == "a":
    dna2 = "a-t"
elif dna2 == "c":
    fdna2= "c-g"
elif dna2 == "t":
    fnda2 = "a-t"
elif dna2 == "g":
    fnda2 = "c-g"

if dna3 == "a":
    dna3 = "a-t"
elif dna3 == "c":
    fdna3= "c-g"
elif dna3 == "t":
    fnda3 = "a-t"
elif dna3 == "g":
    fnda3 = "c-g"

if dna4 == "a":
    dna4 = "a-t"
elif dna4 == "c":
    fdna4= "c-g"
elif dna4 == "t":
    fnda4 = "a-t"
elif dna4 == "g":
    fnda4 = "c-g"

if dna5 == "a":
    dna5 = "a-t"
elif dna5 == "c":
    fdna5= "c-g"
elif dna5 == "t":
    fnda5 = "a-t"
elif dna5 == "g":
    fnda5 = "c-g"

flist - "(0), (1), (2), (3), (4), (5)".format(fdna0, fnda1, fdna2, fdna3, fdna4, fdna5)
print(flist)