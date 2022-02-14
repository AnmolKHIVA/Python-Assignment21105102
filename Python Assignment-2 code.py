print("Question-1\n")

print("\n(Part-a):")
string="Python is a case sensitive language"
print("length of string:",len(string))
print("\n(Part-b):")
print(string[::-1])
print("\n(Part-c):")
print(string[10:26])
print("\n(Part-d):")
print(string.replace("a case sensitive","object oriented"))
print("\n(Part-e):")
print(string.index("a"))
print("\n(Part-f):")
print(string.replace(" ",""))

##################################################
 
print("Question-2\n")

name="Anmolpreet Singh"
SID="21105102"
department="Electronics and Communication Engineering"
CGPA="9.9"

print(f"Hey,{name} here \nMy SID is {SID} \nI am from {department}  department and my CGPA is {CGPA}.") 


#####################################################


print("Question:3\n")

a=56
b=10
print("a&b:",a&b)
print("a|b:",a|b)
print("a^b:",a^b)

print("Left shift both a with 2 bits")
print("a<<2:",a<<2)

print("Left shift both b with 2 bits")
print("b<<2:",b<<2)

print("Right shift a with 2 bits")
print("a>>2:",a>>2)

print("Right shift b with 4 bits")
print("b>>4:",b>>4)



##########################################################


print("Question-4\n")

num1=float(input("Enter first number:"))
num2=float(input("Enter second number:"))
num3=float(input("Enter third number:"))
if (num1>num2) and (num2>num3):
     greatest_number=num1
elif (num2>num1) and (num2>num3):
     greatest_number=num2
else:
     greatest_number=num3
print("The greatest number is:",greatest_number)


##############################################################


print("Question-5\n")

string1="My name is Virat Kohli"
string2="I am an excellent cricketer"
if "name"in string1:
    print("Yes")
else:
    print("No")
if "name"in string2:
    print("Yes")
else:
    print("No")


###################################################################

print("Question-6\n")

s1=int(input("Length of first side:"))
s2=int(input("Length of second side:"))
s3=int(input("Length of third side:"))

#Checking whether the given sides form a triangle or not

if s1+s2>s3 and s2+s3>s1 and s3+s1>s2 : 
    print("Yes,the triangle is possible")
else:
    print("No,the triangle is not possible")

    
    
    




