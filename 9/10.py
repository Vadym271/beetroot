# task 1
def oops():
    raise IndexError

def oops2():
    print(1)
    oops()
    print(2)
#oops2()
# changing exception to KeyError calls an KeyError

# task 2
A = input("insert a:")
B = input("insert b:")

def div(a, b):
    try:
        a = float(a)
        b = float(b)
        return a**2 / b
    except ZeroDivisionError:
        print("you can't divide by 0")
    except ValueError:
        print("you shold enter numbers")
print(div(A, B))