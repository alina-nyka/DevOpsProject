# zero exception
# a = int(input("enter number: "))
# b = int(input("enter number: "))
result = 0
try:

    a = int(input("enter number: "))
    b = int(input("enter number: "))
    result = a / b
    f = open("sdsdfsf.txt")

except ZeroDivisionError:
    print("could nor divide by zero")
except FileNotFoundError:
    print("could not find a file")
except BaseException as e:
    print("something went wrong")
    print(e.args)
print(result)
print("aviel")
