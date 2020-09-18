#Calculator

a = int(input('Value #1: '))
b = int(input('Value #2: '))
func = input('Choose your func: ')

def Add():
    total = a + b
    print(total)

def Subs():
    total = a - b
    print(total)

def Mult():
    total = a * b
    print(total)

def Div():
    total = a // b
    print(total)
    mod = a % b
    print("The thing no one cares: " + str(mod))

if func == 'add':
    Add()
elif func == 'subs':
    Subs()
elif func == 'mult':
    Mult()
elif func == 'div':
    Div()
else:
    print('Not available.')