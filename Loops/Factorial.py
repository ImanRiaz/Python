num=int(input("Enter a number you want factorial of: "))

factorial=1

for i in range(1,num+1):
    factorial*=i

print("The factorial of ",num,"is",factorial)