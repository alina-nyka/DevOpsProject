#1
#import fibo
#print(fibo.pi)
#fibo.fib(100)

#2
from fibo import fib
fib(100)

#3 if there are 2 imports with the same name of function
#so, the last one is overwritting the first one, to avoid it
# and for using both of them, need to use "alias"
#f.i.: from fibo import fib as first_fib

# from fibo import fib as first_fib
# from aviel import fib as second_fib
# first_fib(100)
# second_fib(100)