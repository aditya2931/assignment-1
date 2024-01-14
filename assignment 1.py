#!/usr/bin/env python
# coding: utf-8

# ## Python Basic Programming Exercises
Q1: What is the output of following expression
    5 + 4 * 9 % (3 + 1) / 6 - 1
# In[1]:


print(5 + 4 * 9 % (3 + 1) / 6 - 1)

Q2: Write a program to check if a Number is Odd or Even. Take number as a input from user at runtime.
# In[1]:


n=int(input("Enter a number:"))
if n%2==0:
    print("even")
else:
    print("odd")

Q3: Write a program to display the multiplication table by taking a number as input. 
    [Hint : Use print statement inside of a loop]
# In[2]:


n=int(input("Enter the number:"))
for i in range(1,11):
    print(str(n)+'*'+str(i)+'=',(n*i))

Q4: Write a program which will find all numbers between 2000 and 3200 which are divisible by 7 
    but are not a multiple of 5.
 
Note: The numbers obtained should be printed in a comma-separated sequence on a single line.
# In[4]:


for i in range(2000,32001):
    if i%7==0 and i%5!=0:
        print(i,end=' , ')

Q5: Count the elements of each datatype inside the list and display in output
    [2, 3, 'Py', '10', 1, 'SQL', 5.5, True, 3, 'John', None, 7]    
# In[5]:


li=[2, 3, 'Py', '10', 1, 'SQL', 5.5, True, 3, 'John', None, 7] 
count_int=0
count_str=0
count_float=0
count_none=0
count_bool=0
for i in li:
    if type(i)==int:
        count_int+=1
    elif type(i)==float:
        count_float+=1
    elif type(i)==str:
        count_str+=1
    elif type(i)==bool:
        count_bool+=1
    else:
        count_none+=1
print('int : ',count_int)
print('float : ',count_float)
print('str : ',count_str)
print('bool : ',count_bool)
print('NoneType : ',count_none)

Q6: Add all values from the list with numeric datatypes 
    [2, 3, 'Py', '10', 1, 'SQL', 5.5, True, 3, 'John', None, 7] 
# In[6]:


li=[2, 3, 'Py', '10', 1, 'SQL', 5.5, True, 3, 'John', None, 7] 
sum=0
for i in li:
    if type(i)==int or type(i)==float:
        sum=sum+i
print(sum)
    

Q7: Concat all str datatypes with hyphen as a delimiter
    [2, 3, 'Py', '10', 1, 'SQL', 5.5, True, 3, 'John', None, 7] 
# In[7]:


li=[2, 3, 'Py', '10', 1, 'SQL', 5.5, True, 3, 'John', None, 7] 
u=''
for i in li:
    if type(i)==str:
        u=u+i+'-'
print(u)

Q8: Write a UDF that takes list as input and returns sum of all numbers 
    (exclude bool) and count of all str 
    [2, 3, 'Py', '10', 1, 'SQL', 5.5, True, 3, 'John', None, 7] 
    
Hint:
-----
def my_func:
    # your code
        
my_func(l1)
# output --> {'Sum': xxx, 'Count_of_Strs': xxx}
# In[8]:


def my_func(li_):
    sum=0
    count=0
    for i in li_:
        if type(i)==int or type(i)==float:
            sum=sum+i
        if type(i)==str:
            count=count+1
    dic={'Sum':sum ,'Count_of_Strs':count }
    print(dic)
li=[2, 3, 'Py', '10', 1, 'SQL', 5.5, True, 3, 'John', None, 7] 
my_func(li)
    
    
    
        

Q9: Get only odd numbers from the following list and store the numbers in new list
    li = [5, 7, 22, 97, 54, 62, 77, 23, 73, 61]

    i. Use loops to get the answer
   ii. Use list comprehensions
  iii. Use lambda function with filter
# In[9]:


li = [5, 7, 22, 97, 54, 62, 77, 23, 73, 61]
odd_numbers=list(filter(lambda i :(i%2!=0),li))
print(odd_numbers)

Q10: Write a UDF to return the descriptives [sum, count, min, mean, max] for a list of n number of input 
    numbers.
# In[10]:


def manipulation(li_):
    sum=0
    count=0
    for i in li_:
        sum=sum+i
        count=count+1
    s=[sum,count,min(li_),(sum/count),max(li_)]
    print(s)
n=int(input("Number of integers:"))
a=[]
for i in range(n):
    i=int(input())
    a.append(i)
manipulation(a)
    

    

Q11: Write an udf to calculate the area of different shapes

Take shape and dimensions as arguments to udf as follows : 

1. square which has side
2. rectangle which has length and width
3. circle which has radius

The shape should be a positional argument and it's dimensions are taken as kwargs

Perform proper validation for the user inputs and then calculate area.

E.g. if shape is square, ensure kwargs has "side" and if so, then you may return the area, else display appropriate error message like "Please enter 'side' for a square"
# In[3]:


def area(name,**kwargs):
    if name not in ['Square','Rectangle','Circle']:
        print("Enter valid shape : ")
    else:
        if name=='Square':
            if "side" in kwargs:
                print('Area of square is ', kwargs['side']*kwargs['side'])
            else:
                print('Please enter valid side:')
        elif name=='Rectangle':
            if 'length' in kwargs and 'width' in kwargs:
                print('Area of rectangle is ',kwargs['length']*kwargs['width'])
            else:
                print('Please enter length and width of rectangle:')
        elif name=='Circle':
            if 'radius' in kwargs:
                print('Area of circle is ',3.14*kwargs['radius']*kwargs['radius'])
            else:
                print('Please enter radius of circle:')
