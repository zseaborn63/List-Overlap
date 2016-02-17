import random

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

new_list = []
for x in a and b:
    if x in a and b:
        new_list.append(x)

print(new_list)

rand_1 = []
rand_2 = []
occur_both = []
for i in range(0,11):
    rand_1.append(random.randint(0, 101))
for i in range(0,16):
    rand_2.append(random.randint(0, 101))
for num in rand_1 and rand_2:
    if num in rand_1 and rand_2:
        occur_both.append(num)

print(occur_both)
