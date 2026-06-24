number system
_______________
(1)binary  0,1  base=2
(2)octal   0,1,2,3,4,5,6,7  base=8
(3)decimal 0,1,2,3,4,5,6,7,8,9 base=10
(4)hexdecimal 0,1,2,3,4,5,6,7,8,9,A,B,C,D,E,F base=16

decimal to binary
___________________
(25)10=( 11001)2

(37)10=(100101)2

a=37
b=bin(a)
print(a)
print(b)

short rule
____________


64   32    16   8    4   2   1
            1   1    0   0    1    ->25
     1       0  0    1    0   1     ->37


decimal to octal
___________________
(25)10=(31)8

(37)10=(45)8

a=37
b=oct(a)
print(a)
print(b)

short rule
____________


64   32    16   8    4   2   1
            1   1    0   0    1    ->25    31
     1      0   0    1    0   1     ->37    45  
     1     1    1    0    0   0      ->56    70


decimal to hexdecimal
___________________
(25)10=(19)16

(37)10=(25)16

a=37
b=hex(a)
print(a)
print(b)

o/p:
37
0x25
short rule
____________


64   32    16   8    4   2   1
            1   1    0   0    1    ->25       19  
     1      0   0    1    0   1     ->37      25  
     1     1    1    0    0   0      ->56      38


binary  to decimal
__________________

(1011)2=(11)10
(101011)2=(   )10
a=0b1011
b=a
print(a)
print(b)

o/p:
11
11

64   32    16   8    4   2   1
                1    0   1   1   ->11

      1     0  1     0    1  1   ->  43



octal  to decimal
__________________

(25)8=(21)10
(37)8=(31)10
a=0o25
b=a
print(a)
print(b)

o/p:
21
21

64   32    16   8    4   2   1
      0     1    0   1   0   1   25->   21
             1   1   1   1  1   37->   31



hexdecimal  to decimal
__________________

(25)16=(37)10

(B2)16=(   )10

a=0x25
b=a
print(a)
print(b)

o/p:
37
37

a=0xB2
b=a
print(a)
print(b)

o/p:
178
178
128 64   32    16   8    4   2   1
    1     0    0     1   0   1   25->    37
 1  0     1    1    0    0   1   0   B2->  178



hexdecimal to octal
____________________
(25)16=(37)10=(45)8

(B2)16=(178)10=(262)8

a=0xB2
b=oct(a)
print(a)
print(b)

o/p:
178
0o262
128 64   32    16   8    4   2   1
    1     0    0     1   0   1   25->    37
 1  0     1    1    0    0   1   0   B2->  178



octal  to hexdecimal
____________________
(25)8=(21)10=(15)16

(262)8=(178)10=(b2)16

a=0o262
b=hex(a)
print(a)
print(b)


128 64   32    16   8    4   2   1
          0     1   0     1  0   1      25 ->21->  15

 
bitwise  operator
____________________

|  bitwise or
&   bitwise and
^   bitwise xor
<<   leftshift
>>   rightshift
~    one's completer

|

1  1  1
1  0  1
0  1  1
0  0  0

&
1  1  1
1  0  0
0  1  0
0  0  1

^
1  1  0
1  0  1
0  1  1
0  0  0

a=5
b=7
print(a | b)
print(a  & b)
print(a  ^ b)

o/p:
7
5
2
     1   0   1   ->5
     1    1  1    ->7
    ____________________
     1    1    1        a |b   7          
     1     0     1       a&b   5
     0     1    0     a^b      2

a=15
b=17
print(a | b)
print(a  & b)
print(a  ^ b)


o/p:
31
1
30


a=7
print(a<<1)
print(a<<2)
print(a<<3)


o/p:
14
28
56

number * 2 power  shifting

>>

a=100
print(a>>1)
print(a>>2)
print(a>>3)



+ve number store computer directly

example  5
1 byte =8bites

0  0  0   0  0  1 0 1


-ve store   2's complemet

example   -5

1   0     0   0   0   1  0  1
    1     1   1   1   0  1  0   1's
                         +  1
 _______________________________
1   1     1    1    1   0 1  1



~
_______
a=5
print(~a)

o/p:
-6

0 0  0   0 0    1  0  1
1 1   1  1 1   0  1  0
  0   0  0 0  1   0  1
                   +  1
________________________
1  0    0   0  0 1   1   0


a=20
print(~a)

o/p:

-21



a=-4
print(~a)

o/p:
3




sub two no without using - operator


a=10
b=3
c=a+~b+1

print(c)


o/p:
7