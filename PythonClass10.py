String 
___________
'abc'  "abc" '125'  "125"

s="ram"
print(s)

o/p:
ram

s='ram'
print(s)

s='''ram
das'''
print(s)
o/p:
ram 
das


s="""ram
das"""
print(s)


o/p:
ram 
das


s='ram 
das'
print(s)
o/p:
error

s="r'a'm"
print(s)
o/p:
r'a'm


s='r"a"m'
print(s)
o/p:
r"a"m


s="r"a"m"
print(s)
o/p:
error


s="r\"a\"m"
print(s)
o/p:
r"a"m


s='welcome'
print(type(s))
o/p:
<class 'str'>


s="welcome"
print(type(s))
o/p:
<class 'str'>

s="welcome"
print(s)

o/p:
welcome

indexing
_________
s="welcome"
print(s[3])
o/p:
c


0 1  2  3 4   5      6  +ve index
w e  l  c o   m      e
-7-6 -5 -4-3 -2     -1   -ve index

s="welcome"
print(s[3],s[-4])
print(s[5],s[-2])
o/p:
c c
m m

s="welcome"
print(s[7]) # error
print(s[-9]) # error

o/P:
error

slicing
_____________

stringname[start:stop:step]
stringname[start:stop]
stringname[start:]
stringname[value]  ->index


s="welcome"
print(s[2:5:1])
print(s[-5:-2:1])

O/p:
lco
lco

s="welcome"
print(s[0:5:1])
print(s[0:5])
print(s[0:])
print(s[0])
print(s[0::2])
print(s[-7::2])

o/p:
welco
welco
welcome
w
wloe
wloe


s="welcome"
print(s[0:])
print(s[0::1])
print(s[-7::1])
print(s[:])
print(s[::])

o/p:
welcome
welcome
welcome
welcome
welcome

s="welcome"
print(len(s))
print(s[0:100:])
print(s[0:len(s):])

o/p:
7
welcome
welcome

s="welcome"
print(s[5:2:-1])
print(s[-2:-5:-1])
print(s[::-1])
print(s[::-2])
print(s[-1::-1])
print(s[6::-1])
print(s[-1:-len(s)-1:-1])


o/p:
moc
moc
emoclew
eolw
emoclew
emoclew
emoclew



s="welcome"
print(s[-4:-6])
print(s[-4:-6:-1])
print(s[5:2])
print(s[5:2:-1])
o/p:

cl

moc

operator use in string
______________________
s="hi"
print(s+3)

o/p:
error

repation operator (*)

s="hi"
print(s*3)

o/p:
hihihi


s1="hi"
s2="bye"
print(s1+s2)

o/p:
hibye


s1="hi"
s2="hye"
print(s1>s2)

"""
a 97
b 98
z 122

A 65
B 66

Z 90

"""

o/p:
false

s1="hi"
s2="hi"
print(s1==s2)
o/p:
True


s="welcome"
print("c" in s)
print("d" in s)
print("d" not in s)
print("com" in s)
print("cme" in s)
print(s in "welcome")

o/p:
True
False
True
True
False
True


inbulit function
_____________________

max() – Returns the largest character (ASCII/Unicode order)

s = "python"

print(max(s))

o/p:
y


s = "pythHon"

print(min(s))

o/p:
H


s = "python"

print(sorted(s))

o/p:
['h', 'n', 'o', 'p', 't', 'y']


s = "python"
l=sorted(s)
print("".join(l))

o/p:
hnopty



s = "Python"

for index, ch in enumerate(s):
    print(index, ch)


o/p:
0 P
1 y
2 t
3 h
4 o
5 n


s = "123"
print(all(ch.isdigit() for ch in s))



s = "Python"

print(list(s))

o/p:
['P', 'y', 't', 'h', 'o', 'n']



s = "Python"

print(set(s))

o/p:

{'h', 'o', 'y', 'P', 'n', 't'}





print(ord('A'))
print(ord('a'))
print(chr(98))

o/p:
65
97
b

s = "ABC"

print(sum(ord(ch) for ch in s))

o/p:
198


s1 = "ABC"
s2 = "123"

print(list(zip(s1, s2)))


o/p:
[('A', '1'), ('B', '2'), ('C', '3')]