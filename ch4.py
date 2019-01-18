
#Q1.1:
def K():
    for row in range(4):
        print('*', end='')
        for col in range(3 - row):
            print(' ', end='')
        print('*')
    for row in range(3):
        print('*', end='')
        for col in range(1 + row):
            print(' ', end='')
        print('*')

def D():
    for row in range(4):
        print('*', end='')
        for col in range(row + 1):
            print(' ', end='')
        print('*')
    for row in range(4):
        print('*', end='')
        for col in range(4 - row):
            print(' ', end='')
        print('*')

def A():
    for row in range(7):
        for space in range(6 - row):
            print(' ', end='')
        print('*', end='')
        for space in range((row * 2) + 1):
            if row == 3:
                print('*', end='')
            else:
                print(' ', end='')
        print('*')

def Y():
    for row in range(3):
        for space in range(row * 2):
            print(' ', end='')
        print('*', end='')
        for star in range(11 - (row * 4)):
            print(' ', end='')
        print('*')
    for row in range(4):
        for space in range(6):
            print(' ', end='')
        print('*')

K()
K()
D()
A()
Y()


#Q1.2:
def tree():
    a = 11
    for row in range(a):
            for space in range(a-row):
                print(' ', end='')
            for star in range(1+(row*2)):
                print('*', end='')
            print()
            for line_space in range(a):
                print(' ', end='')
            print('|')
tree()

# Q1.3:
def tree1():
    a = 9
    for row in range(a):
        for space in range(a-row):
            print(' ', end='')
        print('[', end='')
        for tilde in range(2 * row):
            if row == (a - 1):
                print('_', end='')
            else:
                print('~', end='')
        print(']')
    for row in range(2):
        for space in range(((a*2)+1)//2):
            print(' ', end='')
        print('[]')
tree1()

# Q2:
num = 2
for num in range(2, 300):
   j = 2
   for j in range(2, num):
      if num % j == 0:
         #print('不是質數')
         break
   else:
        print(num)

# Q3:
def a(n):
    a = [1, 1]
    for i in range(2, n):
        a.append(a[-1] + a[-2])
    return a
print('Q3:', a(20))



#Q4:四位數中，使用迴圈找出 0 ~ 7 所能組成的奇數個數
#01/03/05/07/ 11/13/15/17/ 21/23/25/27 31/33/35/37/ 41/43/45/47/
total = 0
b = 1
for a in range(0, 8):
    for b in range(0, 8):
        for c in range(0, 8):
            for d in range(0, 8):
                if d % 2 != 0:
                    #print(a, b, c, d)
                    total += 1
print('Q4:', total)

