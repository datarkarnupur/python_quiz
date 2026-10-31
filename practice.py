
"""a=int(input("enter a number"))
if a>0:
    print("number is positive number")
elif a<0:
    print("number is negative number")
else:
    print("number is zero")
test_score=int(input("enter a test score"))
if test_score>=50:
    print("you passed the test")
else:
    print("you did'nt passed")
a=int(input("enter a number a"))
b=int(input("enter a number b"))
if a>b:
    print("a is largest")
else:
    print("b is largest")
student_score=int(input("enter your score"))
if student_score>=90:
    print("Grade A")
elif student_score>=80 and student_score<90:
    print("Grade B")
elif student_score>=70 and student_score<80:
    print("Grade c")
else:
    print("Grade D")
year=int(input("enter the year"))
if year%4==0:
    print("it is a leap year")
elif year%400==0:
    print("it is aleap year")
else:
    print("it is not leap year")
a= int(input("enter first angle"))
b=int(input("enter  second angle"))
c=int(input("enter third angle of triangle"))
if a+b+c!=180 or a<=0 or b<=0 or c<=0:
    print("triangle is invalid")
elif a==b==c:
    print("triangle equileral triangle")
elif a==b or a==c or b==c:
    print(" triangle is isosceles")
else:
    print("triangle is scelene")
a=float(input("enter the first number:"))
b=float(input("enter a second number:"))
op=input("enter the operation(+,-,/,*):")
if op=="+":
    print("result=",a+b)
elif op=="-":
    print("result=",a-b)
elif op=="*":
    print("result=",a*b)
elif op=="/":
    if b==0:
        print("can't divisible by 0")
    else:
        print("result=",a/b)
else:
    print("invalid operation")
import random
secret_number=random.randint(1,100)
print("welcome to number guessing game")
print("guess the number between 1 to 100")

while True:
    guess=int(input("enter your guess"))

    if guess<secret_number:
        print("too low")
    elif guess>secret_number: 
        print("too hight")
    else:
        print("congratulation! you guessed it ")

a=5
b=8
a,b=b,a
print(a," ",b)

first_name=input("enter your name")
last_name=input("enter your last name")
print("hello",first_name,last_name,"!")

a=10
b=4

print("sum=",a+b)
print("diff=",a-b)
print("mul",a*b)
print("division",a/b)

a=5
if a%2==0:
    print("the  number is even number")
else:
    print("the number is odd number")

a=int(input("enter a first number"))
b=int(input("enter a second number"))
c=int(input("enter a third number"))

if a>b and a>c:
    print("a is largest number")
elif b>a and b>c:
    print("b is largest number")
else:
    print("c is largest number")

score=int(input("enter your score"))
while True:
    if 100>score>=90:
        print("grade A")
    elif 90>score>=80:
        print("grade B")
    elif 80>score>=70:
        print("grade c")
    elif 70>score>=60:
        print("grade D")
    elif 60>score>=0:
        print("grade F")
    else:
        print("invalide score")
    print("congrates")
    break"""
print("===================================")
print("           Quiz game               ")
print("===================================")

name=input("enter your name")
print("welcome to python quiz",name)
score=0
Total_que=10

print("answer each que using A,B,C,D")

print("1.which of the following data types in python is immutable?")
print("A.list")
print("B.dictionary")
print("C.Tupple")
print("D.set")
answer=input("enter your answer")