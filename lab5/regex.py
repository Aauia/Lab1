import re
#ex1
'''
n = input()
a = re.search("ab*", n)
if a:
    print("matched")
else:
    print("not matched")

#ex2

n = str(input())
a = re.match("a(bbb?)", n)
if a:
    print("matched")
else:
    print("not matched")

#ex3

n = str(input())
a = re.findall("[a-z]+_", n)
print(a)

#ex4

n = str(input())
a = re.findall("[a-z]+[A-Z]", n)
print(a)

#ex5

n = str(input())
a = re.match("a.*b$", n)
if a:
    print("matched")
else:
    print("not matched")

#ex6

n = str(input())
a = re.sub("\s|[,]|[.]", ":", n)
print(a)

#ex7

n = input()
a = re.sub("_([a-z])", lambda a: a.group(1).upper(), n)
print(a)

#ex8

n = input()
a = re.findall("[A-Z][^A-Z]*", n)
print(a)

#ex8

n = input()
a = re.findall("[A-Z][^A-Z]*", n)
print(a)

#ex9

n = input()
a = re.sub("([A-Z])", r" \1", n)
print(a)

#ex10

n = input()
a = re.sub("([a-z])([A-Z])", r"\1_\2", n)
print(a.lower())
'''
file = open("row.txt", "r", encoding= "utf-8")
print(file.readlines())