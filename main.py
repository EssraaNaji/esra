

'''s = input()
s=s.split()
x = int(s[0])
y = int(s[1])

print(f'{x} + {y} = {x+y}')
print(f'{x} * {y} = {x*y}')
print(f'{x} - {y} = {x-y}')'''

'''num = int(input('Enter your number:'))
x = 1

while x <= 10 :
    print (f'{num} x {x} = {x*num}')
    x+=1'''


'''n = int(input("ادخلي رقم صحيح غير سالب: "))

if n < 0:
    print("الفاكتوريل معرفش للارقام السالبة")
else:
    result = 1
    i = 1
    while i <= n:
        result *= i
        i += 1
    print(f"{n}! = {result}")'''

'''def fact(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return n * fact(n-1)

print(fact(4))'''




'''def mul(num1, num2):
    print ('num1 * num2 = ', num1 * num2)
mul(6,4)'''



'''def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "لا يمكن القسمة على صفر"
    return x / y


print("اختر العملية:")
print("1. جمع")
print("2. طرح")
print("3. ضرب")
print("4. قسمة")

choice = input("ادخل اختيارك (1/2/3/4): ")

x = float(input("ادخل الرقم الأول: "))
y = float(input("ادخل الرقم الثاني: "))

if choice == '1':
    print(f"النتيجة: {add(x, y)}")
elif choice == '2':
    print(f"النتيجة: {subtract(x, y)}")
elif choice == '3':
    print(f"النتيجة: {multiply(x, y)}")
elif choice == '4':
    print(f"النتيجة: {divide(x, y)}")
else:
    print("اختيار غير صحيح")'''



def add(n,d):
    return n+d
def mult(n,d):
    return n*d
def divide(n,d):
    if d == 0:
        return 'error'
    else:
        return n/d
def sub(n,d):
    return n-d

print('choose')
print('1/ add')
print('2/ muliply' )
print('3/ divide')
print('4/ subtract')


choose = input('Enter Your Choice: ')

n = float(input(' Enter Your first num'))
d = float(input(' Enter Your second num'))


if choose == '1':
    print(f' result : {add(n,d)}')
elif choose == '2':
    print (f'result = {mult(n,d)}')
elif choose == '3':
    print (f'result = {divide(n,d)}')
elif choose == '4':
    print(f'result = {sub(n,d)}')
else:
    print('wrong choice')


