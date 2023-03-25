# import fibo as fimonacci
from fibo import fib2 as fibonacci
import math
#fib2 = fibo.fib2

#fib2(50)

users_pi = 3.14
r = 5

result = users_pi * r**2
print(result)

modules_pi = math.pi
modules_result = modules_pi * r**2
print(modules_result)

print(math.isclose(result, modules_result, rel_tol=0.001))
