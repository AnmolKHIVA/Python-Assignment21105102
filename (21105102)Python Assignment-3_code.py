print("\nQuestion-1:\n")

#Taking input from the user
string=str(input("Enter the Input string:"))
list1=string.split()
list_1=[]
for o in list1:
    lower_o=o.lower()
    list_1.append(lower_o)

set1=set(list_1)
dic={}
for op in set1:
    count=list_1.count(op)
    dic.update({op:count})
dic2={}
set2={1,2}
set2.clear()
list2=[]

if len(list1)==1:
    for elements in string:
        list2.append(elements)
    for op in list2:
        set2.add(op.lower())
    string_1=string.lower()
    for ele in set2:
        dic2.update({ele:string_1.count(ele)})

    print("Dictionary containing 'Letter':'Letter count':")
    print(dic2)
else:
    print("Dictionary containing {'Word':'Word Count'}:")
    print(dic)

#############################################################################################################################################################################

print("\nQuestion-2:\n")

print("Enter date below to get date of the next day")

def leap_year(x):

    if(x%400)==0 or ((x%100!=0) and (x%4==0)):
        return True
    else:
        return False

day=int(input("Enter Day [1-31]:"))
month=int(input("Enter Month[1-12]:"))
year=int(input("Enter Year[1800-2025]:"))

if day<1 or day>31 or month<1 or month>12 or year<1800 or year>2025:
    condition1=False
else:
    condition1=True

month_31=[1,3,5,7,9,11]
month_30=[4,6,8,10,12]

c1a=day==31 and (month in month_30)
c1b=day>29 and month==2
c1c=day==29 and (not leapyear(year) and month==2)
if c1a or c1b or c1c :
    condition2=False
else:
    condition2=True
if c1a:
    print(f"\nError\n{day} day cann't be in month{month}")
elif c1b:
    print(f"\nError\n{day}day can't be in month{month}")
elif c1c:
    print("\n\Error\n{day}day can't be in month {month} as the year{year} is nor leapyear")
elif condition1==False:
    print(f"\nError\nEnter date in the range [1-31]'month[1-12],year[1800-2025]")

if condition1==True and condition2==True:
    month_31=[1,3,5,7,9,11]
    month_30=[4,6,8,10,12]

    if(month in month_30)==True:
        if day==31:
            day=1
            month=month+1
        elif 1<= day <=30:
            day=day+1
    elif(month in month_30)==True:
        if day ==30 and month==12:
            day=1
            month=1
            year=year+1
        elif day==30 and month!=12:
            day=1
            month=month+1
        elif 1<= day<=29:
            day=day+1
    elif month==2: 
        if leap_year(year)==True:
            if day==29:
                day=1
                month=month+1
            elif 1 <= day <= 28:
                day=day+1
        elif leap_year(year)==False:
            if day==28:
                day=1
                month=month+1
            elif 1<= day<= 27:
                day= day+1
                              
    print(f"\nNext Date in format Day/Month/Year is:{day}/{month}/{year}")                      
            

###########################################################################################################################################################################

print("\nQuestion-3:\n")

#Input numbers
list1=list(map(int,input("Enter the numbers with space between them:").split()))
#Empty list
list2=[]
for i in list1:
    k=(i,i*i)
    list2.append(k)
print(list2)



#####################################################################################################################################################################

    
print("\nQuestion-4:\n")

while True:
    print("\nEnter grade of the student:\n")
    grade_point=input()
    if grade_point.isnumeric():
        if not (grade_point.isnumeric() and 4<int(grade_point)<=10):
            print("Input invalid.\nGrade should be an integer between 4 to 10.")
            continue
        else:
            break
    else:
        print("Input invalid. Grade should be an integer between 4 to 10.")
        
gradeDict={"10":(" A+ "," Outstanding "),
           "9":(" A "," Excellent "),
           "8":(" B+ "," Very Good "),
           "7":(" B "," Good "),
           "6":(" C+ "," Average "),
           "5":(" C "," Average "),
           "4":(" D "," Poor ")}
               
print('Your grade is',gradeDict[grade_point][0],'and performance is ',gradeDict[grade_point][1],".",sep='')




###########################################################################################################################################################################



print("\nQuestion-5:\n")

print("The required pattern :\n")

xyz="ABCDEFGHIJK"
#forming a list
list_xyz=[]
for i in xyz:
    list_xyz.append(i)
