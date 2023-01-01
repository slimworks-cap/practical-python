# bounce.py
#
# Exercise 1.5
height = 100
numbounce = 0

while numbounce != 10:
    numbounce = numbounce + 1
    height = height * (3/5)
    print(numbounce,round(height,4))