area('Square',side=2)
area('Rectangle',length=4,width=5)
area('Circle',radius=14)
    

Q12: Write a UDF to reconcile the values within two lists.
    l1 = ['January', 'February', 'March', 'May', 'June', 'September', 'December']
    l2 = ['January', 'February', 'April', 'June', 'October', 'December']

Hint:
-----
def func(l1, l2):
    your code here...
    
Output:
{'Matched': ['January', 'February', 'June', 'December'],
    'Only in l1': ['March', 'May', 'September'],
        'Only in l2': ['April', 'October']}
# In[12]:


l1 = ['January', 'February', 'March', 'May', 'June', 'September', 'December']
l2 = ['January', 'February', 'April', 'June', 'October', 'December']
a=[]
b=[]
out={'Matched':a,'Only in l1':b,'Only in l2':l2}
for i in l1:
    if i in l2:
        a.append(i)
        l2.remove(i)
    elif i not in l2:
        b.append(i)
print(out)  


Q13: write a UDF to check if a number is prime or not.
# In[4]:


def primenumber(num):
    for i in range(2,num+1):
        if num==2:
            print('prime')
        else:
            if num%i!=0:
                print('prime')
                break
            
                
            else:
                print('not prime')
                break
    
            
        
n=int(input("Enter a number"))
primenumber(n)
            

Q14. Write a program which can compute the factorial of a given numbers. 
#   The results should be printed in a comma-separated sequence on a single line. 
# input() function can be used for getting user(console) input


#Suppose the input is supplied to the program:  8  
#Then, the output should be:  40320 
#Hints: In case of input data being supplied to the question, it should be assumed to be a console input. 

# In[5]:


def factorial(num):
    fact=1
    for i in range(1,num+1):
        fact=fact*i
    print(fact)
n=int(input("Enter the number:"))
factorial(n)

Q15. With a given integral number n, write a program to generate a dictionary that contains (i, i*i) such that is an integral number between 1 and n (both included). and then the program should print the dictionary.

#Suppose the following input is supplied to the program: 8
#Then, the output should be: {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64}
#Hints: In case of input data being supplied to the question, it should be assumed to be a console input. Consider using dict()


# In[15]:


my_dict={}
n=int(input("Number of inputs"))
for i in range(n):
    key=int(input("Enter the key"))
    value=key*key
    my_dict[key]=value
print(my_dict)



Q16. Write a program which accepts a sequence of comma-separated numbers from console and generate a list and a tuple which contains every number.
#Suppose the following input is supplied to the program: 34,67,55,33,12,98
    #Then, the output should be: ['34', '67', '55', '33', '12', '98'] ('34', '67', '55', '33', '12', '98')

#Hints: In case of input data being supplied to the question, it should be assumed to be a console input. you may use tuple() method to convert list to tuple

# In[16]:


li=[]
tup=()
n=int(input("Enter the number of values:"))
for i in range(n):
    num=int(input("Enter the number:"))
    li.append(num)
    tup=tup+(num,)
print(li,end=' ')
print(tup)
    

Q17. Write a program that accepts a comma separated sequence of words as input and 
# prints the words in a comma-separated sequence after sorting them alphabetically.

# Suppose the following input is supplied to the program: without,hello,bag,world
# Then, the output should be: bag,hello,without,world

#Hints: In case of input data being supplied to the question, it should be assumed to be a console input.

# In[17]:


enter_string=input("Enter the string : ")
words=enter_string.split(',')
words.sort()
output_string = ",".join(words)
print(output_string)

Q18. Write a program that accepts a sequence of whitespace separated words 
# as input and prints the words after removing all duplicate words and sorting them alphanumerically.
# Suppose the following input is supplied to the program: hello world and practice makes perfect and hello world again
# Then, the output should be: again and hello makes perfect practice world

#Hints: In case of input data being supplied to the question, it should be assumed to be a console input.
#We use set container to remove duplicated data automatically and then use sorted() to sort the data.

# In[18]:


enter_string=input("Enter the string : ")
s=[]
words=enter_string.split(' ')

for i in words:
     if i not in s:
            
            s.append(i)

s.sort()

output_string=' '.join(s)
print(output_string)

Q19. Write a program that accepts a sentence and calculate the number of upper case 
# letters and lower case letters.
#Suppose the following input is supplied to the program: Hello world!
#Then, the output should be: UPPER CASE 1 LOWER CASE 9

#Hints: In case of input data being supplied to the question, it should be assumed to be a console input.

# In[19]:


s=input("Enter the string : ")
count_u=0
count_l=0
for i in s:
    if i.isupper():
        count_u=count_u+1
    if i.islower():
        count_l=count_l+1
print("UPPER CASE ",count_u,end=' ')
print("LOWER CASE",count_l)

Q20. Write a program that takes a string and returns reversed string. i.e. if input is "abcd123" output should be "321dcba"
# In[20]:


s=input("Enter your string : ")
u=''
for i in range(len(s)-1,-1,-1):
    u=u+s[i]
print(u)
    


# In[ ]:




