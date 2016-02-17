import random

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

new_list = []
#for x in a and b:
#    if x in a and b:
#        new_list.append(x)

#print(new_list)

rand_1 = []
rand_2 = []
occur_both = []
lenlist_1 = int(input("How long should the first list be?\n"))
lenlist_2 = int(input("How long should the second list be?\n"))
limit = int(input("What is the upper limit on the range?\n")) + 1
for i in range(0, lenlist_1):
    rand_1.append(random.randint(0, limit))
for i in range(0, lenlist_2):
    rand_2.append(random.randint(0, limit))
for num in rand_1 and rand_2:
    if num in rand_1 and rand_2:
        occur_both.append(num)

print(occur_both)
