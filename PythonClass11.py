string :
it is collection of char digit space ,...

'hi'
"hi"
'''hi'''
"""hi"""

s="hi"
print(s)
o/p:
hi
s="h'i'ram"
print(s)
o/p:
h'i'ram


s="""hi 
ram"""
print(s)

o/p:
hi
ram


s='''hi 
ram'''
print(s)

o/p:
hi
ram

s='''h"""i """
ram'''
print(s)

o/p:
h"""i """
ram


indexing
____________

s="welcome"

     0   1   2  3  4  5  6
     w   e   l  c  o  m  e
     -7  -6  -5 -4 -3 -2 -1

s[2]   l
s[-5]  l
s[5]   m
s[-2]  m


s="welcome"
print(s[3],s[-4])

o/p:
c c

s="welcome"
print(s[7])

o/p:
indexerror


slicing
______________
more char   (substring)
[start:stop:step]
[start:stop]
[start:]
[:stop]

[::]   start=0 stop-1  step value increase one




     0   1   2  3  4  5  6
     w   e   l  c  o  m  e
     -7  -6  -5 -4 -3 -2 -1
s="welcome"
print(s[2:5:1])   #lco
print(s[2:5:])    #lco
print(s[2:5])     #lco
print(s[-5:-2:1])  #lco
print(s[-5:-2:])   #lco
print(s[-5:-2])   #lco


     0   1   2  3  4  5  6
     w   e   l  c  o  m  e
     -7  -6  -5 -4 -3 -2 -1
s="welcome"
print(s[2]) #l
print(s[2:]) #lcome
print(s[-5:]) #lcome


 	0   1   2  3  4  5  6
     w   e   l  c  o  m  e
     -7  -6  -5 -4 -3 -2 -1
s="welcome"
print(s[2:5:2])  #lo
print(s[-5:5:2])  #lo
print(s[-5:-2:2])  #lo




 	0   1   2  3  4  5  6
     w   e   l  c  o  m  e
     -7  -6  -5 -4 -3 -2 -1
s="welcome"
print(s[5:2]) #nothing 
print(s[5:2:-1]) #moc



s="welcome"
print(s)
print(s[::])
print(s[0::])
print(s[-7::])
print(s[:])

o/p:
welcome
welcome
welcome
welcome
welcome

s="welcome"
print(s)
print(s[::2])
o/P:
welcome
wloe


#display string individual line by line

s="welcome"
for i in s:
	print(i)
o/p:
w
e
l
c
o
m
e


s="welcome"
print(len(s))

o/p:
7


s="welcome"
for i in range(0,len(s),1):
	print(s[i])

o/p
	print(i)
o/p:
w
e
l
c
o
m
e