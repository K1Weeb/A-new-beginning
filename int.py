# integration using power rule
import random


num1 = random.randint(1, 9)
num2 = random.randint(1, 9)
y = random.randint(0, 12)
x = random.randint(0, 5)
print("Integrate {}x + {}, where y = {} if x = {}".format(num1, num2, y, 5))

sq_co = num1/2
print("Integrated is {}x^2 + {}x + c".format(sq_co, num2))