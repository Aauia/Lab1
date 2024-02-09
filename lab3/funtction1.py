# ex 1 
def ounce(g):
    print(g*28.3495231)

g=float(input())
ounce(g)

# ex 2
def ftc(f):
    s=(5/9)*(f-32)
    print(s)

f=float(input())
ftc(f)


# ex 3 
def ma(h,l):
    y= (l-(2*h))/2 
    x=h-y
    print(x,y)

h=int(input())
l=int(input())
ma(h,l)  



# ex 4 

def pf(a):
    b=[]
    for i in  a:
        s=0 
        for j in range(1,i+1):
            if i % j==0:
                s+=1
        if s==2:
            b.append(i)
    for i in b:
        print(i)


from array import array 
a = array('i')
a=list(map(int,input().split()))
pf(a)

#ex 5
def p(string, prefix=""):
    if len(string) == 0:
        print(prefix)
    else:
        for i in range(len(string)):
            p(string[:i] + string[i+1:], prefix + string[i])

i = input()
p(i)


#ex 6
def r(s):
    return s[::-1]

s = input()
print(r(s))

#ex 7
def has_33(n):
    for i in range(len(n) - 1):
        if n[i] == 3 and n[i + 1] == 3:
            return True
    return False

a = input()
n = [int(x) for x in a.split()]

result = has_33(n)
print(result)

#ex 8
def spy_game(n):
    c = 0
    for i in n:
        if i == 0 and c < 2:
            c += 1
        elif n == 7 and c == 2:
            return True
    return False

a = input()
n = [int(x) for x in a.split()]

result = spy_game(n)
print(result)





#ex 9
def volu(r):
    n=4*(3.14)*(r^3)
    print(n)
            

r=int(input())  
volu(r) 



#ex 10
def unique_elements(n):
    d = []
    for i in n:
        if i not in d:
            d.append(i)
    return d

a = input()
n = [int(x) for x in a.split()]

result = unique_elements(n)
print(result)


#ex 11
def palindrome(d):
    m = d[::-1]
    if m == d:
        print("Yes")
    else:
        print("No")

d= str(input())
r = palindrome(d)

#ex 12
def histogram(x, y, z):
    for i in range(1, x + 1):
        print("*", end=' ')
    print()

    for i in range(1, y + 1):
        print("*", end=' ')
    print()

    for i in range(1, z + 1):
        print("*", end=' ')

x = int(input())
y = int(input())
z = int(input())
histogram(x, y, z)

#ex 13
import random 

def guess_the_number(name):
    n = random.randint(1,20)
    a = 0
    while True:
        m = int(input())
        a += 1
        if m == n:
            print(f"Good job, {name}! You guessed my number in {a} guesses!")
            break
        elif m<n:
            print("Your guess is too low. Take a guess")
        elif m>n:
            print("Your guess is too big. Take a guess")



name = (input("Hello! What is your name? "))
print("Well,", name, ", I am thinking of a number between 1 and 20. Take guess")

n = guess_the_number(name)
 

from ex4 import histogram
