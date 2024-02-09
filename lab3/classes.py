#ex1
class methods:
    def init(self):
        self.d=""
    def getstring(self):
        self.d = input()
    def printstring(self):
        print(self.d.upper())
s = methods()
s.getstring()
s.printstring()

#ex2
class S(object):
     def init(self):
         pass
     def area(self):
         return 0
class Ss(S):
     def init(self, length):
         S.init(self)
         self.length=length
     def area(self):
         return self.length*self.length
aSq= Ss(4)
print(aSq.area())

#ex3
class S(object):
     def init(self):
         pass 
     def area(self):
         return 0
class rectangle(S):
    def init(self, length , width):
        S.init(self)
        self.length=length
        self.width=width
    def area(self):
        return self.length*self.width
aSq= rectangle(4,7)
print(aSq.area())
    
#ex4
class p:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def show(self):
        print(f'({self.a}, {self.b})')

    def move(self, na, nb):
        self.x = na
        self.y = nb

    def dist(self, other):
        distance = ((self.a - other.a)**2 + (self.b - other.b)**2) ** 0.5
        return distance 

p1 = p(2, 3)
p2 = p(5, 7)
p1.show()
p1.move(8, 11)
print(p1.dist(p2))


#ex5
class Bank:
    def _init_(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited {amount}. Balance: {self.balance}")

    def withdraw(self, amount):
        if amount > 0:
            if amount <= self.balance:
                self.balance -= amount
                print(f"Withdrew {amount}. Balance: {self.balance}")
            else:
                print("Withdrawal not allowed.")

a= input()
b = int(input()) 
ac = Bank(a, b)

d = int(input()) 
w = int(input())
ac.deposit(d)
ac.withdraw(w)

#ex6
def prime(n):
    if n <= 1:
        return False
    elif n == 2:
        return True
    elif n % 2 == 0:
        return False
    else:
        for i in range(3, int(n**0.5) + 1, 2):
            if n % i == 0:
                return False
        return True
numbers = input().split()
numbers = list(map(int, numbers)) 
prime_numbers = list(filter(lambda x: prime(x), numbers))
print( prime_numbers)