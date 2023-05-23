names = ["inbar", "lanir", "eran", "alina"]
# print(list(range(5)))
# print(list(range(5, 12)))
# print(list(range(5, 12, 3)))
# for name in names:
#   print(name, end=',')
# for i in range(len(name)):
#   print(names[i])
# for i in range(30):
#   print(i)

numbers = 1, 2, 3, 4, 5, 6, 7
# a = 0
# while a < 5:
#   print(a)
#  a = a + 1
# print("***********************")
for number in numbers:
    if number == 5:
        continue
    if number == 2:
        break
    print(number)
else:
    print("finished")
print("\n================================")
isTrue = False
a = 2
b = 2.5
strOne = "One"
strTwo = "Two"
if a > b and strOne == "aviel" or b > 1:
    print("a is a greater ten b")
elif not a == b:
    print("a is equals to b")
elif strOne != strTwo:
    print("blala")
else:
    print("b is greater then a")
