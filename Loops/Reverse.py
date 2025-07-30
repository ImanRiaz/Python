num = input("Enter a number: ")
reversed_num = ""

for i in range(len(num) - 1, -1, -1):
    reversed_num += num[i]

print("Reversed number is:", reversed_num)
