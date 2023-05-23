# def get_name():
#   name = input("enter your name")
# f = open("my_file_targil.txt.py", "a")
# f.write(name)
# f.close()
# f = open("my_file_targil.txt.py", "r")
# print(f.read())


# get_name()


def get_name():
    current_name = input("enter your name: ")
    my_file_targil = open("my_file_targil.txt.py", "a")
    my_file_targil.write(f"{current_name}\n")
    my_file_targil.close()

with open("my_file_targil.txt.py") as my_fyle_targil:
    for line in my_fyle_targil.readlines():
        print(line)

def show_names():
    my_file_targil = open("my_file_targil.txt.py")
    for line in my_file_targil.readlines():
        print(f"hello {line}", end='')
    my_file_targil.close()


for i in range(3):
    get_name()
show_names()
