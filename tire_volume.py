import math

w = float(input("What is the width of the tire? "))
a = float(input("What is the aspect ratio of the tire? "))
d = float(input("What is the diameter of the tire? "))

v = (math.pi * (w **2)) * (a) * (w * a + 2540 * d) / 10000000000

print (f"The approximate volume is {v:.2f}")
