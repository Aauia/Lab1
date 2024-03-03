# ex 1
ar = [1, 2, 3, 4, 5]
y = "*".join(str(i) for i in ar)
print(eval(y))

# ex 2
n = input()
up = 0
low = 0
for i in n:
    if i.isupper():
        up += 1
    elif i.islower():
        low += 1
print("Uppercase letters: ", up)
print("Lowercase letters: ", low)

# ex 3
n = input()
if n == n[::-1]:
    print("String is palindrome")
else:
    print("String is not palindrome")

# ex 4
import time
num = int(input())
milsec = int(input())
sec = milsec / 1000
time.sleep(sec)
sqrt = num**0.5
n = "Square root of {fnum} after {fsec} is {fsqrt}".format(
    fnum=num, fsec=milsec, fsqrt=sqrt
)
print(n)

# ex 5
a = (True, True, False)
b = (True, True, True)
print(all(a))
print(all(b))