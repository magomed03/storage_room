#Результаты:
#№1,2,3,4,5,6,8(1 и 2 вариант) верные
#№7 +-

#№1
import re
from string import ascii_letters

l = set('abcdefghijklmnopqrstuvwxyz авбгдеёжзийклмнопрстуфхцчшщъыьэюя ABCDEFGHIJKLMNOPQRSTUVWXYZ АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ')
s = input()
otvet = ''.join(filter(l.__contains__, s))

t = re.split(' ', otvet)
for k in t:
    for i in range(len(k)):
        if i + 3 <= int(len(k)):
            print(k[i:i + 3])
            i = i + 1

#---------------------------------------------------------------------------------------------------

#№2
x = input()
n = '0123456789'

for i in range(len(x)-9):
    if x[i] in n and x[i + 1] in n and x[i + 3] in n and x[i + 4] in n and x[i + 6] in n and x[i + 7] in n and x[i + 8] in n and x[i + 9] in n and x[i + 2] == '.' and x[i + 5] == '.':
        print(x[i + 6:i + 10] +'-'+ x[i + 3:i + 5] +'-'+ x[i:i + 2])


#---------------------------------------------------------------------------------------------------

#№3
N = int(input())
K = int(input())

if K == 0 or N == 0:
    print(0)
else:
    print(int(K / N))

#---------------------------------------------------------------------------------------------------

#№4
N = int(input())

print(N % 10)

#---------------------------------------------------------------------------------------------------

#№5
hour = 0
minute = 0

N = int(input())

hour = N / 60
minute = N % 60

if(minute < 10):
    print(f"{int(hour)}:0{int(minute)}")
else:
    print(f"{int(hour)}:{int(minute)}")

#---------------------------------------------------------------------------------------------------

#№6(Вариант 1)
x = int(input())
y = int(input())
z = int(input())

S = {x, y, z}

if len(S) == 2:
    print(2)
elif len(S) == 1:
    print(3)
else:
    print(0)

#№6(Вариант 2)
x = int(input())
y = int(input())
z = int(input())

if(x == y == z):
	print(3)

elif(x == y or x == z or y == z):
	print(2)

elif(x != y != z):
	print(0)

#---------------------------------------------------------------------------------------------------

#№7

A1 = int(input())
B1 = int(input())
C1 = int(input())
A2 = int(input())
B2 = int(input())
C2 = int(input())

if (A1 == A2 or A1 == B2 or A1 == C2) and (B1 == A2 or B1 == B2 or B1 == C2) and (C1 == A2 or C1 == B2 or C1 == C2):
    print('Ящики равны')

elif (A1 < A2 or A1 < B2 or A1 < C2) and (B1 < A2 or B1 < B2 or B1 < C2) and (C1 < A2 or C1 < B2 or C1 < C2):
    print('Первое поле меньше второго')

elif (A1 >= A2 or A1 >= B2 or A1 >= C2) and (B1 >= A2 or B1 >= B2 or B1 >= C2) and (C1 >= A2 or C1 >= B2 or C1 >= C2):
    print('Первое поле больше второго')

else:
    print('Ящики несопоставимы')

#---------------------------------------------------------------------------------------------------

#№8(1 вариант)
N = int(input())
if (N >= 11 and N <= 14):
	print(N, 'коров')
else:
	A = N % 10
	if (A == 0 or (A >= 5 and A <= 9)):
		print(N, 'коров')
if (A == 1):
	print(N, 'корова')
if (A >=2 and A <=4):
	print(N, 'коровы')

#№8(2 вариант +-)
N = int(input())

number = abs(N) % 10

if number % 10 == 1 and (N > 20 or N <= 5):
    print(f"{N} коровa")

elif (number % 10 == 2 or number % 10 == 3 or number % 10 == 4) and (N > 20 or N <= 5):
    print(f"{N} коровы")

else:
    print(f"{N} коров")
