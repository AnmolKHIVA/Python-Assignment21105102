print("ASSIGNMENT-4\n")

print("\nQuestion-1:\n")

print("")
def Tower_of_Hanoi( n , initial , final , aux ):
    if n==0:
        return

    Tower_of_Hanoi( n-1, initial , aux , final )
    print(f"Move Disc Number {n} from {initial} to {final}")
    Tower_of_Hanoi( n-1 , aux , final , initial )
    
#function calling    
Tower_of_Hanoi(3,'A','C','B')
print()



############################################################################################################################


print("\nQuestion-2:\n")

n=int(input("Enter the number of rows in Pascal's triangle:"))

print("\nPascal's triangle using loops:\n")

for line in range(1,n+1):

    print(' '*(n-line),end='')

    x=1
    for i in range(1, line+1):

        print(x,end=' ')

        x=x*(line-i)//i
    print()


print("\nPascal's Triangle using Recursions:\n")

def Pascal_Triangle(n,originaln=n):
    if n==0:
        return

    Pascal_Triangle(n-1,originaln)

    print(' '*(originaln-n),end=' ')

    entry=1
    for i in range(1,n+1):

        print(entry,end=' ')

        entry=entry*(n-i)//i
    print()
Pascal_Triangle(n)    


###################################################################################################################################



print("\nQuestion-3:\n")

a=int(input("Enter the first integer: "))
b=int(input("Enter the second integer: "))

c=a%b
d=a//b

print("The Remainder is: ",c)
print("The Quotient is: ",d)
if (c!=0):
    if (d!=0):
        print("Both the values are non zero ")
    else:
        print("Both values are zero")
else:
    if d!=0:
     
        print("One value is zero")
    else:
        print("Both values are zero")
set1=set()
for i in range (4,7):
    f=c+i
    g=d+i
    if(f>4):
        set1.add(f)
        print(set1)
    if(g>4):
        set1.add(g)
        print(set1)

print(set1)
set2=frozenset(set1)
print("Immutable set: ", frozenset(set1))
print("Largest value in the set: ", max(set2))
k=max(set2)
print("Hash value: ", hash(k))
print("")



############################################################################################################################################


print("\nQuestion-4:\n ")


class Student:
    def __init__(self, student, sid):
        self.name = student
        self.sid = sid
    
    def __del__(self):
        print("Object is Destroyed")

#object  Created
student1 = Student("Anmolpreet Singh" , 21105102)
print("Object is created")

#Assigned values are printed
print(f"The name of the student is {student1.name} and SID is {student1.sid}.")

#Object  deleted
del student1



##############################################################################################################################################


print("\nQuestion-5:\n")

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
    
    def __del__(self):
        print(f"Employee {self.name} record deleted")

#creating the records of employees

employee1 = Employee("Mehak", 40000)
employee2 = Employee("Ashok", 50000)
employee3 = Employee("Viren", 60000)

# updating the salary in Part(a)

employee1.salary = 70000
print(f"a. The updated salary of the employee {employee1.name} is {employee1.salary}")

#deleting a record in part(b)

print("b. ", end='')
del employee3


#####################################################################################################################################################


print("\nQuestion-6:\n")


#taking input of the word from one of the friend

word = input("Enter the first word: ")

#Input a meaningful word for friendship test

testword = input("\nEnter a new meaningful word to test your friendship: ")

#defining dictionary from last assignment

def count_in_dict(word):
    count = {}
    list1 = list(word)
    
    n = len(list1)
    for i in range(n):
        if list1[i] in count:
            count[list1[i]] += 1
        else:
            count[list1[i]] = 1
    return count

#Verifying the letters of the new word

if count_in_dict(word) != count_in_dict(testword):
    print("The letters are not same and the Friendship is Fake!!")

#shopkeeper's input to verify the word's meaning

def userinput():
    ans = input("\nDoes the word makes sense?(y or n)\n")

    if ans == 'y':
        print("The friends pass the friendship test!!\n\n")
    elif ans == 'n':
        print("The word has no meaning, friendship is fake!!\n\n")
    else:
        print("The input is invalid , Please try again")
        userinput()
userinput()
print("")

###################################################################################################################################################

