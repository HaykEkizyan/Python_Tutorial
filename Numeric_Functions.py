#1 To find the maximum or minimum of some numbers or a list, you can use max or min.

print(min(0, -2, 3, 15,78))   # -2
print(max(0, -2, 3, 15,78))   # 78

#2 To find the distance of a number from zero (its absolute value), use abs.

print(abs(0, -2, 3, 15,78))  # TypeError: abs() takes exactly one argument (5 given)
print(abs(2))               # 2
print(abs(-2))              # 2

#3 To round a number to a certain number of decimal places, use round.

print(round(2.8))           # 3
print(round(2.2))           # 2
print(round(2.5))           # 2
print(round(2.500000000000001))       # 3 (13 zeroes)     ?????
print(round(2.5000000000000001))      # 2 (14 zeroes)     ?????

#4 To find the total of a list, use sum.

print(sum(1, 2, 3, 4, 5))                 # TypeError: sum() takes at most 2 arguments (5 given)
print(sum([1, 2, 3, 4, 5]))               # 15 
print(sum([1, 2, 3, 4, 5] + [1, 2]))      # 18
print(sum([1, 2, 3, 4, 5] + 1))           # TypeError: can only concatenate list (not "int") to list