# Using loop to print desired rows    
k=1
while k<=6:
    for op in list_xyz:
        print(op,end="")
    list_xyz.pop(len(list_xyz)-1)
    list_xyz.pop(len(list_xyz)-1)
    list_xyz.insert(0," ")
    print()
    k=k+1




######################################################################################################################################################################


print("\nQuestion-6\n")

repeat="Y"
#Empty dictionary
dic={}
dic2={}
list=["Y","y","n","N"]
while repeat=="Y" or repeat=="y":
    name=str(input("Enter student name:"))
    sid=int(input("Enter student SID:"))
    if sid<0:
        print("SID can't be negative")
    else:
        dic.update({sid:name})
        dic2.update({name:sid})
        repeat=str(input("Enter Y to continue or N to end:"))
    if repeat=="N" or repeat=="n":
        break
    elif(not(repeat in list)):
        print("Please enter valid input['Y'or'N']")
        repeat=str(input("Enter Y to continue and N to end:"))
        
#Part a        
print("\nPart(a):\n")
print("The dictionary containing{'SID':Name}:")
print(dic)

#Part b
print("\nPart(b):\n")
list_k=sorted(dic2)
dic3={}
for op in list_k:
    dic3.update({dic2.get(op):op})
print("The dictionary after sorting according to name:")
print(dic3)

#Part c
print("\nPart(c):\n")
sort_dic=sorted(dic)
dic4={}
for op in sort_dic:
    dic4.update({op:dic.get(op)})
print("The dictionary after sorting according to SID:")
print(dic4)

#Part d
print("\nPart(d):\n")
enter_sid=int(input("Enter SID to get name of the student:"))
output_name=str(dic.get(enter_sid))
#Output name using SID of the student
print(f"Name of student with SID {enter_sid} is {output_name}.")      

      
#################################################################################################################################################################


print("\nQuestion-7\n")

n=int(input("Number of elements required in fionacci sequence:"))

if n<=0:
    print("Number of elements can not be less than or equal to zero")

else:
    if n==1:
        print("The Fibonacci sequence with one element is\n[1]")
        print("Average of series is:",1)

    elif n==2:
        print("The Fibonacci sequence with two elements is\n[1,1]")
        print("Average of series is:",1)

    else:
        list1=[1,1]

        a=1
        b=1

        for i in range(n-2):
            s=a+b
            list1.append(s)
            a=b
            b=s
        print("The Fibonacci sequence with {n} elements is: ")
        print(list1)

        sum=0
        for num in list1:
            sum=sum+num
        average=(sum/n)
        print("Average of Fibonacci Sequence is",average )



#############################################################################################################################################################################


print("Question-8:\n")
Set1={1,2,3,4,5}
Set2={2,4,6,8}
Set3={1,5,9,13,17}

print("\nPart(a):\n")

print("Set of all elements that are in Set1 and Set2 but not both:\n")
#symmertic difference of Set1 and Set2
new_set=Set1.symmetric_difference(Set2)
print("Required set is:",new_set)

print("\nPart(b):\n")

print("Set of all elements that are in only one of the three sets Set1,Set2 and Set3:\n")

#Union of Set1 and Set2
set_u12=Set1|Set2

#Union of Set1 and Set2 and Set3
set_u123=set_u12|Set3

#Intersection of Set1 and Set2
set_i12=Set1&Set2

#Intersection of Set2 and Set3
set_i23=Set2&Set3

#Intersection of Set1 and Set3
set_i13=Set1&Set3

##Intersection of Set1 and Set2 and Set3
set_i123=set_i12&Set3

new_set2=set_u123-set_i12-set_i23-set_i13
print("Required set is:",new_set2)

print("\nPart(c):\n")

new_set3=(set_i12|set_i23|set_i13)-set_i123
print("Required set is:",new_set3)

print("\nPart(d):\n")

print("Set of all integers in the range 1 to 10 that are not in Set1:\n")

set_d={1,2}
set_d.clear()
for i in range(1,11):
    set_d.add(i)
new_set4=set_d-Set1

print("Required set is:",new_set4)

print("\nPart(e):\n")

print("Set of all integers in the range 1 to 10 that are not in Set1, Set2 and Set3:\n")

new_set5=set_d-set_u123
print("Required set is:",new_set5)


        
            
        
