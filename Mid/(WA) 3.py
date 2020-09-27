user_input = input()

length = len(user_input)
first_index = 0
last_index = length - 1
palindrome = ""

for _ in range(length):

    if user_input[first_index] == user_input[last_index]:
        palindrome += user_input[first_index]
    else:
        break
    
    first_index += 1
    last_index -= 1

count = user_input.count(palindrome)
if count == 4:
    print(palindrome)
    