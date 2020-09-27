import sys

a_list = [1, 2, 3, 4, 5, 6, 1]
length = len(a_list)
result = list()

for i in range(length):
    a_list[a_list[i] % length] = a_list[a_list[i] % length] + length

for i in range(length):

    if (a_list[i] >= length * 2):
        result.append(i)

while(True):

    check = int(input())

    if check in result:
        print (check, "has duplicates")
    else:
        print (check, "doesn't have duplicates")
