s#program for max number of three from given inputs
def got(num1,num2,num3):
    return max(num1,num2,num3);
num1=float(input("enter first number "));
num2=float(input("enter second number "));
num3=float(input("enter third number "));
l=got(num1,num2,num3);
print(l);

#program for greatest number 
n=int(input());
max=0
for i in range(n):
    a=int(input())
if a>=max:
    max=a
    print("greatest number is",max)

# #3--reversal of a given input
n=input()
rev=""
for i in n:
    rev=i+rev
print(rev)

#program to print fibonacci series until range NN
n=int(input());
a=0
b=1
for i in range(n):
    c=a+b
    print(c,end=',')
    a=b
    b=c

#program to find factors of a given Number
n=int(input())
for i in range(1,n+1):
    if n%i==0:
        print(i,end=" ")


